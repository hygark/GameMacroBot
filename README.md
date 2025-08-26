# GameMacroBot

## Features:

Aimbot: Detects targets on the screen (e.g., enemies in red) using OpenCV and simulates clicks with PyAutoGUI.
Auto-Click: Performs automatic clicks for farming (e.g., collecting resources).
Auto-Farm: Simulates repetitive movements (WASD + jump) for task automation.
Movement Macros: Executes actions such as quick jumps or speed boost.
Configuration GUI: Tkinter interface to adjust FOV, delay, and enable/disable features.
Optional Logging: Sends logs to a webhook (e.g., Discord) for monitoring.
Safety Limits: Includes failsafe (move mouse to top-left corner) and robust error handling.

## Requirements:

Python: Version 3.9+ (standard in 2021, download at python.org).
Dependencies: Install via pip:

* pyautogui: For mouse/keyboard simulation.
* opencv-python: For screen detection.
* requests: For logging via webhook.
* tkinter: Native in Python for GUI.
  Environment Setup: An emulator such as BlueStacks running Roblox or Free Fire.
  Libraries: Run `pip install pyautogui opencv-python requests` in the script directory.

## Installation:

Create a Repository on GitHub (optional for version control):

* Go to github.com and create a new repository called "GameMacroBot".
* Clone the repo to your PC: `git clone https://github.com/hygark/GameMacroBot.git`.

Add the Script:

* Copy the content of GameMacroBot.py into a Python file in your directory.

Install Dependencies:

* In terminal: `pip install pyautogui opencv-python requests`.

## Configuration in Python:

Open the script and edit the Settings table:

* FOV: Field of view for aimbot (default: 100 pixels).
* ClickDelay: Delay between clicks (default: 0.1 seconds).
* TargetColorLower/Upper: HSV range for target detection (default: red).
* AutoClickKey: Key to toggle auto-click (default: 'x').
* AutoFarmKey: Key to toggle auto-farm (default: 'z').
* MoveMacroKey: Key for movement macros (default: 'c').
* LogWebhook: URL of a Discord webhook (create in Discord > Server Settings > Integrations).
* ScreenshotPath: Folder for screenshots (default: './screenshots/').
* DetectionThreshold: Minimum area for targets (default: 1000).

## How to Make It Work?:

Adjust the Settings:

* Edit Settings to match the game/emulator (e.g., color range for enemies).

Run the Script:

* In terminal: `python GameMacroBot.py`.
* A Tkinter window will open for configuration. Use buttons to start/stop the bot, enable auto-click/farm, or execute macros.

Test:

* Open Roblox or Free Fire in an emulator.
* Adjust the color range to detect targets (e.g., enemies in Free Fire).
* Use keys (x, z, c) or the GUI to activate features.
* Monitor console, webhook, or GUI for logs (e.g., "Target detected and clicked at (x, y)").

Stop the Script:

* Move the mouse to the top-left corner (failsafe) or click "Stop Bot" in the GUI.

## Usage Examples:

Test in Free Fire: Configure the color range to detect enemies (red). The aimbot will automatically click on targets, while auto-farm simulates movements for collecting.
Test in Roblox: Use auto-click for farming in games like "Pet Simulator" or auto-farm for repetitive movements in "Blox Fruits".
Advanced Logging: Set up a Discord webhook to receive real-time notifications.
Expansion: Add detection of specific objects (e.g., resources in Roblox) with OpenCV templates.

## Legal and Ethical Disclaimer:

This script is for educational purposes and private testing only. Do not use in public games or for cheating, as it may result in bans ().
Always respect the Terms of Service of Roblox and Free Fire ().
For pentest or ethical automation, adapt it to legal scenarios.

## Contributions:

Feel free to fork the repository on GitHub and contribute improvements, such as support for more games or advanced image detection.
