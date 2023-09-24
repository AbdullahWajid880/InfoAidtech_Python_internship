import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QSpinBox, QLineEdit, QMessageBox

class DiceRollerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Dice Roller App")
        self.setGeometry(100, 100, 400, 250)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.welcome_label = QLabel("Welcome to the Dice Roller App!", self)
        self.layout.addWidget(self.welcome_label)

        self.name_label = QLabel("Enter your name:", self)
        self.layout.addWidget(self.name_label)

        self.name_input = QLineEdit(self)
        self.layout.addWidget(self.name_input)

        self.explanation_label = QLabel("Game Explanation: Click 'Roll Dice' to roll the dice.", self)
        self.layout.addWidget(self.explanation_label)

        self.dice_label = QLabel("Number of Dice:", self)
        self.layout.addWidget(self.dice_label)

        self.dice_input = QSpinBox(self)
        self.dice_input.setMinimum(1)
        self.dice_input.setMaximum(10)
        self.layout.addWidget(self.dice_input)

        self.roll_button = QPushButton("Roll Dice", self)
        self.roll_button.clicked.connect(self.roll_dice)
        self.layout.addWidget(self.roll_button)

        self.quit_button = QPushButton("Quit", self)
        self.quit_button.clicked.connect(self.close)
        self.layout.addWidget(self.quit_button)

        self.central_widget.setLayout(self.layout)

    def roll_dice(self):
        user_name = self.name_input.text()
        if not user_name:
            QMessageBox.critical(self, "Error", "Please enter your name before rolling the dice.")
            return

        num_dice = self.dice_input.value()
        results = [random.randint(1, 6) for _ in range(num_dice)]
        result_text = f"Hello, {user_name}! Result: {', '.join(map(str, results))}"
        self.explanation_label.setText("Game Explanation: Click 'Roll Dice' to roll the dice again.")
        self.show_alert(result_text)

    def show_alert(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Roll Result")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

def main():
    app = QApplication(sys.argv)
    window = DiceRollerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
