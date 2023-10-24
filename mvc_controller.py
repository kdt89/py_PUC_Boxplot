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

        self.bindSignalAndSlot()
        # let Controller (class Process object) subscribe to Model object Event (Observer pattern)
        self.model.attach(self)
        # Show initial message to UI
        self.view.Main.updateMessage(f"<b>Program initialized at: </b> \
                                  <font color='blue'>{self.setting.rootdir}\
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
    
    """ Grab matched files in Input folder and pass to Model object to import to database """
    def import_input_data(self) -> None:

        # update Setting from user
        self.view.Main.updateMessage("- User setting loaded")

        input_files_count = len(Status.list_import_files)
        if input_files_count > 0:
            self.view.Main.updateMessage(f"- Found {input_files_count} data files to be input")
            Status.set_input_status(True)
        else:
            Status.set_input_status(False)
            self.view.Main.updateMessage("There are no data files in Input directory")
            return None
        
        # pass import file to Model object to import data
        self.model.database.import_csv_files(
            Status.list_import_files,
            Setting.reading_cols,
            Setting.data_row_to_skipread,
            self.view.Main.updateSttBar)

        rows, columns = self.model.database.get_data().shape
        self.view.Main.updateMessage(f"- Input data imported successfully: {rows} rows - {columns} columns")

        # Test

    '''
    Function ask View to render Plot
    '''
    def build_boxplot(self)->None:
        pass
        # Request View class to render and show up a new Frame window



    '''
    Function to export data in Model to output folder
    '''
    def export_data(self)->None:

        self.model.database.export_data(self.setting.output_dir)


    """
    Define methods execute when occuring Event from View
    """
    def btnMakePlot_actions(self):
        
        # Notice to UI
        self.view.Main.updateMessage(f"\n <b>Making Plot from data files in Input directory</b>...")
        
        self.setting.update()
        
        if not Status.setting_update_ok:
            self.view.Main.updateMessage(Status.error_message)
            Status.clear_error_message()
            return
        
        self.import_input_data()

        if not Status.input_ready:
            self.view.Main.updateMessage("There are no data files in Input directory") # status bar
            return None
        
        self.export_data()
        self.build_boxplot()
        # Notice to UI
        
        # Export combined data to Output folder
        # Rendering box plot via View object
        # Call View module to draw Plot





        # ==== 4. DRAW BOXPLOT USING PLOTLY MODULE ====

        # 1 visualization page contains 1 figure
        # 1 figure contains 1 subplots grid
        # 1 subplots contains multiple traces 
        # 1 subplots equal to 1 group categorized by 'Group' column in [user]setting_boxplot.csv file
        # 1 trace is 1 boxplot made from df_base dataframe


        # get pandas groupby object of df_base
        # this is for the later use of get_group() to check for how many plot
        # should be contains in one figure