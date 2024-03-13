import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QFrame, QCheckBox
from PyQt5.QtCore import Qt, pyqtSignal, QObject
import speech_recognition as sr
import pyperclip
import keyboard
import pyautogui
# import time

class KeyboardListener(QObject):
    shortcut_triggered = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_keyboard_listener()

    def init_keyboard_listener(self):
        keyboard.add_hotkey('ctrl+alt+s', self.handle_shortcut)

    def handle_shortcut(self):
        self.shortcut_triggered.emit()

class SpeechToTextApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.button_option = QPushButton("Options")
        self.button_record = QPushButton("Start Recording")
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.options_frame = QFrame()
        self.options_frame.hide()

        self.checkbox_a = QCheckBox("Copy Text Said")
        self.checkbox_b = QCheckBox("Paste Text Said\n(Need above option to be checked\nto work well)")
        self.checkbox_c = QCheckBox("Stay On Top")

        self.checkbox_a.setChecked(True)
        self.checkbox_b.setChecked(True)
        self.checkbox_c.setChecked(True)

        options_layout = QVBoxLayout()
        options_layout.addWidget(self.checkbox_a)
        options_layout.addWidget(self.checkbox_b)
        options_layout.addWidget(self.checkbox_c)
        self.options_frame.setLayout(options_layout)

        layout = QVBoxLayout()
        layout.addWidget(self.button_option)
        layout.addWidget(self.options_frame)
        layout.addWidget(self.button_record)
        layout.addWidget(self.text_edit)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Speech to Text App')

        self.keyboard_listener = KeyboardListener()
        self.keyboard_listener.shortcut_triggered.connect(self.start_recognition)

        self.button_option.clicked.connect(self.toggle_options)
        self.checkbox_c.stateChanged.connect(self.update_window_flags)

    def toggle_options(self):
        self.options_frame.setVisible(not self.options_frame.isVisible())

    def update_window_flags(self):
        if self.checkbox_c.isChecked():
            self.setWindowFlags(
                Qt.Window |
                Qt.CustomizeWindowHint |
                Qt.WindowTitleHint |
                Qt.WindowCloseButtonHint |
                Qt.WindowStaysOnTopHint
            )
        else:
            self.setWindowFlags(
                Qt.Window |
                Qt.CustomizeWindowHint |
                Qt.WindowTitleHint |
                Qt.WindowCloseButtonHint
            )
        self.show()

    def start_recognition(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.text_edit.setText("Recording!")
            self.button_record.setEnabled(False)
            QApplication.processEvents()
            audio = recognizer.listen(source)
            self.button_record.setEnabled(True)

        try:
            text = recognizer.recognize_google(audio, language="id-ID")
            self.text_edit.setText(text)

            if self.checkbox_a.isChecked():
                pyperclip.copy(text)

            if self.checkbox_b.isChecked():
                pyautogui.hotkey("ctrl", "v")
                pyautogui.press("enter")

        except sr.UnknownValueError:
            self.text_edit.setText("Could not understand audio")
        except Exception as e:
            print(f"Exception occurred: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpeechToTextApp()
    window.update_window_flags()
    window.show()
    sys.exit(app.exec_())
