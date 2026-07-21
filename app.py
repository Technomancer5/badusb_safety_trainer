"""
BadUSB Safety Trainer

A local defensive cybersecurity training app for learning about
USB keystroke-injection risks using safe, harmless templates only.

This project is designed for authorized lab learning and does not include
payloads that steal data, bypass security, download code, or modify systems.
"""

import json
import re
import zipfile
from datetime import datetime
from io import BytesIO
from pathlib import Path
from urllib.parse import urlparse

from flask import Flask, render_template, request, send_file


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
EXPORT_DIR = BASE_DIR / "exports" / "generated_payloads"

TEMPLATE_DATA_FILE = DATA_DIR / "templates.json"
LAB_NOTES_FILE = DATA_DIR / "lab_notes.json"
SECURITY_CHECKLIST_FILE = DATA_DIR / "security_checklist.json"

app = Flask(__name__)


def load_training_templates():
    """
    Load safe training templates from the local JSON data file.

    This keeps template content separate from the Flask routes so the app can
    grow without hard-coding every template directly in Python.
    """
    if not TEMPLATE_DATA_FILE.exists():
        return []

    with TEMPLATE_DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_lab_notes():
    """
    Load saved lab notes from the local JSON data file.

    If the file does not exist or is empty, the app returns an empty list so
    the lab notes page can still load safely.
    """
    if not LAB_NOTES_FILE.exists():
        return []

    try:
        with LAB_NOTES_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_lab_notes(notes):
    """
    Save the full lab notes list back to the JSON data file.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with LAB_NOTES_FILE.open("w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4)

def load_security_checklist():
    """
    Load the USB security checklist from the local JSON data file.

    The checklist supports defensive security planning by tracking habits and
    controls that reduce BadUSB-style risk.
    """
    if not SECURITY_CHECKLIST_FILE.exists():
        return []

    try:
        with SECURITY_CHECKLIST_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_security_checklist(checklist_items):
    """
    Save the USB security checklist back to the JSON data file.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with SECURITY_CHECKLIST_FILE.open("w", encoding="utf-8") as file:
        json.dump(checklist_items, file, indent=4)


def calculate_checklist_summary(checklist_items):
    """
    Count checklist item statuses for the readiness summary.
    """
    summary = {
        "Complete": 0,
        "Needs Review": 0,
        "Not Started": 0,
    }

    for item in checklist_items:
        status = item.get("status", "Needs Review")

        if status not in summary:
            summary[status] = 0

        summary[status] += 1

    return summary

def find_template_by_id(template_id):
    """
    Find one template from the template library by its unique ID.
    """
    templates = load_training_templates()

    for template in templates:
        if template["id"] == template_id:
            return template

    return None


def is_safe_url(url):
    """
    Validate that a URL uses a normal web scheme.

    This project only allows http and https links for safe demonstration.
    It blocks file paths, shell-style input, javascript URLs, and other schemes.
    """
    parsed_url = urlparse(url)

    if parsed_url.scheme not in ["http", "https"]:
        return False

    if not parsed_url.netloc:
        return False

    return True


def sanitize_delay(delay_value):
    """
    Convert the delay value into a safe integer.

    Delay is limited so the generated script remains simple and predictable.
    """
    try:
        delay = int(delay_value)
    except ValueError:
        return 1000

    if delay < 250:
        return 250

    if delay > 5000:
        return 5000

    return delay

def get_selected_operating_systems(form_data):
    """
    Read selected operating systems from the builder form.

    The builder can generate one script, or multiple scripts, depending on
    which OS checkboxes the user selects.
    """
    allowed_systems = ["windows", "linux", "macos"]
    selected_systems = []

    for operating_system in allowed_systems:
        if form_data.get(f"os_{operating_system}") == "on":
            selected_systems.append(operating_system)

    return selected_systems


def format_os_name(target_os):
    """
    Convert internal OS names into user-friendly labels.
    """
    labels = {
        "windows": "Windows",
        "linux": "Linux",
        "macos": "macOS",
    }

    return labels.get(target_os, target_os)

