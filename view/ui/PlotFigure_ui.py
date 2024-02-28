# Form implementation generated from reading ui file 'c:\PJT\PY\py_PUC_Boxplot\view\ui\PlotFigure.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PlotFigure(object):
    def setupUi(self, PlotFigure):
        PlotFigure.setObjectName("PlotFigure")
        PlotFigure.resize(872, 541)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlotFigure.sizePolicy().hasHeightForWidth())
        PlotFigure.setSizePolicy(sizePolicy)
        PlotFigure.setMinimumSize(QtCore.QSize(800, 430))
        PlotFigure.setBaseSize(QtCore.QSize(1920, 1080))
        self.gridLayoutWidget = QtWidgets.QWidget(parent=PlotFigure)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 871, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_main = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_main.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_main.setObjectName("gridLayout_main")
        self.tab_plotFigureHolder = QtWidgets.QTabWidget(parent=self.gridLayoutWidget)
        self.tab_plotFigureHolder.setObjectName("tab_plotFigureHolder")
        self.gridLayout_main.addWidget(self.tab_plotFigureHolder, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_main.addItem(spacerItem, 0, 1, 1, 1)
        self.btn_exportPPT = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_exportPPT.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_exportPPT.sizePolicy().hasHeightForWidth())
        self.btn_exportPPT.setSizePolicy(sizePolicy)
        self.btn_exportPPT.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        self.btn_exportPPT.setFont(font)
        self.btn_exportPPT.setMouseTracking(True)
        self.btn_exportPPT.setTabletTracking(False)
        self.btn_exportPPT.setStatusTip("")
        self.btn_exportPPT.setWhatsThis("")
        self.btn_exportPPT.setAccessibleName("")
        self.btn_exportPPT.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btn_exportPPT.setAutoFillBackground(False)
        self.btn_exportPPT.setStyleSheet("QPushButton {\n"
"  background-color: #ffffff;\n"
"  color: #000000;\n"
"  border: 1px solid #cccccc;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(0, 110, 200);\n"
"  color: rgb(255, 255, 255);\n"
"  border: 1px solid #cccccc;\n"
"}")
        self.btn_exportPPT.setText("Export PowerPoint")
        self.btn_exportPPT.setAutoDefault(False)
        self.btn_exportPPT.setFlat(False)
        self.btn_exportPPT.setObjectName("btn_exportPPT")
        self.gridLayout_main.addWidget(self.btn_exportPPT, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_main.addItem(spacerItem1, 1, 0, 1, 1)
        self.actionExportGraph2PPTX = QtGui.QAction(parent=PlotFigure)
        self.actionExportGraph2PPTX.setMenuRole(QtGui.QAction.MenuRole.PreferencesRole)
        self.actionExportGraph2PPTX.setObjectName("actionExportGraph2PPTX")

        self.retranslateUi(PlotFigure)
        QtCore.QMetaObject.connectSlotsByName(PlotFigure)

    def retranslateUi(self, PlotFigure):
        _translate = QtCore.QCoreApplication.translate
        PlotFigure.setWindowTitle(_translate("PlotFigure", "Box Plot View"))
        self.actionExportGraph2PPTX.setText(_translate("PlotFigure", "ExportGraph2PPTX"))
        self.actionExportGraph2PPTX.setToolTip(_translate("PlotFigure", "Export Graph to MS PowerPoint"))
