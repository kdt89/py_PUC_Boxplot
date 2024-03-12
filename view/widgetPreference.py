from PyQt6.QtWidgets import QWidget
from view.ui.Preference_ui import Ui_Preference
from typing import List


class WidgetPreference(QWidget):

    def __init__(self):
        super(WidgetPreference, self).__init__()
        self.ui = Ui_Preference()
        self.ui.setupUi(self)
        self.setLayout(self.ui.vLayout_main)
        self.ui.btnSave.clicked.connect(self.ui.actionSavePreference.trigger)


    def getUI_preference(self):
        dataset_label_rotation = int(self.ui.comboBox_datasetLabelRotation.currentText())
        show_median = self.ui.comboBox_plotConfigShowMedianVal.currentText()
        if 'Yes' == show_median:
            show_median = True
        else:
            show_median = False
        number_row_skip = int(self.ui.lineEdit_dataConfigImportSkipRow.text())

        return dataset_label_rotation, show_median, number_row_skip


    def setUI_preference(
        self,
        dataset_label_rotation: int,
        show_median: bool,
        number_row_skip: List[int]
    ) -> None:
        if type(dataset_label_rotation) != int:
            dataset_label_rotation = 0
        else:
            if not dataset_label_rotation in [0, 45, 90]:
                dataset_label_rotation = 0

        if number_row_skip != None:
            number_row_skip = [num for num in number_row_skip if type(num) == int]
            number_row_skip = [num for num in number_row_skip if num > 0]
            if len(number_row_skip) == 0:
                number_row_skip = None

        try:
            self.ui.comboBox_datasetLabelRotation.setCurrentText(str(dataset_label_rotation))
        except:
            self.ui.comboBox_datasetLabelRotation.setCurrentIndex(0)

        if show_median:
            self.ui.comboBox_plotConfigShowMedianVal.setCurrentText('Yes')
        else:
            self.ui.comboBox_plotConfigShowMedianVal.setCurrentText('No')

        if number_row_skip == None:
            self.ui.lineEdit_dataConfigImportSkipRow.setText('None')
        else:
            self.ui.lineEdit_dataConfigImportSkipRow.setText(' '.join(map(int, number_row_skip)))

        return None