def contains_blocked_terms(user_text):
    """
    Block clearly unsafe terms from user-provided text.

    This is not a complete security system, but it helps keep the training
    project aligned with its defensive-only purpose.
    """
    blocked_terms = [
        "password",
        "credential",
        "token",
        "secret",
        "download",
        "invoke-webrequest",
        "curl",
        "wget",
        "powershell",
        "cmd",
        "bash",
        "sudo",
        "rm -rf",
        "net user",
        "registry",
        "exfiltrate",
        "payload",
        "reverse shell",
        "keylogger",
    ]

    normalized_text = user_text.lower()

    for term in blocked_terms:
        if term in normalized_text:
            return True

    return False


def generate_usb_awareness_message(message, delay_ms):
    """
    Generate a harmless script that types a training message.

    This template assumes the user has opened a text editor on an authorized
    lab computer before running the script.
    """
    return f"""REM BadUSB Safety Trainer - USB Awareness Message
REM Authorized lab use only.
REM This script only types a harmless training message.
DELAY {delay_ms}
STRING {message}
ENTER
"""


def generate_portfolio_url_demo(url, delay_ms, target_os):
    """
    Generate a harmless script that opens a safe website URL.

    Because keyboard shortcuts are different across operating systems, this
    function creates OS-specific versions instead of pretending one script
    works everywhere.
    """
    if target_os == "windows":
        return f"""REM BadUSB Safety Trainer - Portfolio URL Demo - Windows
REM Authorized lab use only.
REM Opens a safe http/https URL using the Windows Run dialog.
DELAY {delay_ms}
GUI r
DELAY 500
STRING {url}
ENTER
"""

    if target_os == "linux":
        return f"""REM BadUSB Safety Trainer - Portfolio URL Demo - Linux
        REM Authorized lab use only.
        REM Opens a safe http/https URL using a Linux desktop launcher.
        DELAY {delay_ms}
        ALT F2
        DELAY 1500
        STRING xdg-open {url}
        DELAY 300
        ENTER
        """

    if target_os == "macos":
        return f"""REM BadUSB Safety Trainer - Portfolio URL Demo - macOS
REM Authorized lab use only.
REM Opens a safe http/https URL using Spotlight.
DELAY {delay_ms}
GUI SPACE
DELAY 700
STRING {url}
ENTER
"""

    return ""

def generate_custom_safety_demo(message, url, delay_ms, target_os):
    """
    Generate a custom harmless script using a message, a URL, or both.

    URL-opening behavior is generated differently for each selected operating
    system because shortcuts are not universal.
    """
    script_lines = [
        f"REM BadUSB Safety Trainer - Custom Safety Demo - {target_os.title()}",
        "REM Authorized lab use only.",
        "REM This script only performs simple harmless demonstration actions.",
        f"DELAY {delay_ms}",
    ]

    if message:
        script_lines.append(f"STRING {message}")
        script_lines.append("ENTER")

    if url:
        if target_os == "windows":
            script_lines.extend([
                "GUI r",
                "DELAY 500",
                f"STRING {url}",
                "ENTER",
            ])

        elif target_os == "linux":
            script_lines.extend([
                "ALT F2",
                "DELAY 700",
                f"STRING xdg-open {url}",
                "ENTER",
            ])

        elif target_os == "macos":
            script_lines.extend([
                "GUI SPACE",
                "DELAY 700",
                f"STRING {url}",
                "ENTER",
            ])

    return "\n".join(script_lines) + "\n"

