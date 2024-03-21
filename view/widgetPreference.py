from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from view.ui.Preference_ui import Ui_Preference
from typing import List


class WidgetPreference(QWidget):

    def __init__(self):
        super(WidgetPreference, self).__init__()
        self.ui = Ui_Preference()
        self.ui.setupUi(self)

        # Set the custom validator for the line edit
        digit_space_validator = DigitSpaceValidator()
        self.ui.lineEdit_dataConfigImportSkipRows.setValidator(
            digit_space_validator)

        self.setLayout(self.ui.vLayout_main)
        self.ui.btnSave.clicked.connect(self.ui.actionSavePreference.trigger)

    def getUI_preference(self):
        # get value from QCombobox, value is selected in list 0, 45, 90
        dataset_label_rotation = int(
            self.ui.comboBox_datasetLabelRotation.currentText())

        # get value from QComboBox
        show_median = self.ui.comboBox_plotConfigShowMedianVal.currentText()
        if 'Yes' == show_median:
            show_median = True
        elif 'No' == show_median:
            show_median = False
        else:
            show_median = False

        # get value from QComboBox
        median_size = int(
            self.ui.comboBox_plotConfigMedianFontSize.currentText())

        # get value from QLineEdit
        skiprows = self.ui.lineEdit_dataConfigImportSkipRows.text()
        if skiprows == 'None':
            skiprows = None
        else:
            skiprows = skiprows.split(' ')
            # Filter out non-numeric string
            skiprows = [int(num) for num in skiprows if num.isnumeric()]
            skiprows = [row for row in skiprows if row >= 0]
            if len(skiprows) == 0:
                skiprows = None

        return dataset_label_rotation, show_median, median_size, skiprows

    def setUI_preference(
        self,
        dataset_label_rotation: int,
        show_median: bool,
        median_fontsize: int,
        rowskip: List[int]
    ) -> None:
        # Data validation
        if type(dataset_label_rotation) != int:
            dataset_label_rotation = 0
        else:
            if not dataset_label_rotation in [0, 45, 90]:
                dataset_label_rotation = 0

        if type(median_fontsize) != int:
            median_fontsize = 6
        else:
            if not median_fontsize in range(2, 10, 1):
                median_fontsize = 6

        if rowskip != None:
            rowskip = [num for num in rowskip if type(num) == int]
            rowskip = [num for num in rowskip if num >= 0]
            if len(rowskip) == 0:
                rowskip = None

        # Set UI
        try:
            self.ui.comboBox_datasetLabelRotation.setCurrentText(
                str(dataset_label_rotation))
        except:
            self.ui.comboBox_datasetLabelRotation.setCurrentIndex(0)

        if show_median:
            self.ui.comboBox_plotConfigShowMedianVal.setCurrentText('Yes')
        else:
            self.ui.comboBox_plotConfigShowMedianVal.setCurrentText('No')

        try:
            self.ui.comboBox_plotConfigMedianFontSize.setCurrentText(
                str(median_fontsize))
        except:
            self.ui.comboBox_plotConfigMedianFontSize.setCurrentIndex()

        if rowskip == None:
            self.ui.lineEdit_dataConfigImportSkipRows.setText('None')
        else:
            self.ui.lineEdit_dataConfigImportSkipRows.setText(
                ' '.join(map(str, rowskip)))

        return None


class DigitSpaceValidator(QRegularExpressionValidator):
    """
    Custom validator class to set Validator for Line Edit to only accept digits and space characters
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        # Regular expression to match digits and space characters only
        regex = QRegularExpression("[0-9 ]*")
        self.setRegularExpression(regex)

    def validate(self, input, pos):
        # Use the regular expression validation
        return super().validate(input, pos)
