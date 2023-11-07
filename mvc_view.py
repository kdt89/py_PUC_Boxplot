''' 
- all .ui files designed from Qt Designer will be convert to .py file via PyQt6.uic function
- these will be imported to View module
- View module contains some Ui classes and these classes add UI component from imported prebuilt UI module
'''
from view.widgetMain import WidgetMain
from view.widgetAbout import WidgetAbout
from view.widgetPlotFigure import WidgetPlotFigure


# Application UI object contains all other frame objects
class UI():

    def __init__(self) -> None:
        self.Main = WidgetMain()
        self.About = WidgetAbout()
        self.PlotFigure = WidgetPlotFigure()
        
        self.Main.show()
        self.PlotFigure.show()
        
        # Binding Menu action to slots
        self.Main.ui.actionShowAbout.triggered.connect(self.About.show)