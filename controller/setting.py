from __future__ import annotations
import os
import pandas as pd
from typing import List
from controller.workstatus import Status

"""
A Figure contains multiple subplot object.
Each subplot object is a single box plot which are object returned by matplotlib.pyplot.boxplot()
"""

class SubplotConfig:

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


class FigureConfig:

    _MAX_ROW_SIZE = 2; # maximum row of subplots
    _MAX_COL_SIZE = 4; # maximum col of subplots

    def __init__(self):

        self.subplot_list: List[SubplotConfig] = []
        self.name = ""
        self.rowsize = 0
        self.columnsize = 0


    def update_figure_size(self):
        subplot_count = len(self.subplot_list)

        if subplot_count < 4: # subplotsize in [1, 2, 3]
            self.rowsize = 1
            self.columnsize = subplot_count
        elif subplot_count == 4:
            self.rowsize = 2
            self.columnsize = 2
        elif subplot_count < 7: # subplotsize in [5, 6]
            self.rowsize = 2
            self.columnsize = 3
        else: # subplotsize > 7
            self.rowsize = self._maxrow
            self.columnsize = self._maxcol


class Setting:

    rootdir = os.path.abspath('')
    file_ext = 'csv'
    local_plot_list_database = 'setting_plot.csv'
    
    input_dir = os.path.abspath("Input")
    output_dir = os.path.abspath("Output")
    
    import_data_column_list = []
    data_row_to_skipread = [1, 2]
    
    plotpages = List[FigureConfig]


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
                
                figure_config = FigureConfig()
                figure_config.name = groupname

                for row in group_data.itertuples():
                    subplot = SubplotConfig(
                        subplotname= str(row[1]), # ['Plot Item']
                        lowerspec= float(row[2]), # 'LSL'
                        upperspec= float(row[3]), # 'USL'
                        to_plot= bool(row[4]), # 'To Plot'
                        figurename= str(row[5])) # 'Figure'
                    
                    # Adding ['Plot Item'] value to import_data_column_list, then Model object use this for import CSV data file
                    Setting.import_data_column_list.append(str(row[1]))

                    figure_config.subplot_list.append(subplot)

                figure_config.update_figure_size()
                plotpages.append(figure_config)

            return plotpages