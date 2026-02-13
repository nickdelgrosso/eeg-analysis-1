# Contributing Guide

## Workflow for Team Members

### Daily Workflow

1. **Pull latest changes**:
   ```bash
   git pull origin main
   ```

2. **Work in your scratch folder** for experiments:
   ```bash
   # Use your personal scratch area
   cd scratch/me/  # or scratch/Sangyeob/
   ```

3. **When you have working code**, move it to the appropriate location:
   - Processing scripts → `scripts/`
   - Analysis notebooks → `notebooks/`
   - Reusable code → create a `src/` folder (if needed)

### Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Update scripts in `scripts/`
   - Add notebooks to `notebooks/`
   - Update documentation in README

3. **Test your changes**:
   ```bash
   pixi run pipeline
   ```

4. **Commit and push**:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin feature/your-feature-name
   ```

5. **Create a pull request** on GitHub

## Code Standards

### Python Style
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

### Script Structure
- Include a main() function
- Add helpful print statements for progress
- Handle errors gracefully
- Document expected inputs/outputs

### Notebooks
- Add markdown cells to explain your analysis
- Clear outputs before committing
- Use meaningful cell titles
- Include references for methods used

## Adding New Dependencies

If you need a new Python package:

1. **Edit pixi.toml**:
   ```toml
   [dependencies]
   your-package = ">=1.0.0"
   ```

2. **Install and test**:
   ```bash
   pixi install
   ```

3. **Commit the change**:
   ```bash
   git add pixi.toml pixi.lock
   git commit -m "Add your-package dependency"
   ```

## Organizing Data

### Raw Data
- **Never commit raw data files** (they're gitignored)
- Document data location and access instructions in README
- Use consistent naming: `subjectID_sessionID_condition.fif`

### Processed Data
- Processed data files (.fif) are also gitignored
- Document processing steps in scripts
- Include date/version in filenames for tracking

### Results
- Results (figures, tables) CAN be committed
- Use descriptive filenames
- Save in appropriate format (PNG for figures, CSV for tables)
- Document how each result was generated

## Documentation

### When to Update README
- Adding new features
- Changing workflow
- Adding new dependencies
- Modifying directory structure

### When to Update QUICKSTART
- Adding common tasks
- New troubleshooting solutions
- Simplifying setup process

### Code Comments
- Explain WHY, not WHAT (code shows what)
- Document parameter choices
- Note any assumptions or limitations

## Scratch Folder Usage

The `scratch/` folder is for:
- ✓ Testing new ideas
- ✓ Quick experiments
- ✓ Personal notes
- ✓ Temporary scripts
- ✓ Work in progress

The `scratch/` folder is NOT for:
- ✗ Final code (move to `scripts/`)
- ✗ Important results (move to `results/`)
- ✗ Shared notebooks (move to `notebooks/`)

## Communication

### Code Reviews
- Review others' pull requests
- Provide constructive feedback
- Test changes when possible
- Approve once satisfied

### Meetings
- Share progress and challenges
- Discuss methodology decisions
- Plan upcoming analyses
- Review results together

### Documentation
- Document decisions in comments/docstrings
- Update README for major changes
- Keep QUICKSTART current
- Add issues for known problems

## Best Practices

### Version Control
- Commit often with clear messages
- Don't commit sensitive data
- Don't commit large data files
- Keep commits focused and atomic

### Reproducibility
- Pin dependency versions in pixi.toml
- Document random seeds used
- Note date and software versions
- Save preprocessing parameters

### Data Management
- Keep raw data pristine
- Save intermediate steps
- Use version numbers for major changes
- Document data quality issues

### Collaboration
- Communicate early and often
- Ask questions when unsure
- Share knowledge and resources
- Help review each other's work

## Getting Help

If you're stuck:
1. Check the documentation (README, QUICKSTART)
2. Search MNE-Python docs
3. Ask your teammate
4. Create an issue on GitHub
5. Check MNE-Python forums/GitHub issues

## Questions?

Contact the team or open an issue on GitHub.
