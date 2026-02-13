#!/usr/bin/env python
"""
Step 2: Analyze EEG Data

This script demonstrates analysis steps for preprocessed EEG data.
"""

import mne
import numpy as np
from pathlib import Path

# Configure paths
DATA_INTERIM = Path("data/interim")
DATA_PROCESSED = Path("data/processed")
DATA_PROCESSED.mkdir(exist_ok=True, parents=True)


def create_epochs(raw_file):
    """
    Create epochs from preprocessed data.
    
    Steps:
    1. Load preprocessed data
    2. Find events
    3. Create epochs
    4. Baseline correction
    5. Reject bad epochs
    6. Save processed epochs
    """
    print(f"\n{'='*60}")
    print(f"Creating epochs: {raw_file.name}")
    print(f"{'='*60}\n")
    
    # Load preprocessed data
    print("Loading preprocessed data...")
    raw = mne.io.read_raw_fif(raw_file, preload=True)
    
    # Find events (this is dataset-specific)
    print("Finding events...")
    events = mne.find_events(raw, stim_channel='STI 014', min_duration=0.002)
    
    # Define event IDs (example)
    event_id = {
        'auditory/left': 1,
        'auditory/right': 2,
        'visual/left': 3,
        'visual/right': 4
    }
    
    # Create epochs
    print("Creating epochs...")
    epochs = mne.Epochs(
        raw, 
        events, 
        event_id=event_id,
        tmin=-0.2, 
        tmax=0.5,
        baseline=(None, 0),
        preload=True,
        reject=dict(eeg=100e-6),  # Reject epochs with amplitude > 100 µV
        reject_by_annotation=True
    )
    
    print(f"Created {len(epochs)} epochs")
    print(f"Dropped {epochs.drop_log_stats()}% of epochs")
    
    # Save processed epochs
    output_file = DATA_PROCESSED / f"{raw_file.stem.replace('_preprocessed', '')}_epo.fif"
    print(f"Saving epochs to {output_file}")
    epochs.save(output_file, overwrite=True)
    
    print(f"✓ Epoch creation complete!\n")
    return epochs


def compute_evoked(epochs_file):
    """
    Compute evoked responses from epochs.
    """
    print(f"\n{'='*60}")
    print(f"Computing evoked responses: {epochs_file.name}")
    print(f"{'='*60}\n")
    
    # Load epochs
    print("Loading epochs...")
    epochs = mne.read_epochs(epochs_file, preload=True)
    
    # Compute evoked responses for each condition
    print("Computing evoked responses...")
    evoked_dict = {}
    for condition in epochs.event_id.keys():
        evoked_dict[condition] = epochs[condition].average()
        print(f"  {condition}: {len(epochs[condition])} trials")
    
    # Save evoked responses
    for condition, evoked in evoked_dict.items():
        output_file = DATA_PROCESSED / f"{epochs_file.stem.replace('_epo', '')}_{condition.replace('/', '_')}_ave.fif"
        print(f"Saving evoked response for '{condition}' to {output_file}")
        evoked.save(output_file, overwrite=True)
    
    print(f"✓ Evoked computation complete!\n")
    return evoked_dict


def main():
    """Main analysis pipeline."""
    print("\n" + "="*60)
    print("EEG ANALYSIS PIPELINE")
    print("="*60)
    
    # Find all preprocessed files
    preprocessed_files = list(DATA_INTERIM.glob("*_preprocessed.fif"))
    
    if not preprocessed_files:
        print("\n⚠ No preprocessed files found in data/interim/")
        print("Please run 01_preprocess.py first.")
        return
    
    # Process each file
    for preprocessed_file in preprocessed_files:
        try:
            epochs = create_epochs(preprocessed_file)
            # Compute evoked responses
            epochs_file = DATA_PROCESSED / f"{preprocessed_file.stem.replace('_preprocessed', '')}_epo.fif"
            if epochs_file.exists():
                compute_evoked(epochs_file)
        except Exception as e:
            print(f"✗ Error processing {preprocessed_file.name}: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\nAnalysis complete! Processed {len(preprocessed_files)} file(s).")


if __name__ == "__main__":
    main()
