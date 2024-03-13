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
        # get value from QCombobox, value is selected in list 0, 45, 90
        dataset_label_rotation = int(self.ui.comboBox_datasetLabelRotation.currentText())

        # get value from QComboBox
        show_median = self.ui.comboBox_plotConfigShowMedianVal.currentText()
        if 'Yes' == show_median:
            show_median = True
        elif 'No' == show_median:
            show_median = False
        else:
            show_median = False

        # get value from QLineEdit
        skiprows = self.ui.lineEdit_dataConfigImportSkipRows.text()
        if skiprows == 'None':
            skiprows = None
        else:
            skiprows = skiprows.split(' ')
            skiprows = [int(num) for num in skiprows if num.isnumeric()] # Filter out non-numeric string
            skiprows = [row for row in skiprows if row >= 0]
            if len(skiprows) == 0:
                skiprows = None

        return dataset_label_rotation, show_median, skiprows


    def setUI_preference(
        self,
        dataset_label_rotation: int,
        show_median: bool,
        rowskip: List[int]
    ) -> None:
        if type(dataset_label_rotation) != int:
            dataset_label_rotation = 0
        else:
            if not dataset_label_rotation in [0, 45, 90]:
                dataset_label_rotation = 0

        if rowskip != None:
            rowskip = [num for num in rowskip if type(num) == int]
            rowskip = [num for num in rowskip if num >= 0]
            if len(rowskip) == 0:
                rowskip = None

        try:
            self.ui.comboBox_datasetLabelRotation.setCurrentText(str(dataset_label_rotation))
        except:
            self.ui.comboBox_datasetLabelRotation.setCurrentIndex(0)

        if show_median:
            self.ui.comboBox_plotConfigShowMedianVal.setCurrentText('Yes')
        else:
            self.ui.comboBox_plotConfigShowMedianVal.setCurrentText('No')

        if rowskip == None:
            self.ui.lineEdit_dataConfigImportSkipRows.setText('None')
        else:
            self.ui.lineEdit_dataConfigImportSkipRows.setText(' '.join(map(str, rowskip)))

        return None