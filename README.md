# Trackman Automation Helper

## Overview
**Trackman Automation Helper** is a lightweight Windows utility designed to streamline gameplay when using the Trackman golf simulator software.

The tool reduces repetitive manual interaction by allowing the user to advance gameplay (e.g., *Next Shot* / *Next Hole*) using a single keyboard hotkey instead of repeated mouse clicks.

The application runs in the background and listens for a configurable global hotkey. When triggered, it simulates user input (mouse clicks) at predefined screen locations to advance the Trackman UI.

This project is intended for **personal convenience and accessibility**, helping maintain pace of play during practice or casual sessions.

---

## Key Features
- Global hotkey support (works while Trackman is focused)
- Hotkey interception to prevent input from reaching the Trackman app
- Screen-relative mouse positioning (resolution-independent)
- Lightweight, no modification of Trackman software
- Simple and extensible Python codebase

---

## How It Works
1. The application registers a **global keyboard hotkey** at the operating system level.
2. When the hotkey is pressed:
   - The keystroke is intercepted and suppressed (not passed to Trackman).
   - The script calculates a target screen coordinate.
   - A mouse click is programmatically issued at that location.
3. Trackman receives the click exactly as if it came from a real mouse.

The automation operates entirely at the **OS input level** and does not hook into or modify Trackman’s internal logic.

---

## Technologies & Libraries Used

### Python
The core application logic is written in **Python 3**, chosen for its simplicity, readability, and strong automation ecosystem.

### PyAutoGUI
Used for:
- Retrieving screen dimensions
- Moving the mouse
- Simulating mouse clicks

PyAutoGUI enables safe, cross-resolution screen interaction using standard OS input events.

### keyboard
Used for:
- Registering global hotkeys
- Intercepting and suppressing keyboard input
- Triggering automation regardless of which application is active

This allows the script to respond instantly without interfering with Trackman’s normal controls.

### Pillow (PIL)
Used indirectly by PyAutoGUI for:
- Screen capture
- Image handling

### OpenCV (Optional)
Enables:
- Confidence-based image matching
- More robust UI detection if image-based automation is added

---

## Requirements
- Windows 10 or Windows 11
- Python 3.9+
- Trackman software (windowed or borderless mode recommended)

---

## Installation

```bash
pip install pyautogui keyboard pillow opencv-python
