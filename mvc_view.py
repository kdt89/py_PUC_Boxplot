''' 
- all .ui files designed from Qt Designer will be convert to .py file via PyQt6.uic function
- these will be imported to View module
- View module contains some Ui classes and these classes add UI component from imported prebuilt UI module
'''
from view.widgetMain import WidgetMain
from view.widgetAbout import WidgetAbout
from view.widgetPlotFigure import WidgetPlotFigure


# Application UI object contains all other frame objects
class View():

    def __init__(self) -> None:
        self.Main = WidgetMain()
        self.About = WidgetAbout()
        self.PlotFigure: WidgetPlotFigure = None
        
        # Binding Menu action to slots
        self.Main.ui.actionShowAbout.triggered.connect(self.About.show)

        # Display main window
        self.Main.show()


    def wxPlotFigure_newWidget(self):
        # close previous Plot Figure widget if existing
        if not self.PlotFigure is None:
            if self.PlotFigure.isVisible():
                self.PlotFigure.close()

        # intentionally abandon self.PlotFigure. Gabage collection will take care of it
        self.PlotFigure = WidgetPlotFigure()
  