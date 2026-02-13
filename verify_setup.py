#!/usr/bin/env python
"""
Setup verification script for the EEG analysis template.

This script checks that the directory structure is correct and provides
guidance for getting started.
"""

from pathlib import Path
import sys


def check_directory_structure():
    """Verify all required directories exist."""
    print("Checking directory structure...")
    
    required_dirs = [
        'data/raw',
        'data/interim',
        'data/processed',
        'scripts',
        'notebooks',
        'results',
        'scratch/me',
        'scratch/Sangyeob'
    ]
    
    all_good = True
    for dir_path in required_dirs:
        path = Path(dir_path)
        if path.exists() and path.is_dir():
            print(f"  ✓ {dir_path}")
        else:
            print(f"  ✗ {dir_path} - MISSING")
            all_good = False
    
    return all_good


def check_files():
    """Verify all required files exist."""
    print("\nChecking required files...")
    
    required_files = [
        'pixi.toml',
        'README.md',
        '.gitignore',
        'scripts/01_preprocess.py',
        'scripts/02_analyze.py',
        'scripts/03_visualize.py'
    ]
    
    all_good = True
    for file_path in required_files:
        path = Path(file_path)
        if path.exists() and path.is_file():
            print(f"  ✓ {file_path}")
        else:
            print(f"  ✗ {file_path} - MISSING")
            all_good = False
    
    return all_good


def check_pixi():
    """Check if pixi is installed."""
    print("\nChecking pixi installation...")
    
    import subprocess
    try:
        result = subprocess.run(['pixi', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  ✓ Pixi is installed: {result.stdout.strip()}")
            return True
        else:
            print("  ✗ Pixi is not working correctly")
            return False
    except FileNotFoundError:
        print("  ✗ Pixi is not installed")
        print("\n  Install pixi from: https://pixi.sh/")
        print("  macOS/Linux: curl -fsSL https://pixi.sh/install.sh | bash")
        print("  Windows: iwr -useb https://pixi.sh/install.ps1 | iex")
        return False


def print_next_steps(pixi_installed):
    """Print next steps for the user."""
    print("\n" + "="*60)
    print("NEXT STEPS")
    print("="*60)
    
    if pixi_installed:
        print("\n1. Install dependencies:")
        print("   pixi install")
        print("\n2. Add your EEG data to data/raw/")
        print("\n3. Run the processing pipeline:")
        print("   pixi run preprocess")
        print("   pixi run analyze")
        print("   pixi run visualize")
        print("\n4. Or run the full pipeline:")
        print("   pixi run pipeline")
        print("\n5. Launch Jupyter for interactive analysis:")
        print("   pixi run notebook")
    else:
        print("\n1. Install pixi from https://pixi.sh/")
        print("\n2. Run this script again to verify installation")
        print("\n3. Then run: pixi install")
    
    print("\nFor more information, see README.md")
    print("="*60)


def main():
    """Main verification function."""
    print("\n" + "="*60)
    print("EEG ANALYSIS TEMPLATE - SETUP VERIFICATION")
    print("="*60 + "\n")
    
    # Check directory structure
    dirs_ok = check_directory_structure()
    
    # Check files
    files_ok = check_files()
    
    # Check pixi
    pixi_ok = check_pixi()
    
    # Summary
    print("\n" + "="*60)
    print("VERIFICATION SUMMARY")
    print("="*60)
    
    if dirs_ok and files_ok:
        print("✓ Directory structure: OK")
        print("✓ Required files: OK")
        if pixi_ok:
            print("✓ Pixi installation: OK")
            print("\n🎉 Setup is complete! Ready to start analyzing EEG data.")
        else:
            print("⚠ Pixi installation: NOT FOUND")
            print("\n⚠ Please install pixi to use this template.")
    else:
        print("✗ Some components are missing")
        print("\n⚠ Please check the errors above and fix them.")
        sys.exit(1)
    
    # Print next steps
    print_next_steps(pixi_ok)


if __name__ == "__main__":
    main()
