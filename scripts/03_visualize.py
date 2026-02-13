#!/usr/bin/env python
"""
Step 3: Visualize EEG Results

This script creates visualizations of processed EEG data and saves them to results.
"""

import mne
import matplotlib.pyplot as plt
from pathlib import Path

# Configure paths
DATA_PROCESSED = Path("data/processed")
RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True, parents=True)

# Set matplotlib backend
plt.switch_backend('Agg')


def extract_condition_from_filename(filepath):
    """
    Extract condition name from evoked file path.
    
    Expected filename format: [subject_]condition_ave.fif
    Examples:
        - 'auditory_left_ave.fif' -> 'auditory_left'
        - 'subject01_auditory_left_ave.fif' -> 'auditory_left'
        - 'sub01_visual_right_ave.fif' -> 'visual_right'
    
    Args:
        filepath: Path object for the evoked file
        
    Returns:
        str: Condition name extracted from filename
    """
    # Remove _ave suffix
    name = filepath.stem.replace('_ave', '')
    
    # Split by underscore
    parts = name.split('_')
    
    # If filename starts with common subject prefixes, skip them
    # Otherwise, use all parts as condition name
    if len(parts) > 1 and (parts[0].startswith('sub') or 
                           parts[0].startswith('subj') or 
                           parts[0].lower().startswith('s') and parts[0][1:].isdigit()):
        # Skip subject prefix, use rest as condition
        condition = '_'.join(parts[1:])
    else:
        # Use entire name as condition
        condition = name
    
    return condition


def plot_evoked_responses(evoked_files):
    """
    Create plots of evoked responses.
    
    Expected filename format: [subject_]condition_ave.fif
    Example: subject01_auditory_left_ave.fif or auditory_left_ave.fif
    """
    print(f"\n{'='*60}")
    print("Plotting evoked responses")
    print(f"{'='*60}\n")
    
    # Group files by condition
    evoked_by_condition = {}
    for evoked_file in evoked_files:
        try:
            evoked = mne.read_evokeds(evoked_file)[0]
            condition_name = extract_condition_from_filename(evoked_file)
            
            if not condition_name:
                print(f"⚠ Warning: Could not extract condition from {evoked_file.name}, skipping...")
                continue
            
            if condition_name not in evoked_by_condition:
                evoked_by_condition[condition_name] = []
            evoked_by_condition[condition_name].append(evoked)
        except Exception as e:
            print(f"⚠ Warning: Could not process {evoked_file.name}: {e}")
            continue
    
    # Plot each condition
    for condition, evokeds in evoked_by_condition.items():
        print(f"Plotting {condition}...")
        
        # Butterfly plot
        fig = evokeds[0].plot(spatial_colors=True, gfp=True, show=False)
        output_file = RESULTS / f"evoked_{condition}_butterfly.png"
        fig.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close(fig)
        print(f"  Saved butterfly plot to {output_file}")
        
        # Topographic plot
        fig = evokeds[0].plot_topomap(times='auto', show=False)
        output_file = RESULTS / f"evoked_{condition}_topomap.png"
        fig.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close(fig)
        print(f"  Saved topomap to {output_file}")
        
        # Joint plot
        fig = evokeds[0].plot_joint(show=False)
        output_file = RESULTS / f"evoked_{condition}_joint.png"
        fig.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close(fig)
        print(f"  Saved joint plot to {output_file}")
    
    print(f"✓ Evoked visualization complete!\n")


def plot_epochs_overview(epochs_files):
    """
    Create overview plots of epochs.
    """
    print(f"\n{'='*60}")
    print("Creating epochs overview")
    print(f"{'='*60}\n")
    
    for epochs_file in epochs_files:
        print(f"Processing {epochs_file.name}...")
        epochs = mne.read_epochs(epochs_file, preload=True)
        
        # Plot image (average over epochs)
        fig = epochs.plot_image(picks='eeg', combine='mean', show=False)
        output_file = RESULTS / f"{epochs_file.stem}_image.png"
        fig[0].savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close(fig[0])
        print(f"  Saved epochs image to {output_file}")
        
        # Plot PSD
        fig = epochs.compute_psd(fmin=1, fmax=40).plot(show=False)
        output_file = RESULTS / f"{epochs_file.stem}_psd.png"
        fig.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close(fig)
        print(f"  Saved PSD plot to {output_file}")
    
    print(f"✓ Epochs visualization complete!\n")


def compare_conditions(evoked_files):
    """
    Create comparison plots across conditions.
    """
    print(f"\n{'='*60}")
    print("Creating condition comparisons")
    print(f"{'='*60}\n")
    
    # Load all evoked responses
    evokeds = []
    labels = []
    for evoked_file in evoked_files:
        try:
            evoked = mne.read_evokeds(evoked_file)[0]
            condition_name = extract_condition_from_filename(evoked_file)
            
            if condition_name:
                evokeds.append(evoked)
                labels.append(condition_name)
        except Exception as e:
            print(f"⚠ Warning: Could not load {evoked_file.name}: {e}")
            continue
    
    if len(evokeds) > 1:
        # Compare all conditions
        print(f"Comparing {len(evokeds)} conditions...")
        fig = mne.viz.plot_compare_evokeds(
            dict(zip(labels, evokeds)),
            picks='eeg',
            show=False
        )
        output_file = RESULTS / "evoked_comparison.png"
        fig[0].savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close(fig[0])
        print(f"  Saved comparison plot to {output_file}")
    
    print(f"✓ Condition comparison complete!\n")


def main():
    """Main visualization pipeline."""
    print("\n" + "="*60)
    print("EEG VISUALIZATION PIPELINE")
    print("="*60)
    
    # Find processed files
    evoked_files = list(DATA_PROCESSED.glob("*_ave.fif"))
    epochs_files = list(DATA_PROCESSED.glob("*_epo.fif"))
    
    if not evoked_files and not epochs_files:
        print("\n⚠ No processed files found in data/processed/")
        print("Please run 01_preprocess.py and 02_analyze.py first.")
        return
    
    # Create visualizations
    try:
        if evoked_files:
            plot_evoked_responses(evoked_files)
            compare_conditions(evoked_files)
        
        if epochs_files:
            plot_epochs_overview(epochs_files)
        
        print(f"\nVisualization complete!")
        print(f"Results saved to {RESULTS}/")
        
    except Exception as e:
        print(f"✗ Error during visualization: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
