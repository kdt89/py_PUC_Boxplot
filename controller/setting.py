from __future__ import annotations
import os
import pandas as pd
from typing import List
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
    
    import_data_column_list = []
    data_row_to_skipread = [1, 2]
    
    plotpages = List[Figure]


    @staticmethod
    def update():

        df_plot_list = pd.read_csv(Setting.local_plot_list_database, index_col=None, sep=',', header=0)
        
        # Update the plot item in local database of setting to class object
        Setting.plotpages = Setting._dataframe_to_plotpages(df_plot_list)
        
        if len(Setting.plotpages) == 0:
            Status.setting_update_ok = False


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
                        subplotname= str(row[1]), # ['Plot Item']
                        lowerspec= float(row[2]), # 'LSL'
                        upperspec= float(row[3]), # 'USL'
                        to_plot= bool(row[4]), # 'To Plot'
                        figurename= str(row[5])) # 'Figure'
                    
                    # Adding ['Plot Item'] value to import_data_column_list, then Model object use this for import CSV data file
                    Setting.import_data_column_list.append(str(row[1]))

                    figure.subplot_list.append(subplot)

                plotpages.append(figure)

            return plotpages