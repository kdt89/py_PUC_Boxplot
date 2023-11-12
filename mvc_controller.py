from __future__ import annotations
import mvc_model
import mvc_view
from controller.setting import Setting
from controller.workstatus import Status
from util.observer import Observer, Subject


class Controller(Observer): # Controller in MVC pattern

    def __init__(self, model: mvc_model.Model, view: mvc_view.UI):
        self.model = model
        self.view = view
        self.setting = Setting()

        # let Controller (class Process object) subscribe to Model object Event (Observer pattern)
        self.model.attach(self)
        self.model.notify
        
        self.bindSignalAndSlot()
        # Show initial message to UI
        self.view.Main.updateMessage(f"<b>Program initialized at: </b> \
                                  <font color='blue'>{self.setting.ROOTDIR}\
                                  </font>")

    """
    Define inherited methods from Observer class
    """
    # Receive update from subject.
    def update(self, subject: Subject) -> None:
        self.view.Main.updateMessage(subject._status)


    """
    Binding PyQt signal & slot
    """
    def bindSignalAndSlot(self):
        self.view.Main.ui.btnMakePlot.clicked.connect(self.btnMakePlot_actions)

    """
    DEFIND METHODS FOR INTERAL USE WITHIN CONTROLLER MODULE
    """
    



    """
    Define methods execute when occuring Event from View
    """
    def btnMakePlot_actions(self):
        # Notice to UI
        self.view.Main.updateMessage(f"\n <b>Making Plot from data files in Input directory</b>...")
        Setting.update()
        Status.update_list_input_files(Setting.INPUT_DIR, Setting.FILE_EXT)
        self.import_input_data()

        if not Status.input_status_ready:
            self.view.Main.updateMessage("There are no data files in Input directory") # status bar
            return None

        self.export_data()        
        # Build figure plot pages on PlotFigure Widget
        self.build_boxplot()
        

    '''
    Function to export data in Model to output folder
    '''
    def export_data(self)->None:
        self.model.database.export_data(Setting.OUTPUT_DIR)


    def build_boxplot(self)-> None:
        self.view.wxPlotFigure_newWidget()
        if self.view.PlotFigure != None:
            self.view.PlotFigure.build_plot_pages(
                Setting.plotpages,
                self.model.database)
        
        self.view.PlotFigure.show()
        

    """ Grab matched files in Input folder and pass to Model object to import to database """
    def import_input_data(self) -> None:
        # update Setting from user
        self.view.Main.updateMessage("- User setting loaded")

        input_status_files_count = len(Status.input_status_list_files)
        if input_status_files_count > 0:
            self.view.Main.updateMessage(f"- Found {input_status_files_count} data files to be input")
            Status.input_status_ready = True
        else:
            Status.input_status_ready = False
            self.view.Main.updateMessage("There are no data files in Input directory")
            return None
        
        # pass import file to Model object to import data
        self.model.database.import_csv_files(
            Status.input_status_list_files,
            Setting.IMPORT_DATA_COLUMN_LIST,
            Setting.DATA_ROW_TO_SKIPREAD,
            self.view.Main.updateSttBar)

        rows, columns = self.model.database.size
        self.view.Main.updateMessage(f"- Input data imported successfully: {rows} rows - {columns} columns")