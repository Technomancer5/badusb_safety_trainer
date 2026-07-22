# Overview

I created the BadUSB Safety Trainer as a tool for cybersecurity awareness to show family and freinds or any future clients of mine. I wanted to build something that was practical, educational, and a cybersecurity tool to create awareness of our vulnerabilities.

My purpose for writing this software was to create a safe learning tool that demonstrates why unknown USB devices can be risky without creating harmful payloads. This project focuses on defensive education only. It does not generate scripts for credential theft, data collection, persistence, stealth, disabling security tools, or destructive behavior. Instead, it helps users understand how quickly an unlocked workstation can be interacted with by a keyboard-emulating USB device and why habits like locking workstations, using trusted USB devices, and documenting authorized testing matter.

[Bad USB Safety Trainer demo](https://youtu.be/P_eo_I-fg1M)

# Development Environment

I developed this project locally using VS Code on a Linux system. The application runs as a local Flask web app and is accessed through a browser using `http://127.0.0.1:5000`.

The main programming language I used was Python. I used Flask to handle routing, page rendering, form submission, validation, script generation, exporting files, and loading local JSON data. I also used HTML for page structure, CSS for styling, JavaScript for dynamic builder form behavior, and JSON for simple local data storage.
Javascript, JSON, pathlib, zipfile, datetime and urllib.parse

# Useful Websites

- [Flipper Zero BadUSB Documentation](https://docs.flipper.net/zero/bad-usb)
- [qFlipper Documentation](https://docs.flipper.net/qflipper)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python pathlib Documentation](https://docs.python.org/3/library/pathlib.html)
- [Python json Documentation](https://docs.python.org/3/library/json.html)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}


- Add more safe training templates for additional defensive awareness scenarios.
- Improve operating system support by adding more desktop environment options, such as KDE, GNOME, Windows, and macOS-specific variations.
- Add clearer template categories such as beginner, intermediate, awareness, and defensive checklist.
