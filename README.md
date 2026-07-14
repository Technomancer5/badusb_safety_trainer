# BadUSB Safety Trainer

## Overview

BadUSB Safety Trainer is a local defensive cybersecurity training web application that helps users understand USB keystroke-injection risks using safe, harmless, authorized training templates.

The project is designed for cybersecurity awareness training. It allows the user to review safe template descriptions, generate a harmless training script preview, export a Flipper Zero-compatible `.txt` file, document the purpose of the lab, and track USB-related defensive controls.

This project does not include offensive payloads. It does not generate scripts for credential theft, data exfiltration, persistence, stealth, downloading external code, disabling security tools, bypassing authentication, or modifying system security settings.

The goal of this project is to demonstrate how quickly an unknown USB device can interact with an unlocked computer and to reinforce defensive habits such as locking workstations, using only trusted USB devices, limiting privileges, and documenting authorized security training.

[Software Demo Video](VIDEO_LINK_HERE)

## Development Environment

This project was created and tested locally in VS Code on Linux.

Tools and technologies used:

- Python
- Flask
- HTML
- CSS
- JavaScript
- JSON
- VS Code
- Localhost development server
- Flipper Zero-compatible `.txt` export format

## Useful Websites

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python pathlib Documentation](https://docs.python.org/3/library/pathlib.html)
- [Python json Documentation](https://docs.python.org/3/library/json.html)
- [Flipper Zero BadUSB Documentation](https://docs.flipper.net/zero/bad-usb)
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)

## Features

Current project features include:

- Local Flask web application
- Defensive cybersecurity landing page
- Safe BadUSB training template library
- Safe script builder
- Script preview before export
- Required safety acknowledgements before export
- Flipper-compatible `.txt` export
- Lab notes and export history
- USB security checklist
- Readiness summary for defensive USB controls
- JSON-based local data storage

## Project Safety Policy

This project is for defensive security education and authorized lab demonstrations only.

Allowed use:

- Use only on devices I own or have explicit permission to test.
- Use safe templates that demonstrate keystroke automation without harm.
- Preview every generated script before exporting it.
- Document the purpose and result of each lab.
- Use the project to teach defensive USB security awareness.

Disallowed use:

- Credential theft
- Data exfiltration
- Downloading and executing external code
- Persistence
- Stealth behavior
- Disabling security tools
- Bypassing authentication
- Modifying system security settings
- Running destructive commands

## How to Run the Project

Clone or download the project, then open the project folder:

```bash
cd badusb_safety_trainer
```

## First-Time Setup for Fish Shell

Use this section if your terminal uses **fish shell**, which is common on some Linux systems and customized terminals.

Create a virtual environment:

```fish
python -m venv .venv
```

Activate the virtual environment:

```fish
source .venv/bin/activate.fish
```

Install the project dependencies:

```fish
python -m pip install -r requirements.txt
```

Run the application:

```fish
python app.py
```

Open the local website in a browser:

```text
http://127.0.0.1:5000
```

After the first setup, future runs with fish shell usually only require:

```fish
cd badusb_safety_trainer
source .venv/bin/activate.fish
python app.py
```

## First-Time Setup for Bash or Zsh

Use this section if your terminal uses **bash or zsh**, which are common default shells on many Linux and macOS systems.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open the local website in a browser:

```text
http://127.0.0.1:5000
```

After the first setup, future runs with bash or zsh usually only require:

```bash
cd badusb_safety_trainer
source .venv/bin/activate
python app.py
```

