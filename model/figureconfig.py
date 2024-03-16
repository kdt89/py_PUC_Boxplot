from typing import List
from model.plotconfig import PlotConfig
from util.string import String
import pandas as pd
from controller.setting import Setting


class FigureConfig:
    def __init__(self):
        self.plotconfig_list: List[PlotConfig] = []
        self._title: str = ""
        self._name: str = ""        # similar to _title but replace wildcard character with '-'

    @property                       # there is not setter for property 'name'
    def name(self) -> str:
        return self._name

    @property
    def title(self) -> str:
        return self._title

    @property
    def size(self) -> tuple[int, int]:
        subplot_count = len(self.plotconfig_list)
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
            row_size = FigureConfigList._MAX_ROW_SIZE
            column_size = FigureConfigList._MAX_COL_SIZE

        return row_size, column_size


    @title.setter                   # set value for property 'title' will set 'name' alongside
    def title(self, string: str):
        self._title = string
        self._name = String.replaceUnacceptedString(string, '-')

"""
A Figure contains multiple subplot object.
Each subplot object is a single box plot which are object returned by matplotlib.pyplot.boxplot()
"""
class FigureConfigList:

    _MAX_ROW_SIZE = int(2); # maximum row of subplots
    _MAX_COL_SIZE = int(4); # maximum col of subplots
    PLOTCONFIG_BASE_COLUMNS: str = ['Plot Item', 'Plot Title', 'LSL', 'USL', 'To Plot', 'Figure']
    PLOTCONFIG_GROUPBY_COLUMN: str = 'Figure'
    DATA_IMPORT_COLUMN_LIST: List[str] = []
    LOCAL_FIGURECONFIG_FILE = Setting.LOCAL_FIGURECONFIG_FILENAME

    def __init__(self):
        self.list: List[FigureConfig] = []

    def update(self) -> None:
        try:
            local_plot_list = pd.read_csv(self.LOCAL_FIGURECONFIG_FILE, index_col=None, sep=',', header=0)
        except:
            return

        if list(local_plot_list.columns) != self.PLOTCONFIG_BASE_COLUMNS:
            return

        # Clear the list of column name of data to be import before updating again
        self.DATA_IMPORT_COLUMN_LIST.clear()
        self.list.clear()
        
        # Divide dataframe to groups by column ['Figure']
        plot_list_datagroups = local_plot_list.groupby(self.PLOTCONFIG_GROUPBY_COLUMN, sort=False)
        
        # Iterate through each Figure group in dataframe and convert to PlotPage class object
        for groupname, group_data in plot_list_datagroups:
            figureconfig = FigureConfig()
            figureconfig.title = str(groupname)
    
            for row in group_data.itertuples():
                plotname = row[1]               # ['Plot Item']
                plottitle = row[2]              # 'Plot Title'
                try:
                    lowerspec = float(row[3])   # 'LSL'
                except:
                    lowerspec = None
                try:
                    upperspec = float(row[4])   # 'USL'
                except:
                    upperspec = None
                to_plot = row[5]                # 'To Plot'
                to_plot = True if to_plot == 'Yes' else False

                # Adding ['Plot Item'] value to import_data_column_list, 
                # then Model object use this for import CSV data file
                if to_plot:
                    plotconfig = PlotConfig(plotname, plottitle, lowerspec, upperspec, to_plot)
                    self.DATA_IMPORT_COLUMN_LIST.append(str(row[1]))
                    figureconfig.plotconfig_list.append(plotconfig)

            # keep only figure config that the plot config is not empty
            if len(figureconfig.plotconfig_list) > 0:
                self.list.append(figureconfig)