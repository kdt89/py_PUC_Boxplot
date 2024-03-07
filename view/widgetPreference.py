
from PyQt6.QtWidgets import QWidget
from view.ui.Preference_ui import Ui_Preference


class WidgetPreference(QWidget):

    def __init__(self):
        super(WidgetPreference, self).__init__()
        self.ui = Ui_Preference()
        self.ui.setupUi(self)
        self.setLayout(self.ui.vLayout_main)
        self.bindingSignal2Slot()


    # binding Action to function
    def bindingSignal2Slot(self) -> None:
        self.ui.btnSave.clicked.connect(self.ui.actionSaveAndClose.trigger)
        self.ui.btnSave.clicked.connect(self.close)