def build_safe_script(template_id, form_data):
    """
    Build one or more safe training scripts from the selected template.

    The function returns a tuple:
    - dictionary of generated scripts
    - list of validation errors

    The dictionary format is:
    {
        "Windows": "script text",
        "Linux": "script text"
    }
    """
    errors = []
    generated_scripts = {}
    delay_ms = sanitize_delay(form_data.get("delay_ms", "1000"))

    if template_id == "usb_awareness_message":
        message = form_data.get("message", "").strip()

        if not message:
            errors.append("Training message is required.")

        if len(message) > 120:
            errors.append("Training message must be 120 characters or fewer.")

        if contains_blocked_terms(message):
            errors.append("Training message contains blocked unsafe terms.")

        if errors:
            return {}, errors

        generated_scripts["Generic"] = generate_usb_awareness_message(message, delay_ms)
        return generated_scripts, errors

    if template_id == "portfolio_url_demo":
        url = form_data.get("url", "").strip()
        selected_systems = get_selected_operating_systems(form_data)

        if not url:
            errors.append("URL is required.")

        if contains_blocked_terms(url):
            errors.append("URL contains blocked unsafe terms.")

        if url and not is_safe_url(url):
            errors.append("Only valid http or https URLs are allowed.")

        if not selected_systems:
            errors.append("Select at least one operating system.")

        if errors:
            return {}, errors

        for target_os in selected_systems:
            os_label = format_os_name(target_os)
            generated_scripts[os_label] = generate_portfolio_url_demo(url, delay_ms, target_os)

        return generated_scripts, errors

    if template_id == "custom_safety_demo":
        message = form_data.get("message", "").strip()
        url = form_data.get("url", "").strip()
        selected_systems = get_selected_operating_systems(form_data)

        if not message and not url:
            errors.append("Custom Safety Demo requires a message, a URL, or both.")

        if len(message) > 120:
            errors.append("Training message must be 120 characters or fewer.")

        if message and contains_blocked_terms(message):
            errors.append("Training message contains blocked unsafe terms.")

        if url and contains_blocked_terms(url):
            errors.append("URL contains blocked unsafe terms.")

        if url and not is_safe_url(url):
            errors.append("Only valid http or https URLs are allowed.")

        if url and not selected_systems:
            errors.append("Select at least one operating system when using a URL.")

        if errors:
            return {}, errors

        if url:
            for target_os in selected_systems:
                os_label = format_os_name(target_os)
                generated_scripts[os_label] = generate_custom_safety_demo(
                    message,
                    url,
                    delay_ms,
                    target_os,
                )
        else:
            generated_scripts["Generic"] = generate_custom_safety_demo(
                message,
                "",
                delay_ms,
                "generic",
            )

        return generated_scripts, errors

    errors.append(f"Unknown template selected: {template_id}")
    return {}, errors


def export_acknowledgements_are_checked(form_data):
    """
    Confirm that the user checked every safety acknowledgement before export.

    This reinforces that scripts should only be used in authorized lab settings.
    """
    required_checks = [
        "authorized_device",
        "no_data_collection",
        "no_security_changes",
        "no_external_code",
        "controlled_lab",
    ]

    for check_name in required_checks:
        if form_data.get(check_name) != "on":
            return False

    return True


