from __future__ import annotations
import os
import pandas as pd
from pandas import DataFrame
from typing import List
from controller.workstatus import Status

"""
A Figure contains multiple subplot object.
Each subplot object is a single box plot which are object returned by matplotlib.pyplot.boxplot()
"""

class PlotConfig:

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
        self.figure_name  = figurename


class FigureConfig:

    _MAX_ROW_SIZE = int(2); # maximum row of subplots
    _MAX_COL_SIZE = int(4); # maximum col of subplots

    def __init__(self):
        self.subplot_list: List[PlotConfig] = []
        # self.title: str = ""


    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, title: str):
        self._title = title


    @property
    def size(self) -> tuple[int, int]:
        subplot_count = len(self.subplot_list)

        if subplot_count < 4: # subplotsize in [1, 2, 3]
            row_size = 1
            column_size = subplot_count
        elif subplot_count == 4:
            row_size = 2
            column_size = 2
        elif subplot_count < 7: # subplotsize in [5, 6]
            row_size = 2
            column_size = 3
        else: # subplotsize > 7
            row_size = FigureConfig._MAX_ROW_SIZE
            column_size = FigureConfig._MAX_COL_SIZE

        return row_size, column_size


class Setting:

    ROOTDIR = os.path.abspath('')
    FILE_EXT: str = 'csv'
    LOCAL_PLOT_LIST_CONFIG_FILE: str = 'setting_plot.csv'
    
    INPUT_DIR = os.path.abspath("Input")
    OUTPUT_DIR = os.path.abspath("Output")
    PLOT_PAGES_GROUPBY_COLUMN_NAME: str = 'Figure'
    
    IMPORT_DATA_COLUMN_LIST: List[str] = []
    DATA_ROW_TO_SKIPREAD: List[int] = [1, 2]
    
    plotpages: List[FigureConfig] = []


    @staticmethod
    def update():

        df_plot_list = pd.read_csv(
            Setting.LOCAL_PLOT_LIST_CONFIG_FILE,
            index_col=None,
            sep=',',
            header=0)
        
        # Update the plot item in local database of setting to class object
        Setting.plotpages = Setting._dataframe_to_plotpages(df_plot_list)
        
        if len(Setting.plotpages) == 0:
            Status.setting_update_ok = False


    def _dataframe_to_plotpages(dataframe: DataFrame) -> List[FigureConfig]:
            try:
                if list(dataframe.columns) != ['Plot Item', 'LSL', 'USL', 'To Plot', 'Figure']:
                    Status.error_message("Plot item in database have incorrect header.")
                    Status.setting_update_ok = False
                    return
            except:
                return

            plotpages: List[FigureConfig] = []
            # Divide dataframe to groups by column ['Figure']
            datagroups = dataframe.groupby(
                Setting.PLOT_PAGES_GROUPBY_COLUMN_NAME, 
                sort=False)

            # Iterate through each Figure group in dataframe and convert to PlotPage class object
            for groupname, group_data in datagroups:
                
                figure_config = FigureConfig()
                figure_config.title = str(groupname)

                for row in group_data.itertuples():
                    subplot = PlotConfig(
                        subplotname= str(row[1]), # ['Plot Item']
                        lowerspec= float(row[2]), # 'LSL'
                        upperspec= float(row[3]), # 'USL'
                        to_plot= bool(row[4]), # 'To Plot'
                        figurename= str(row[5])) # 'Figure'
                    
                    # Adding ['Plot Item'] value to import_data_column_list, then Model object use this for import CSV data file
                    Setting.IMPORT_DATA_COLUMN_LIST.append(str(row[1]))

                    figure_config.subplot_list.append(subplot)

                # figure_config.update_figure_size()
                plotpages.append(figure_config)

            return plotpages