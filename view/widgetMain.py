from view.ui.Main_ui import Ui_Main
from view.rc import icons_rc
from PyQt6.QtWidgets import QMainWindow
from typing import List


class WidgetMain(QMainWindow):

    def __init__(self):
        super(WidgetMain, self).__init__()
        # GUI Main form
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.ui.btn_showAbout.clicked.connect(self.ui.actionShowAbout.trigger)
        self.ui.btn_makePlot.clicked.connect(self.ui.actionMakePlot.trigger)
        self.ui.btn_showPreference.clicked.connect(
            self.ui.actionShowPreference.trigger)
        self.ui.btn_loadDatasetName.clicked.connect(
            self.ui.actionLoadDatasetName.trigger)

    def updateUI_statusbar(self, message: str):
        self.ui.statusbar.showMessage(message, 2000)
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

    def getfromUI_datasetNameList_txtEdit(self) -> List[str]:
        str_list = self.ui.textEdit_datasetNameList.toPlainText()
        str_list = str_list.split()  # split string by \n \r \t \f and spaces
        return str_list
