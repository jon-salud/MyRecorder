# MyRecorder Application

A simple audio recording application built with Python and Tkinter.

## Prerequisites

- Python 3.x (Important: Download and install from [python.org](https://www.python.org/downloads/))
  - During installation, make sure to check "Add Python to PATH"
- Required Python packages:
  - sounddevice
  - scipy
  - tkinter (usually comes with Python)
  - numpy

## Installation

1. Install Python:
   - Download Python from [python.org](https://www.python.org/downloads/)
   - Run the installer
   - ✅ Check "Add Python to PATH" during installation
   - Click "Install Now"

2. Verify Python installation by opening Command Prompt and typing:

```bash
py --version
```

3. Install the required packages:

```bash
py -m pip install sounddevice scipy numpy
```

## Running the Application

1. Navigate to the application directory:

```bash
cd /path/to/MyRecorder
```

2. Create a logs directory:

```bash
mkdir logs
```

3. Run the main script:

```bash
py main.py
```

## Usage

1. Click "Start Recording" to begin recording audio
2. Click "Stop Recording" to stop and save the recording
3. The recorded file will be saved in the same directory as 'recorded_audio.wav'
4. Use "Play" to listen to the last recorded audio
5. Use "Stop" to stop the playback

## Note

Make sure your microphone is properly connected and selected as the default input device in your system settings.

## Troubleshooting

### Python Not Found Error

If you get "Python was not found" error, try these steps:

1. **Remove Microsoft Store Python Alias**:
   - Open Windows Settings
   - Search for "Manage app execution aliases"
   - Turn OFF "App Installer Python" and "App Installer Python3"

2. **Reinstall Python**:
   - Uninstall any existing Python versions
   - Download Python 3.x from [python.org](https://www.python.org/downloads/)
   - Run installer as Administrator
   - ✅ **IMPORTANT**: Check both boxes:
     - "Add Python to PATH"
     - "Install for all users"
   - Choose "Customize installation"
   - On next screen, keep all options checked
   - On "Advanced Options" screen, check:
     - Install for all users
     - Associate files with Python
     - Add Python to environment variables
     - Customize install location to: `C:\Python3x` (where x is version number)

3. **Verify Installation**:
   - Open a **new** Command Prompt
   - Use this command:

```bash
py --version
```

Note: On Windows, using `py` is the recommended way to run Python.

If still not working, add Python manually to PATH:

1. Search for "Edit system environment variables"
2. Click "Environment Variables"
3. Under "System Variables", find and select "Path"
4. Click "Edit" and "New"
5. Add: `C:\Python3x` and `C:\Python3x\Scripts`
