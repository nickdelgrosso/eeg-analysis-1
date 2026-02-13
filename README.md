# EEG Analysis Template with MNE-Python

A template repository for EEG data analysis using MNE-Python, with a structured workflow from raw data to final results.

## Features

- 🧠 **MNE-Python Integration**: Professional EEG/MEG analysis tools
- 📦 **Pixi Package Management**: Reproducible Python environment
- 📁 **Organized Structure**: Clear separation of raw, interim, and processed data
- 🔄 **Processing Pipeline**: Automated preprocessing, analysis, and visualization scripts
- 👥 **Team Collaboration**: Personal scratch folders for team members
- 📊 **Results Output**: Organized folder for final figures and reports

## Directory Structure

```
eeg-analysis-1/
├── data/
│   ├── raw/              # Raw EEG data files (gitignored)
│   ├── interim/          # Intermediate processing outputs
│   └── processed/        # Final processed data ready for analysis
├── scripts/
│   ├── 01_preprocess.py  # Data preprocessing pipeline
│   ├── 02_analyze.py     # Analysis and epoch creation
│   └── 03_visualize.py   # Visualization and results generation
├── notebooks/            # Jupyter notebooks for exploration
├── results/              # Final figures, tables, and reports
├── scratch/
│   ├── me/              # Personal scratch area
│   └── Sangyeob/        # Sangyeob's scratch area
├── pixi.toml            # Pixi environment configuration
└── README.md
```

## Getting Started

### Prerequisites

Install [Pixi](https://pixi.sh/):

```bash
# macOS/Linux
curl -fsSL https://pixi.sh/install.sh | bash

# Windows
iwr -useb https://pixi.sh/install.ps1 | iex
```

### Installation

1. Clone this repository:
```bash
git clone https://github.com/nickdelgrosso/eeg-analysis-1.git
cd eeg-analysis-1
```

2. Install dependencies with Pixi:
```bash
pixi install
```

### Usage

#### Running the Processing Pipeline

The analysis pipeline consists of three main steps:

1. **Preprocessing**: Filter, re-reference, and clean raw data
```bash
pixi run preprocess
```

2. **Analysis**: Create epochs and compute evoked responses
```bash
pixi run analyze
```

3. **Visualization**: Generate figures and save to results folder
```bash
pixi run visualize
```

Or run the entire pipeline at once:
```bash
pixi run pipeline
```

#### Using Jupyter Notebooks

Launch Jupyter for interactive analysis:
```bash
pixi run notebook
# or
pixi run lab
```

#### Adding Your Data

1. Place your raw EEG files in `data/raw/`
2. Supported formats: .fif, .edf, .bdf, .vhdr, .set
3. Modify the scripts in `scripts/` to match your data structure

## Workflow

### 1. Data Preparation

- Add raw EEG files to `data/raw/`
- Configure channel montage and experiment-specific parameters in scripts

### 2. Preprocessing (01_preprocess.py)

- Load raw data
- Set channel montage
- Apply bandpass filter (0.5-40 Hz)
- Mark bad channels
- Re-reference to average
- Save to `data/interim/`

### 3. Analysis (02_analyze.py)

- Load preprocessed data
- Detect events/triggers
- Create epochs
- Apply baseline correction
- Reject bad epochs
- Compute evoked responses
- Save to `data/processed/`

### 4. Visualization (03_visualize.py)

- Load processed data
- Generate butterfly plots
- Create topographic maps
- Plot power spectral density
- Compare conditions
- Save figures to `results/`

## Customization

### Modifying the Pipeline

Edit the Python scripts in `scripts/` to customize:
- Filter parameters
- Epoch windows
- Event IDs
- Channel selection
- Analysis methods

### Adding Dependencies

Add new Python packages to `pixi.toml`:
```toml
[dependencies]
your-package = ">=1.0.0"
```

Then run:
```bash
pixi install
```

## Scratch Folders

Personal scratch folders are provided for temporary work:
- `scratch/me/` - Your personal scratch area
- `scratch/Sangyeob/` - Sangyeob's scratch area

These folders are gitignored and perfect for:
- Quick experiments
- Temporary scripts
- Personal notes
- Work-in-progress analyses

## Tips

- Keep raw data in `data/raw/` but don't commit it to git (it's in .gitignore)
- Document your analysis steps in Jupyter notebooks
- Save important figures to `results/` for sharing
- Use meaningful filenames for processed data
- Check data quality at each processing step

## Dependencies

Main packages (managed by Pixi):
- Python 3.10+
- MNE-Python >= 1.6.0
- NumPy >= 1.24.0
- SciPy >= 1.10.0
- Matplotlib >= 3.7.0
- Pandas >= 2.0.0
- Jupyter >= 1.0.0
- Seaborn >= 0.12.0

See `pixi.toml` for complete list.

## Contributing

1. Create a feature branch
2. Make your changes
3. Test the pipeline
4. Submit a pull request

## License

[Add your license here]

## Resources

- [MNE-Python Documentation](https://mne.tools/)
- [MNE-Python Tutorials](https://mne.tools/stable/auto_tutorials/index.html)
- [Pixi Documentation](https://pixi.sh/)

## Contact

[Add contact information]