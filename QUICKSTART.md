# Quick Start Guide

## Installation

1. **Install Pixi** (if not already installed):
   ```bash
   # macOS/Linux
   curl -fsSL https://pixi.sh/install.sh | bash
   
   # Windows
   iwr -useb https://pixi.sh/install.ps1 | iex
   ```

2. **Install dependencies**:
   ```bash
   pixi install
   ```

3. **Verify setup**:
   ```bash
   python verify_setup.py
   ```

## Adding Your Data

1. Place your raw EEG files in `data/raw/`:
   - Supported formats: .fif, .edf, .bdf, .vhdr, .set
   - These files will not be committed to git (they're in .gitignore)

2. If needed, modify the scripts in `scripts/` to match your:
   - Event codes/triggers
   - Channel names
   - Epoch windows
   - Filter parameters

## Running the Analysis

### Option 1: Run the full pipeline
```bash
pixi run pipeline
```

### Option 2: Run steps individually
```bash
# Step 1: Preprocess raw data
pixi run preprocess

# Step 2: Create epochs and compute evoked responses  
pixi run analyze

# Step 3: Generate visualizations
pixi run visualize
```

### Option 3: Interactive analysis with Jupyter
```bash
# Start Jupyter Notebook
pixi run notebook

# Or start Jupyter Lab
pixi run lab
```

## Customizing the Analysis

### Preprocessing (scripts/01_preprocess.py)
- Modify filter parameters (currently 0.5-40 Hz)
- Change montage (currently standard_1020)
- Add/remove bad channels
- Change re-referencing scheme

### Analysis (scripts/02_analyze.py)
- Modify event IDs to match your experiment
- Adjust epoch time windows (currently -0.2 to 0.5 s)
- Change baseline correction period
- Adjust artifact rejection thresholds

### Visualization (scripts/03_visualize.py)
- Add new plot types
- Modify figure parameters
- Customize color schemes
- Export in different formats

## Using Scratch Folders

Personal scratch folders are perfect for:
- Quick experiments
- Testing new analysis ideas
- Personal notes and temporary scripts
- Work-in-progress code

```bash
# Your personal area
scratch/me/

# Sangyeob's area
scratch/Sangyeob/
```

**Note**: Everything in `scratch/` is gitignored and won't be committed.

## Output

### Interim data
- Location: `data/interim/`
- Contains: Preprocessed, filtered data

### Processed data
- Location: `data/processed/`
- Contains: Clean epochs, evoked responses

### Results
- Location: `results/`
- Contains: Figures, plots, statistical results
- These CAN be committed to git (not in .gitignore)

## Common Tasks

### Add a new Python package
```bash
# Edit pixi.toml to add the package
# Then run:
pixi install
```

### Run a single script without pixi
```bash
pixi run python scripts/01_preprocess.py
```

### Check what tasks are available
```bash
pixi task list
```

### Clean up processed data
```bash
rm -rf data/interim/* data/processed/*
```

## Troubleshooting

### "No raw .fif files found"
- Add your EEG data files to `data/raw/`
- Or download sample data from MNE-Python

### "Events not found"
- Check your stimulus channel name in the scripts
- Verify your data contains event markers

### "Bad channel errors"
- Review and update channel names to match your montage
- Check that channel names in data match standard montage

### Import errors
- Make sure you've run `pixi install`
- Check that you're running commands with `pixi run`

## Need Help?

- MNE-Python docs: https://mne.tools/
- MNE tutorials: https://mne.tools/stable/auto_tutorials/
- Pixi docs: https://pixi.sh/

For questions specific to this template, see README.md or open an issue.
