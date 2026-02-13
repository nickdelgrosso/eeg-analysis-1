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

# ============================================================================
# CONFIGURATION - MODIFY THESE FOR YOUR DATA
# ============================================================================

# Filter parameters
FILTER_L_FREQ = 0.5   # High-pass filter frequency (Hz)
FILTER_H_FREQ = 40.0  # Low-pass filter frequency (Hz)

# Channel montage - change to match your electrode setup
# Options: 'standard_1020', 'standard_1005', 'biosemi64', etc.
# See: https://mne.tools/stable/generated/mne.channels.make_standard_montage.html
MONTAGE_NAME = 'standard_1020'

# Re-referencing method
# Options: 'average', ['M1', 'M2'] (for specific channels), etc.
REFERENCE_METHOD = 'average'

# Bad channels (if known) - add channel names here
BAD_CHANNELS = []  # Example: ['Fp1', 'Fp2']

# ============================================================================


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
    
    # Set montage
    print(f"Setting montage: {MONTAGE_NAME}")
    montage = mne.channels.make_standard_montage(MONTAGE_NAME)
    raw.set_montage(montage, on_missing='warn')
    
    # Filter data
    print(f"Filtering data ({FILTER_L_FREQ}-{FILTER_H_FREQ} Hz)...")
    raw.filter(l_freq=FILTER_L_FREQ, h_freq=FILTER_H_FREQ, fir_design='firwin')
    
    # Mark bad channels
    if BAD_CHANNELS:
        print(f"Marking bad channels: {BAD_CHANNELS}")
        raw.info['bads'] = BAD_CHANNELS
    
    # Re-reference
    print(f"Re-referencing to: {REFERENCE_METHOD}")
    raw.set_eeg_reference(REFERENCE_METHOD, projection=False)
    
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
