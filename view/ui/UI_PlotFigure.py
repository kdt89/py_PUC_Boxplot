# Form implementation generated from reading ui file 'PlotFigure.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PlotFigure(object):
    def setupUi(self, PlotFigure):
        PlotFigure.setObjectName("PlotFigure")
        PlotFigure.resize(1570, 939)
        self.verticalLayoutWidget = QtWidgets.QWidget(PlotFigure)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 1551, 871))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutWidget = QtWidgets.QWidget(PlotFigure)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1320, 0, 241, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layoutMain = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layoutMain.setContentsMargins(0, 0, 0, 0)
        self.layoutMain.setObjectName("layoutMain")
        self.btnExport_MS_PPT = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnExport_MS_PPT.setObjectName("btnExport_MS_PPT")
        self.layoutMain.addWidget(self.btnExport_MS_PPT)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.layoutMain.addItem(spacerItem)
        self.btnExportImage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnExportImage.setObjectName("btnExportImage")
        self.layoutMain.addWidget(self.btnExportImage)

        self.retranslateUi(PlotFigure)
        QtCore.QMetaObject.connectSlotsByName(PlotFigure)

    def retranslateUi(self, PlotFigure):
        _translate = QtCore.QCoreApplication.translate
        PlotFigure.setWindowTitle(_translate("PlotFigure", "Box Plot Graph"))
        self.btnExport_MS_PPT.setText(_translate("PlotFigure", "Export MS PowerPoint"))
        self.btnExportImage.setText(_translate("PlotFigure", "Export Image"))