def make_safe_filename(template_id):
    """
    Create a safe export filename using the template ID and a timestamp.

    The filename is cleaned to avoid path traversal or unusual characters.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    cleaned_template_id = re.sub(r"[^a-zA-Z0-9_-]", "", template_id)

    if not cleaned_template_id:
        cleaned_template_id = "training_script"

    return f"{cleaned_template_id}_{timestamp}.txt"


def save_exported_scripts(template_id, generated_scripts):
    """
    Save generated scripts to a zip file.

    If the user selects multiple operating systems, each OS receives its own
    .txt file inside the zip archive.
    """
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    cleaned_template_id = re.sub(r"[^a-zA-Z0-9_-]", "", template_id)

    if not cleaned_template_id:
        cleaned_template_id = "training_script"

    zip_filename = f"{cleaned_template_id}_{timestamp}.zip"
    zip_path = EXPORT_DIR / zip_filename

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for os_label, script_text in generated_scripts.items():
            safe_os_label = re.sub(r"[^a-zA-Z0-9_-]", "", os_label.lower())
            script_filename = f"{cleaned_template_id}_{safe_os_label}_{timestamp}.txt"
            zip_file.writestr(script_filename, script_text)

    return zip_path


def create_lab_note(template, form_data, export_path):
    """
    Create one lab note record for an exported training script.

    The lab note documents the educational purpose of the script and supports
    professional security documentation habits.
    """
    purpose = form_data.get("training_purpose", "").strip()
    target_environment = form_data.get("target_environment", "").strip()
    notes = form_data.get("lab_notes", "").strip()

    if not purpose:
        purpose = "Defensive BadUSB awareness training"

    if not target_environment:
        target_environment = "Authorized local lab device"

    return {
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "template_id": template["id"],
        "template_name": template["name"],
        "risk_level": template["risk_level"],
        "defensive_lesson": template["defensive_lesson"],
        "training_purpose": purpose,
        "target_environment": target_environment,
        "notes": notes,
        "selected_operating_systems": ", ".join(
            format_os_name(os_name) for os_name in get_selected_operating_systems(form_data)
        ) or "Generic", 
        "exported_filename": export_path.name,
    }


def record_lab_note(template, form_data, export_path):
    """
    Add one new lab note to the saved lab notes JSON file.
    """
    notes = load_lab_notes()
    new_note = create_lab_note(template, form_data, export_path)

    notes.insert(0, new_note)
    save_lab_notes(notes)


@app.route("/")
def index():
    """
    Display the project dashboard.
    """
    project_info = {
        "name": "BadUSB Safety Trainer",
        "purpose": "Create and document safe BadUSB awareness demos for authorized lab use.",
        "status": "Local development version",
        "safety_focus": [
            "Authorized devices only",
            "Harmless training templates",
            "Preview before export",
            "No credential collection",
            "No download-and-execute behavior",
            "No persistence or stealth behavior",
        ],
    }

    return render_template("index.html", project=project_info)


@app.route("/templates")
def template_library():
    """
    Display the safe training template library.
    """
    templates = load_training_templates()
    return render_template("library.html", templates=templates)


@app.route("/builder", methods=["GET", "POST"])
def builder():
    """
    Display the safe script builder, preview scripts, and export safe scripts.

    The generated script is not automatically executed. The user must review
    it first, which supports safe security training habits.
    """
    templates = load_training_templates()
    selected_template = None
    generated_scripts = {}
    errors = []
    form_values = {}

    if request.method == "POST":
        form_values = request.form
        template_id = request.form.get("template_id", "")
        action = request.form.get("action", "preview")

        selected_template = find_template_by_id(template_id)
        generated_scripts, errors = build_safe_script(template_id, request.form)

        if action == "export":
            if not export_acknowledgements_are_checked(request.form):
                errors.append("All safety acknowledgements must be checked before export.")

            if not selected_template:
                errors.append("A valid template must be selected before export.")

            if not errors and generated_scripts and selected_template:
                export_path = save_exported_scripts(template_id, generated_scripts)
                record_lab_note(selected_template, request.form, export_path)
            
                return send_file(
                    export_path,
                    as_attachment=True,
                    download_name=export_path.name,
                    mimetype="application/zip",
                )

    return render_template(
        "builder.html",
        templates=templates,
        selected_template=selected_template,
        generated_scripts=generated_scripts,
        errors=errors,
        form_values=form_values,
    )


@app.route("/lab-notes")
def lab_notes():
    """
    Display saved lab notes and export history.

    This gives the project a documentation component, which is valuable for
    cybersecurity training and professional reflection.
    """
    notes = load_lab_notes()
    return render_template("lab_notes.html", notes=notes)

@app.route("/usb-checklist", methods=["GET", "POST"])
def usb_checklist():
    """
    Display and update the USB security checklist.

    This page connects the BadUSB training project to practical defensive
    controls for workstations, home labs, and future server administration.
    """
    checklist_items = load_security_checklist()

    if request.method == "POST":
        for item in checklist_items:
            item_id = item["id"]

            status_field = f"status_{item_id}"
            notes_field = f"notes_{item_id}"

            item["status"] = request.form.get(status_field, item["status"])
            item["notes"] = request.form.get(notes_field, "").strip()

        save_security_checklist(checklist_items)

    summary = calculate_checklist_summary(checklist_items)

    return render_template(
        "usb_checklist.html",
        checklist_items=checklist_items,
        summary=summary,
    )

if __name__ == "__main__":
    app.run(debug=True)