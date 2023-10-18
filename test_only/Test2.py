import sys
import csv
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeySequence, QMessageBox
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QMenu, QActionGroup, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QDialog, QLabel, QLineEdit, QDialogButtonBox


class PlotListWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('Plot List')
        self.setMinimumWidth(600)
        
        self.data = []
        self.backup_data = []
        self.editable = False
        
        # Load data from csv file or create a new file if it doesn't exist
        try:
            with open('plotlist.csv', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    self.data.append(row)
                    self.backup_data.append(row)
        except FileNotFoundError:
            self.data = [['Header 1', 'Header 2', 'Header 3', 'Header 4', 'Header 5']]
            self.backup_data = [['Header 1', 'Header 2', 'Header 3', 'Header 4', 'Header 5']]
            with open('plotlist.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(self.data)
        
        # Create table view
        self.table_view = QTableView()
        self.table_model = TableModel(self.data)
        self.table_view.setModel(self.table_model)
        self.table_view.setEditTriggers(QTableView.NoEditTriggers)
        self.table_view.horizontalHeader().setStretchLastSection(True)
        
        # Create switch button to enable/disable edit mode
        self.switch_button = QPushButton('Edit Mode')
        self.switch_button.setCheckable(True)
        self.switch_button.clicked.connect(self.switch_editable)
        
        # Create layout and add widgets
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel('View/Edit mode:'))
        hbox.addWidget(self.switch_button)
        vbox.addLayout(hbox)
        vbox.addWidget(self.table_view)
        self.setLayout(vbox)
    
    def switch_editable(self):
        self.editable = not self.editable
        if self.editable:
            self.switch_button.setText('View Mode')
            self.table_view.setEditTriggers(QTableView.DoubleClicked)
        else:
            self.switch_button.setText('Edit Mode')
            self.table_view.setEditTriggers(QTableView.NoEditTriggers)
    
    def closeEvent(self, event):
        if self.table_model.data != self.backup_data:
            reply = QMessageBox.question(self, 'Save Changes', 'Do you want to save the changes?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.save_data()
        event.accept()
    
    def save_data(self):
        self.backup_data = self.data.copy()
        with open('plotlist.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.data)
        self.table_model.update_data(self.data)
        

class TableModel:
    def __init__(self, data):
        self.data = data
    
    def rowCount(self, parent):
        return len(self.data)
    
    def columnCount(self, parent):
        return len(self.data[0])
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.data[index.row()][index.column()]
    
    def update_data(self, new_data):
        self.data = new_data
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set window properties
