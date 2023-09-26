from PyQt6.QtWidgets import QWidget
from view.ui.UI_About import Ui_About

# GUI About form
class WidgetAbout(QWidget):

    def __init__(self):
        super(WidgetAbout, self).__init__()
        self.ui = Ui_About()
        self.ui.setupUi(self)