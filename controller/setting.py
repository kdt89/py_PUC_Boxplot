import os, glob
import pandas as pd
from typing import List
from typing import TypeAlias
from controller.workstatus import Status

"""
A Figure contains multiple subplot object.
Each subplot object is a single box plot which are object returned by matplotlib.pyplot.boxplot()
"""




class Subplot:

    def __init__(
        self, 
        subplotname: str = "",
        lowerspec: float = -1,
        upperspec: float = -1,
        to_plot: bool = False,
        figurename: str = "" ):

        self.subplotname = subplotname
        self.lowerspec = lowerspec
        self.upperspec = upperspec
        self.to_plot = to_plot
        self.figurename  = figurename


class Figure:

    def __init__(self):

        self.subplot_list: List[Subplot] = []
        self.name = ""
        self.rowsize = 0
        self.columnsize = 0


class Setting:

    rootdir = os.path.abspath('')
    file_ext = 'csv'
    local_plot_list_database = 'setting_plot.csv'
    
    input_dir = os.path.abspath("Input")
    output_dir = os.path.abspath("Output")
    
    reading_cols = None
    data_row_to_skipread = [1, 2]

    plotpages = List[Figure]
    # def load_local_plot_setting_database


    def __init__(self):
        self.plot_list_database = pd.DataFrame()
        self.plotPages = List[MultiPlotFigure]
        

    def _dataframe_to_plotpages(self, dataframe: pd.DataFrame) ->[]:

        try:
            if list(dataframe.columns) != ['Plot Item', 'LSL', 'USL', 'To Plot', 'Figure']:
                Status.error_message("Plot item in database have incorrect header.")
                Status.setting_update_ok = False
                return
        except:
            return

        # Divide dataframe to groups by column ['Figure']
        datagroups = dataframe.groupby(['Figure'], sort=False)
        
        # Iterate through each Figure group in dataframe and convert to PlotPage class object
        for groupname, group_data in datagroups:
            
            figure = Figure()
            figure.name = groupname
            
            for index, row in group_data:
                subplot = Subplot(
                    subplotname = row['Plot Item'],
                    lsl = row['LSL'],
                    usl = row['USL'],
                    to_plot = row['To Plot'],
                    figurename = row['Figure'])

                figure.plot_list.append(plot)

            self.plotpages.append(figure)

        return self.plotpages

            
            
            
            
            


        



    




    
    def update(self):

        self.plot_list_database = pd.read_csv(self.local_plot_list_database, index_col=None, sep=',', header=0)
        
        
        # load Plot list in local file database to object
        # update status of input data
        Status.list_import_files = [file for file in glob.glob(self.input_dir + './*.{}'.format(self.file_ext))]

        # Update the plot item in local database of setting to class object
        Setting.plotpages = self._dataframe_to_plotpages(self.plot_list_database)

        print("debug here")




    


        