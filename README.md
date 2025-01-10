# real-estate-backend
# Flask App Setup Guide

Follow these steps to set up and run the Flask app on your system. Instructions are provided for both Windows and macOS.

## Prerequisites
Ensure the following are installed on your system:
- Python (3.7 or later)
- pip (comes pre-installed with Python)

---

## Steps

### 1. Creating a Virtual Environment
A virtual environment isolates your project's dependencies from system-wide Python installations.

#### Windows
```bash
python -m venv venv
```

#### macOS
```bash
python3 -m venv venv
```

This command creates a virtual environment named `venv` in your project directory.

---

### 2. Activating the Virtual Environment

#### Windows
- Command Prompt:
  ```bash
  venv\Scripts\activate
  ```
- PowerShell:
  ```bash
  .\venv\Scripts\Activate.ps1
  ```

#### macOS
```bash
source venv/bin/activate
```

Once activated, the virtual environment's name (e.g., `(venv)`) will appear in your terminal prompt.

---

### 3. Installing All Dependencies
Ensure you have a `requirements.txt` file listing your project dependencies.

```text
Flask
# Add other dependencies here
```

#### Install dependencies:
```bash
pip install -r requirements.txt
```

---

### 4. Running the Flask App
Ensure you have a `app.py` file (or equivalent) containing your Flask app code. For example:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

#### Command to run the app:
```bash
python app.py
```

For macOS, use `python3` if `python` defaults to Python 2.x:
```bash
python3 app.py
```

The app will start and by default, it will be accessible at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

### Notes
- If you encounter permission issues on macOS, prepend commands with `sudo` (e.g., `sudo pip install ...`).
- Use `deactivate` to exit the virtual environment when you're done.

---
