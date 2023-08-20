''' 
- all .ui files designed from Qt Designer will be convert to .py file via PyQt6.uic function
- these will be imported to View module
- View module contains some Ui classes and these classes add UI component from imported prebuilt UI module
'''
from view.ui import Main_ui
from view.ui import About_ui
from view.ui import PlotFigure_ui
from view.plotting import FigureCanVas
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget


# class for object Main window of application
class UI_Main(QMainWindow):

    message = ""

    # update status bar message
    def updateSttBar(self, message: str):
        self.ui.statusbar.showMessage(message, 1000)
        self.ui.statusbar.repaint()


    def updateMessage(self, message: str):
        self.ui.txtbrowserMessage.append(message)
        self.ui.txtbrowserMessage.repaint()


    def __init__(self):
        super(UI_Main, self).__init__()
        # GUI Main form
        self.ui = Main_ui.Ui_frame()
        self.ui.setupUi(self)


# GUI Plot list form
class UI_PlotList(QWidget):
        
    pass


# GUI About form
class UI_About(QWidget):

    def __init__(self):
        super(UI_About, self).__init__()
        self.ui = About_ui.Ui_frame()
        self.ui.setupUi(self)


class Frm_PlotSetting(QWidget):

    pass
        

class UI_PlotFigure(QWidget):

    def __init__(self):
        super(UI_PlotFigure, self).__init__()
        self.ui = PlotFigure_ui.Ui_frame()
        self.ui.setupUi(self)


# Application UI object contains all other frame objects
class UI():

    def __init__(self) -> None:
        
        self.Main = UI_Main()
        self.Main.show()
        self.About = UI_About()
        
        # Binding Menu action to slots
        self.Main.ui.actionShowAbout.triggered.connect(self.About.show)