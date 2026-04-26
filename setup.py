#!/usr/bin/env python3
"""
Setup script for agents_session project.
Handles virtual environment creation and package installation.
"""

import os
import sys
import subprocess
import venv
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.absolute()
VENV_DIR = PROJECT_ROOT / "venv"
REQUIREMENTS_FILE = PROJECT_ROOT / "application_source" / "requirements.txt"


def create_virtual_environment():
    """Create a virtual environment in the project root."""
    print(f"Creating virtual environment at: {VENV_DIR}")
    
    if VENV_DIR.exists():
        print(f"Virtual environment already exists at {VENV_DIR}")
        return True
    
    try:
        venv.create(VENV_DIR, with_pip=True)
        print("✓ Virtual environment created successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to create virtual environment: {e}")
        return False


def get_venv_python_executable():
    """Get the path to the Python executable in the virtual environment."""
    if sys.platform == "win32":
        return VENV_DIR / "Scripts" / "python.exe"
    else:
        return VENV_DIR / "bin" / "python"


def get_venv_pip_executable():
    """Get the path to the pip executable in the virtual environment."""
    if sys.platform == "win32":
        return VENV_DIR / "Scripts" / "pip.exe"
    else:
        return VENV_DIR / "bin" / "pip"


def install_requirements():
    """Install packages from requirements.txt into the virtual environment."""
    if not REQUIREMENTS_FILE.exists():
        print(f"Warning: requirements.txt not found at {REQUIREMENTS_FILE}")
        return False
    
    pip_executable = get_venv_pip_executable()
    print(f"\nInstalling packages from {REQUIREMENTS_FILE}...")
    
    try:
        subprocess.check_call(
            [str(pip_executable), "install", "-r", str(REQUIREMENTS_FILE)]
        )
        print("✓ Packages installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to install packages: {e}")
        return False


def download_and_cache_model():
    """Download and cache the FlagEmbedding model locally using venv Python."""
    print("\nDownloading and caching FlagEmbedding model...")
    print("This may take a few minutes on first run...")
    
    python_executable = get_venv_python_executable()
    
    # Python code to run in venv
    model_code = """
from FlagEmbedding import FlagModel
print("Loading model: BAAI/bge-small-en-v1.5")
model = FlagModel('BAAI/bge-small-en-v1.5', use_fp16=True)
print("Model loaded successfully")
"""
    
    try:
        subprocess.check_call(
            [str(python_executable), "-c", model_code],
            cwd=str(PROJECT_ROOT)
        )
        print("✓ Model downloaded and cached successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to download model: {e}")
        print("  Make sure FlagEmbedding is installed in the virtual environment")
        return False
    except Exception as e:
        print(f"✗ Error running model download: {e}")
        return False


def is_git_bash():
    """Check if running in Git Bash environment."""
    return "MSYSTEM" in os.environ and sys.platform == "win32"


def print_activation_instructions():
    """Print instructions for activating the virtual environment."""
    print("\n" + "=" * 60)
    print("Virtual environment setup complete!")
    print("=" * 60)
    
    if sys.platform == "win32":
        if is_git_bash():
            # Git Bash on Windows
            activate_cmd = f"source {str(VENV_DIR).replace(chr(92), '/')}/Scripts/activate"
            print(f"\nGit Bash detected!")
            print(f"To activate the virtual environment, run:")
            print(f"  {activate_cmd}")
        else:
            # Native Windows CMD/PowerShell
            activate_cmd = f"{VENV_DIR}\\Scripts\\activate"
            print(f"\nFor Command Prompt (cmd), run:")
            print(f"  {activate_cmd}")
            print(f"\nFor PowerShell, run:")
            print(f"  .\\{VENV_DIR}\\Scripts\\Activate.ps1")
            print(f"\nFor Git Bash, run:")
            print(f"  source {VENV_DIR}/Scripts/activate")
    else:
        activate_cmd = f"source {VENV_DIR}/bin/activate"
        print(f"\nTo activate the virtual environment, run:")
        print(f"  {activate_cmd}")
    
    print("\nTo deactivate the virtual environment, run:")
    print("  deactivate")
    print("=" * 60 + "\n")


def main():
    """Main setup routine."""
    print("Setting up agents_session project...\n")
    
    # Step 1: Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Step 2: Install requirements
    if not install_requirements():
        print("Warning: Some packages may not have been installed correctly")
    
    # Step 3: Download and cache model
    if not download_and_cache_model():
        print("Warning: Model download may have failed, but setup will continue")
    
    # Step 4: Print activation instructions
    print_activation_instructions()
    
    print("Setup complete! You can now use your virtual environment.")


if __name__ == "__main__":
    main()
