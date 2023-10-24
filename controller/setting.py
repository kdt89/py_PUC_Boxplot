import os, glob
import pandas as pd
from typing import List
from controller.workstatus import Status


class SinglePlot:

    def __init__(self):

        self.plotname = ""
        self.lowerspec = -1
        self.upperspec = -1
        self.is_plot = False
        self.figureContainerName = ""


class MultiPlotFigure:

    def __init__(self):

        self.plotFigureList: List[SinglePlot] = []
        self.containerFigureName = ""
        self.rowsize = 0
        self.columnsize = 0

class Setting:

    rootdir = os.path.abspath('')
    file_ext = 'csv'
    local_plot_list_database = 'setting_plot.csv'
    input_dirname = "Input"
    output_dirname = "Output"
    reading_cols = None
    
    data_row_to_skipread = [1, 2]

    # def load_local_plot_setting_database


    def __init__(self):
        self.plot_list_database = pd.DataFrame()
        self.input_dir = os.path.abspath(self.input_dirname)
        self.output_dir = os.path.abspath(self.output_dirname)

        self.plotPages = List[MultiPlotFigure]
        

    # def 



    
    def update(self):

        self.plot_list_database = pd.read_csv(self.local_plot_list_database, index_col=None, sep=',', header=0)
        
        # Validating the Plot List data loaded from local database (CVS file)
        # Need to implement printing the Invalid case to Main log UI
        if list(self.plot_list_database.columns) != ['Plot Item', 'LSL', 'USL', 'To Plot', 'Figure']:
            Status.error_message("Plot item in database have incorrect header.")
            Status.setting_update_ok = False
            return
        else:
            Status.setting_update_ok = True
        
        # load Plot list in local file database to object
        # update status of input data
        Status.list_import_files = [file for file in glob.glob(self.input_dir + './*.{}'.format(self.file_ext))]






    


        