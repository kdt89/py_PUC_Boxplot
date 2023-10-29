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


    # def __init__(self):
    #     self.plot_list_database = pd.DataFrame()
    #     self.plotPages = List[Figure]
        
    def _dataframe_to_plotpages(dataframe: pd.DataFrame) ->[]:

        try:
            if list(dataframe.columns) != ['Plot Item', 'LSL', 'USL', 'To Plot', 'Figure']:
                Status.error_message("Plot item in database have incorrect header.")
                Status.setting_update_ok = False
                return
        except:
            return

        # plotpages = List[Figure]
        plotpages = []
        
        # Divide dataframe to groups by column ['Figure']
        datagroups = dataframe.groupby(['Figure'], sort=False)
        
        # Iterate through each Figure group in dataframe and convert to PlotPage class object
        for groupname, group_data in datagroups:
            
            figure = Figure()
            figure.name = groupname
            
            for row in group_data.itertuples():
                subplot = Subplot(
                    subplotname= row[1], # ['Plot Item']
                    lowerspec= row[2], # 'LSL'
                    upperspec= row[3], # 'USL'
                    to_plot= row[4], # 'To Plot'
                    figurename= row[5]) # 'Figure'
                
                figure.subplot_list.append(subplot)

            plotpages.append(figure)

        return plotpages


    @staticmethod
    def update():

        df_plot_list = pd.read_csv(Setting.local_plot_list_database, index_col=None, sep=',', header=0)
        
        
        # load Plot list in local file database to object
        # update status of input data
        Status.list_import_files = [file for file in glob.glob(Setting.input_dir + './*.{}'.format(Setting.file_ext))]

        # Update the plot item in local database of setting to class object
        Setting.plotpages = Setting._dataframe_to_plotpages(df_plot_list)

        print("debug here")




    


        