import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog, QVBoxLayout, QHBoxLayout, QTableView, QPushButton
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plot List Application")
        self.setWindowIcon(QIcon("icon.png"))

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("Settings")
        helpMenu = menubar.addMenu("Help")

        plotListAct = QAction("Plot List", self)
        plotListAct.triggered.connect(self.showPlotList)
        fileMenu.addAction(plotListAct)

        aboutAct = QAction("About", self)
        aboutAct.triggered.connect(self.showAbout)
        helpMenu.addAction(aboutAct)

        self.statusBar().showMessage("Ready")

    def showPlotList(self):
        plotListDialog = QDialog(self)
        plotListDialog.setWindowTitle("Plot List")

        vbox = QVBoxLayout()

        self.tableView = QTableView()
        self.tableView.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self.loadCsvData()
        # self.tableView.EditTrigger

        hbox = QHBoxLayout()
        self.editableSwitch = QPushButton("Enable Edit")
        self.editableSwitch.setCheckable(True)
        self.editableSwitch.clicked.connect(self.enableEdit)
        hbox.addStretch()
        hbox.addWidget(self.editableSwitch)

        vbox.addWidget(self.tableView)
        vbox.addLayout(hbox)

        plotListDialog.setLayout(vbox)
        plotListDialog.exec()

    def showAbout(self):
        QMessageBox.about(self, "About", "This is a Plot List Application written in Python using PyQt6.")

    def loadCsvData(self):
        try:
            df = pd.read_csv("plotlist.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Plot Name", "X Axis Label", "Y Axis Label", "Color", "LineStyle"])

        self.plotlist = df
        self.tableView.setModel(self.plotlist)

    def saveCsvData(self):
        self.plotlist.to_csv("plotlist.csv", index=False)

    def enableEdit(self):
        if self.editableSwitch.isChecked():
            self.tableView.setEditTriggers(QTableView.DoubleClicked)
            self.editableSwitch.setText("Disable Edit")
        else:
            self.tableView.setEditTriggers(QTableView.NoEditTriggers)
            self.editableSwitch.setText("Enable Edit")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Save Changes", "Do you want to save the changes you made?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.saveCsvData()
        elif reply == QMessageBox.Cancel:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
