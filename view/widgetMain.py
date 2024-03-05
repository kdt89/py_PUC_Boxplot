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
        self.ui.txtbrowser_operationMessage.append(message)
        self.ui.txtbrowser_operationMessage.repaint()


    def __init__(self):
        super(WidgetMain, self).__init__()
        # GUI Main form
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.ui.btn_about.clicked.connect(self.ui.actionShowAbout.trigger)
        self.ui.btn_makePlot.clicked.connect(self.ui.actionMakePlot.trigger)
        self.ui.btn_preferences.clicked.connect(self.ui.actionShowPreferences.trigger)