# Micreader
This repository contains a Python application that converts speech to text using the Google Speech Recognition API

**Important** You need to have python already install on your device
can be run using console command or VScode or other compiler

---

# Speech-to-Text Application with Browser Interaction

This repository contains a Python application that converts speech to text using the Google Speech Recognition API and interacts with a web browser to perform actions based on the recognized text. The application is built using PyQt5 for the graphical user interface and integrates with various libraries for speech recognition, clipboard manipulation, keyboard event handling, and browser automation.

## Features
- **Speech Recognition**: Utilizes the `speech_recognition` library to transcribe spoken words into text in real-time.
- **Clipboard Integration**: Copies the recognized text to the clipboard for easy pasting into other applications.
- **Keyboard Event Handling**: Listens for keyboard shortcuts (`Ctrl+Alt+S`) to initiate the speech recognition process.
- **GUI**: Provides a simple graphical user interface built with PyQt5 for user interaction.
- **Browser Interaction**: Interacts with a web browser to perform actions based on the recognized text, such as navigating to a specific webpage and simulating keyboard input.
- **Configurable Options**: Offers options to customize the behavior of the application, such as copying the recognized text to the clipboard and pasting it into the active application.

## Requirements
- Python 3.x
- PyQt5
- SpeechRecognition
- pyperclip
- keyboard
- pyautogui

## Usage
1. Install the required libraries using pip: `pip install -r requirements.txt`.
2. Download and install the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome).
3. Run the application by executing the `speech_to_text_app.py` file.
4. Press `Ctrl+Alt+S` to initiate speech recognition and interact with the application.

## License
This project is licensed under the [MIT License](LICENSE).

---

Feel free to adjust the description as needed for your GitHub repository.
