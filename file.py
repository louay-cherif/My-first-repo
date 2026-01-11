import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout
)


class SimpleToolUI(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        self.setFixedSize(480, 280)

        self.heading = QLabel("Heading")
        self.heading.setStyleSheet("font-size:18px; font-weight:bold;")

        self.description = QLabel("Description")
        self.description.setWordWrap(True)

        self.input_label = QLabel("Input:")
        self.input_box = QLineEdit()

        self.button = QPushButton("Run")

        self.output = QLabel("")
        self.output.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(self.heading)
        layout.addWidget(self.description)
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_box)
        layout.addWidget(self.button)
        layout.addWidget(self.output)

        self.setLayout(layout)

    # --- setters (ONLY UI responsibility) ---
    def set_title(self, text): self.setWindowTitle(text)
    def set_heading(self, text): self.heading.setText(text)
    def set_description(self, text): self.description.setText(text)
    def set_input_label(self, text): self.input_label.setText(text)
    def set_placeholder(self, text): self.input_box.setPlaceholderText(text)
    def set_button_text(self, text): self.button.setText(text)
    def set_output(self, text): self.output.setText(text)


# 🔥 ONE-LINER APP RUNNER (NO BOILERPLATE ELSEWHERE)
def run(ui_builder):
    app = QApplication(sys.argv)
    ui = SimpleToolUI()
    ui_builder(ui)      # user customizes + connects logic here
    ui.show()
    sys.exit(app.exec_())
