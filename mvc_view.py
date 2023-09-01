''' 
- all .ui files designed from Qt Designer will be convert to .py file via PyQt6.uic function
- these will be imported to View module
- View module contains some Ui classes and these classes add UI component from imported prebuilt UI module
'''
from view.ui.Main_ui import Ui_Main
from view.ui.About_ui import Ui_About
from view.ui.PlotFigure_ui import Ui_PlotFigure
from view.PlotFigure import FigureCanVas
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets


# class for object Main window of application
class WidgetMain(QMainWindow):

    message = ""

    # update status bar message
    def updateSttBar(self, message: str):
        self.ui.statusbar.showMessage(message, 1000)
        self.ui.statusbar.repaint()


    def updateMessage(self, message: str):
        self.ui.txtbrowserMessage.append(message)
        self.ui.txtbrowserMessage.repaint()


    def __init__(self):
        super(WidgetMain, self).__init__()
        # GUI Main form
        self.ui = Ui_Main()
        self.ui.setupUi(self)


# GUI Plot list form
class WidgetPlotList(QWidget):
        
    pass


# GUI About form
class WidgetAbout(QWidget):

    def __init__(self):
        super(WidgetAbout, self).__init__()
        self.ui = Ui_About()
        self.ui.setupUi(self)


class WidgetPlotFigure(QWidget):

    def __init__(self):
        super(WidgetPlotFigure, self).__init__()
        self.ui = Ui_PlotFigure()
        self.ui.setupUi(self)

        sc = FigureCanVas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        # toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        # widget = QtWidgets.QWidget()
        # widget.setLayout(layout)
        self.setLayout(layout)
        # self.setCentralWidget(widget)


# Application UI object contains all other frame objects
class UI():

    def __init__(self) -> None:
        
        self.Main = WidgetMain()
        self.Main.show()
        self.About = WidgetAbout()
        # self.PlotFigure = WidgetPlotFigure()
        # self.PlotFigure.show()
        # Binding Menu action to slots
        self.Main.ui.actionShowAbout.triggered.connect(self.About.show)