from PyQt6.QtWidgets import QLineEdit, QApplication
from PyQt6.QtGui import QValidator
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
import sys

class DigitSpaceValidator(QRegularExpressionValidator):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Regular expression to match digits and spaces
        regex = QRegularExpression("[0-9 ]*")
        self.setRegularExpression(regex)

    def validate(self, input, pos):
        # Use the regular expression validation
        return super().validate(input, pos)

app = QApplication(sys.argv)
lineEdit = QLineEdit()

# Set the custom validator for the line edit
validator = DigitSpaceValidator()
lineEdit.setValidator(validator)

lineEdit.show()
sys.exit(app.exec())
