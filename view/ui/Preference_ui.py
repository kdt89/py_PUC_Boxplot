# Form implementation generated from reading ui file 'c:\PJT\PY\py_PUC_Boxplot\view\ui\Preference.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Preference(object):
    def setupUi(self, Preference):
        Preference.setObjectName("Preference")
        Preference.resize(544, 388)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Preference.sizePolicy().hasHeightForWidth())
        Preference.setSizePolicy(sizePolicy)
        Preference.setWindowTitle("Preference")
        Preference.setToolTip("")
        Preference.setStatusTip("")
        Preference.setWhatsThis("")
        Preference.setAccessibleName("")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Preference)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 0, 519, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.vLayout_main = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vLayout_main.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.vLayout_main.setContentsMargins(0, 0, 0, 0)
        self.vLayout_main.setObjectName("vLayout_main")
        self.lbl_preference = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_preference.sizePolicy().hasHeightForWidth())
        self.lbl_preference.setSizePolicy(sizePolicy)
        self.lbl_preference.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_preference.setMouseTracking(True)
        self.lbl_preference.setToolTip("")
        self.lbl_preference.setStatusTip("")
        self.lbl_preference.setWhatsThis("")
        self.lbl_preference.setAccessibleName("")
        self.lbl_preference.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#0032c8;\">Preference</span></p></body></html>")
        self.lbl_preference.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lbl_preference.setObjectName("lbl_preference")
        self.vLayout_main.addWidget(self.lbl_preference)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout_main.addItem(spacerItem)
        self.gridlayout_nestedMainLayout = QtWidgets.QGridLayout()
        self.gridlayout_nestedMainLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridlayout_nestedMainLayout.setObjectName("gridlayout_nestedMainLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridlayout_nestedMainLayout.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.comboBox_dataLabelAngle = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_2)
        self.comboBox_dataLabelAngle.setObjectName("comboBox_dataLabelAngle")
        self.comboBox_dataLabelAngle.addItem("")
        self.comboBox_dataLabelAngle.addItem("")
        self.comboBox_dataLabelAngle.setItemText(1, "45")
        self.comboBox_dataLabelAngle.addItem("")
        self.gridlayout_nestedMainLayout.addWidget(self.comboBox_dataLabelAngle, 0, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(300, 100))
        self.label.setText("Dataset Label Rotation On Plot")
        self.label.setObjectName("label")
        self.gridlayout_nestedMainLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridlayout_nestedMainLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridlayout_nestedMainLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridlayout_nestedMainLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_NumRowToSkipImportData = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_NumRowToSkipImportData.sizePolicy().hasHeightForWidth())
        self.lineEdit_NumRowToSkipImportData.setSizePolicy(sizePolicy)
        self.lineEdit_NumRowToSkipImportData.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEdit_NumRowToSkipImportData.setObjectName("lineEdit_NumRowToSkipImportData")
        self.gridlayout_nestedMainLayout.addWidget(self.lineEdit_NumRowToSkipImportData, 2, 2, 1, 1)
        self.comboBox_plotMedianYesNo = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.comboBox_plotMedianYesNo.setFont(font)
        self.comboBox_plotMedianYesNo.setToolTip("")
        self.comboBox_plotMedianYesNo.setStatusTip("")
        self.comboBox_plotMedianYesNo.setWhatsThis("")
        self.comboBox_plotMedianYesNo.setAccessibleName("")
        self.comboBox_plotMedianYesNo.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.comboBox_plotMedianYesNo.setCurrentText("Yes")
        self.comboBox_plotMedianYesNo.setPlaceholderText("")
        self.comboBox_plotMedianYesNo.setFrame(False)
        self.comboBox_plotMedianYesNo.setObjectName("comboBox_plotMedianYesNo")
        self.comboBox_plotMedianYesNo.addItem("")
        self.comboBox_plotMedianYesNo.setItemText(0, "Yes")
        self.comboBox_plotMedianYesNo.addItem("")
        self.comboBox_plotMedianYesNo.setItemText(1, "No")
        self.gridlayout_nestedMainLayout.addWidget(self.comboBox_plotMedianYesNo, 1, 2, 1, 1)
        self.vLayout_main.addLayout(self.gridlayout_nestedMainLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.vLayout_main.addItem(spacerItem3)
        self.btnSave = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.btnSave.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnSave.setToolTip("")
        self.btnSave.setStatusTip("")
        self.btnSave.setWhatsThis("")
        self.btnSave.setAccessibleName("")
        self.btnSave.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnSave.setText("Save")
        self.btnSave.setObjectName("btnSave")
        self.vLayout_main.addWidget(self.btnSave)
        self.actionSaveAndClose = QtGui.QAction(parent=Preference)
        self.actionSaveAndClose.setText("SaveAndClose")
        self.actionSaveAndClose.setIconText("SaveAndClose")
        self.actionSaveAndClose.setToolTip("SaveAndClose")
        self.actionSaveAndClose.setStatusTip("")
        self.actionSaveAndClose.setWhatsThis("")
        self.actionSaveAndClose.setShortcut("")
        self.actionSaveAndClose.setMenuRole(QtGui.QAction.MenuRole.ApplicationSpecificRole)
        self.actionSaveAndClose.setObjectName("actionSaveAndClose")

        self.retranslateUi(Preference)
        QtCore.QMetaObject.connectSlotsByName(Preference)

    def retranslateUi(self, Preference):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("Preference", "Median Value"))
        self.comboBox_dataLabelAngle.setItemText(0, _translate("Preference", "0-Horizontal"))
        self.comboBox_dataLabelAngle.setItemText(2, _translate("Preference", "90-Vertical"))
        self.label_3.setText(_translate("Preference", "Number of rows to skip when import data from CSV"))
