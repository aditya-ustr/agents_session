# agents_session

A Python project for working with AI agents, embeddings, and language models.

## Quick Setup

### Automated Setup (Recommended)

Run the setup script to automatically:
- Create a virtual environment
- Install all dependencies
- Download and cache the FlagEmbedding model

```bash
python setup.py
```

The script will create a `venv` directory and display activation instructions for your shell.

---

## Manual Setup

If you prefer to set up manually, follow these steps:

### Step 1: Create Virtual Environment

```bash
# On Windows (CMD)
python -m venv venv

# On Windows (PowerShell)
python -m venv venv

# On Windows (Git Bash)
python -m venv venv

# On macOS/Linux
python3 -m venv venv
```

### Step 2: Activate Virtual Environment

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**Windows (Git Bash):**
```bash
source venv/Scripts/activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r application_source/requirements.txt
```

### Step 4: Download and Cache Model

```bash
python -c "from FlagEmbedding import FlagModel; model = FlagModel('BAAI/bge-small-en-v1.5', use_fp16=True)"
```

This downloads and caches the BAAI/bge-small-en-v1.5 embedding model locally.

---

### Deactivate Virtual Environment

To exit the virtual environment:
```bash
deactivate
```

---

## Project Structure

```
.
├── README.md                           # This file
├── setup.py                            # Automated setup script
├── application_source/
│   ├── requirements.txt               # Python dependencies
│   └── notebooks/
│       └── demo.ipynb                 # Demo notebook
```

---

## Requirements

- Python 3.8+
- pip (Python package manager)
- ~2GB disk space (for model caching)

---

## Troubleshooting

### Virtual environment not activating?
- Ensure you're running the command from the project root directory
- Try using absolute paths to the activate script
- Check that you have execute permissions (especially on macOS/Linux)

### FlagEmbedding import error?
- Make sure the virtual environment is activated
- Run `pip install -r application_source/requirements.txt` again
- Check your internet connection (required for model download)

### Model download fails?
- Ensure you have 2GB+ of free disk space
- Check your internet connection
- Try running manually: `python -c "from FlagEmbedding import FlagModel; FlagModel('BAAI/bge-small-en-v1.5', use_fp16=True)"`