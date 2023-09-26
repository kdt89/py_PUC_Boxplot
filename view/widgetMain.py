from view.ui.UI_Main import Ui_Main
from PyQt6.QtWidgets import QMainWindow


# class for object Main window of application
class WidgetMain(QMainWindow):

    message = ""

    # update status bar message
    def updateSttBar(self, message: str):
        self.ui.statusbar.showMessage(message, 1000)
        self.ui.statusbar.repaint()


    def updateMessage(self, message: str):
        self.ui.txtbrowserMessage.append(message)
        self.ui.txtbrowserMessage.repaint()


    def __init__(self):
        super(WidgetMain, self).__init__()
        # GUI Main form
        self.ui = Ui_Main()
        self.ui.setupUi(self)