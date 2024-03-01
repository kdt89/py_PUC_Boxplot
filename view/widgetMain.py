from view.ui.Main_ui import Ui_Main
from PyQt6.QtWidgets import QMainWindow


# class for object Main window of application
class WidgetMain(QMainWindow):

    # message = ""
    # update status bar message
    def updateSttBar(self, message: str):
        self.ui.statusbar.showMessage(message, 1000)
        self.ui.statusbar.repaint()


    def updateMessage(self, message: str):
        self.ui.txtbrowserOperationMessage.append(message)
        self.ui.txtbrowserOperationMessage.repaint()


    def __init__(self):
        super(WidgetMain, self).__init__()
        # GUI Main form
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.ui.btnAbout.clicked.connect(self.ui.actionShowAbout.trigger)
        self.ui.btnMakePlot.clicked.connect(self.ui.actionMakePlot.trigger)
        self.ui.btnPreferences.clicked.connect(self.ui.actionShowPreferences.trigger)