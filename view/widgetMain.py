from view.ui.Main_ui import Ui_Main
from PyQt6.QtWidgets import QMainWindow
from typing import List

# Class for object Main window 
class WidgetMain(QMainWindow):

    def __init__(self):
        super(WidgetMain, self).__init__()
        # GUI Main form
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.ui.btn_about.clicked.connect(self.ui.actionShowAbout.trigger)
        self.ui.btn_makePlot.clicked.connect(self.ui.actionMakePlot.trigger)
        self.ui.btn_preferences.clicked.connect(self.ui.actionShowPreferences.trigger)
        self.ui.btn_loadDatasetName.clicked.connect(self.ui.actionLoadDatasetName.trigger)
    # message = ""
    # update status bar message
        
    def updateUI_statusbar(self, message: str):
        self.ui.statusbar.showMessage(message, 1000)
        self.ui.statusbar.repaint()


    def updateUI_messagebox(self, message: str):
        self.ui.txtbrowser_operationMessage.append(message)
        self.ui.txtbrowser_operationMessage.repaint()


    def updateUI_datasetNameList_txtEdit(self, string_list) -> None:
        if not isinstance(string_list, List):
            return
        
        text = str('\n'.join(string_list))
        self.ui.textEdit_datasetNameList.clear()
        self.ui.textEdit_datasetNameList.setText(text)
        # self.ui.textEdit_datasetNameList.repaint()


    def getfromUI_datasetNameList_txtEdit(self) -> List[str]:
        str_list = self.ui.textEdit_datasetNameList.toPlainText()
        str_list = str_list.split() # split string by \n \r \t \f and spaces
        return str_list
