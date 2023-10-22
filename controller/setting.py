import os
import pandas as pd
from typing import List


class PlotFigure:

    def __init__(self):

        self.plotname = ""
        self.figureContainerName = ""
        self.lowerspec = -1
        self.upperspec = -1



class PlotContainerFigure:

    def __init__(self):

        self.plotFigureList: List[PlotFigure] = []
        self.containerFigureName = ""


class Setting:

    rootdir = os.path.abspath('')
    file_ext = 'csv'
    setting_filename = 'setting_plot.csv'
    input_dirname = "Input"
    output_dirname = "Output"
    data_row_to_skipread = [1, 2]
    plot_list_table_columns = ['Plot Item', 'LSL', 'USL', 'To Plot', 'Figures']


    def __init__(self):
        self.plot_list_database = pd.DataFrame()
        self.reading_cols = None
        self.input_dir = os.path.abspath(self.input_dirname)
        self.output_dir = os.path.abspath(self.output_dirname)

        self.plotFigures = PlotContainerFigure()
        

    # def 
    def update(self):

        self.plot_list_database = pd.read_csv(self.setting_filename, index_col=None, sep=',', header=0)
        
        # Validating the Plot List data loaded from local database (CVS file)
        # Need to implement printing the Invalid case to Main log UI
        if list(self.plot_list_database.columns) != self.plot_list_table_columns:
            print("Plot list file have mismatching column names")
            return






    


        