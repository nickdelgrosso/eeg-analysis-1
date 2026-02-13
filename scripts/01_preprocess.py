#!/usr/bin/env python
"""
Step 1: Preprocess EEG Data

This script demonstrates basic preprocessing steps for EEG data using MNE-Python.
"""

import mne
import numpy as np
from pathlib import Path

# Configure paths
DATA_RAW = Path("data/raw")
DATA_INTERIM = Path("data/interim")
DATA_INTERIM.mkdir(exist_ok=True, parents=True)


def preprocess_eeg(raw_file):
    """
    Preprocess raw EEG data.
    
    Steps:
    1. Load raw data
    2. Set montage
    3. Filter data
    4. Mark bad channels
    5. Re-reference
    6. Save interim data
    """
    print(f"\n{'='*60}")
    print(f"Preprocessing: {raw_file.name}")
    print(f"{'='*60}\n")
    
    # Load raw data
    print("Loading raw data...")
    raw = mne.io.read_raw_fif(raw_file, preload=True)
    
    # Set montage (example: standard 10-20 system)
    print("Setting montage...")
    montage = mne.channels.make_standard_montage('standard_1020')
    raw.set_montage(montage, on_missing='warn')
    
    # Filter data (bandpass 0.5-40 Hz)
    print("Filtering data (0.5-40 Hz)...")
    raw.filter(l_freq=0.5, h_freq=40.0, fir_design='firwin')
    
    # Optionally mark bad channels (manual or automatic)
    # raw.info['bads'] = ['Fp1', 'Fp2']  # Example
    
    # Re-reference to average
    print("Re-referencing to average...")
    raw.set_eeg_reference('average', projection=False)
    
    # Save interim data
    output_file = DATA_INTERIM / f"{raw_file.stem}_preprocessed.fif"
    print(f"Saving preprocessed data to {output_file}")
    raw.save(output_file, overwrite=True)
    
    print(f"✓ Preprocessing complete!\n")
    return raw


def main():
    """Main preprocessing pipeline."""
    print("\n" + "="*60)
    print("EEG PREPROCESSING PIPELINE")
    print("="*60)
    
    # Find all raw .fif files
    raw_files = list(DATA_RAW.glob("*.fif"))
    
    if not raw_files:
        print("\n⚠ No raw .fif files found in data/raw/")
        print("Please add your EEG data files to the data/raw/ folder.")
        print("\nTo create sample data, you can use:")
        print("  import mne")
        print("  raw = mne.io.read_raw_fif(mne.datasets.sample.data_path() + '/MEG/sample/sample_audvis_raw.fif')")
        return
    
    # Process each file
    for raw_file in raw_files:
        try:
            preprocess_eeg(raw_file)
        except Exception as e:
            print(f"✗ Error processing {raw_file.name}: {e}")
    
    print(f"\nPreprocessing complete! Processed {len(raw_files)} file(s).")


if __name__ == "__main__":
    main()
