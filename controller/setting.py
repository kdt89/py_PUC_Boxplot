from __future__ import annotations
import os
import configparser
from typing import List


class Setting:

    ROOTDIR = os.path.abspath('')
    FILE_EXT: str = 'csv'
    LOCAL_FIGURECONFIG_FILENAME: str = 'Plot Config.csv'
    
    INPUT_DIR = os.path.abspath("Input")
    OUTPUT_DIR = os.path.abspath("Output")
    LIST_FIGURE_IMAGES: List[str] = []

    # Local preference which load from local and show on UI
    OPTS_LOCAL_FILENAME = 'preference.ini'
    OPTS_PLOTCONFIG_DATASET_LABEL_ROTATION: int = 0 # Rotation of Dataset label on Plot Figure. # 0: no rotation
    OPTS_PLOTCONFIG_SHOW_MEDIAN: bool = False
    OPTS_DATACONFIG_IMPORT_SKIP_ROW = None # List of integer

    PICTURE_WIDTH_HEIGHT_RATIO: float = 1.48 # following Minitab software Boxplot style
    PICTURE_MAX_WIDTH: float = 10.5
    PICTURE_MAX_HEIGHT: float = 4.65
    PLOTCONFIG_DATASET_NAME_LIST: List[str] = []

    def __init__(self):
        self.cfgparser = configparser.ConfigParser()
        self.cfgparser.optionxform = str # preserve case when read/write from/to INI file
        self.loadSetting()


    def loadSetting(self) -> None:
        self.cfgparser.read("preference.ini")
        
        try:
            dataset_labelrotation = self.cfgparser["OPTION"]["DATASET_LABEL_ROTATION"]
        except:
            dataset_labelrotation = 0 # default value
        try:
            rowskip = self.cfgparser["OPTION"]["DATA_IMPORT_SKIP_ROW_NUMBER"]
        except:
            rowskip = 'None' # default value
        try:
            show_median = self.cfgparser["OPTION"]["PLOT_SHOW_MEDIAN"]
        except:
            show_median = 'False' # default value

        if not dataset_labelrotation.isnumeric():
            dataset_labelrotation = 0 # default value
        else:
            dataset_labelrotation = int(dataset_labelrotation)
            if not dataset_labelrotation in [0, 45, 90]:
                dataset_labelrotation = 0 # default value

        match show_median:
            case 'True':
                show_median = True
            case 'False':
                show_median = False
            case _:
                show_median = False

        if rowskip == 'None':
            rowskip = None
        else:
            rowskip = rowskip.split(' ')
            rowskip = [num for num in rowskip if num.isnumeric()] # Filter out non-numeric string
            rowskip = list(map(int, rowskip))
            rowskip = [row for row in rowskip if row >= 0]
            if len(rowskip) == 0:
                rowskip = None

        Setting.OPTS_PLOTCONFIG_DATASET_LABEL_ROTATION = dataset_labelrotation # must be integer [0, 45, 90]
        Setting.OPTS_PLOTCONFIG_SHOW_MEDIAN = show_median # must be boolean
        Setting.OPTS_DATACONFIG_IMPORT_SKIP_ROW = rowskip # must be None or list integer


    def saveSetting(
            self,
            plotconfig_datasetLabelRotation: int,
            plotconfig_showMedian: bool,
            dataconfig_importSkipRows: List[int]
            ) -> None:
        # argument validation
        if type(plotconfig_datasetLabelRotation) != int:
            plotconfig_datasetLabelRotation = 0
        if not plotconfig_datasetLabelRotation in [0, 45, 90]:
            plotconfig_datasetLabelRotation = 0
        
        if type(plotconfig_showMedian) != bool:
            plotconfig_showMedian = False

        if type(dataconfig_importSkipRows) != int:
            dataconfig_importSkipRows = 0
        if dataconfig_importSkipRows < 0:
            dataconfig_importSkipRows = 0

        Setting.OPTS_PLOTCONFIG_DATASET_LABEL_ROTATION = plotconfig_datasetLabelRotation
        Setting.OPTS_PLOTCONFIG_SHOW_MEDIAN = plotconfig_showMedian
        Setting.OPTS_DATACONFIG_IMPORT_SKIP_ROW = dataconfig_importSkipRows

        self.cfgparser["OPTION"]["DATASET_LABEL_ROTATION"] = str(plotconfig_datasetLabelRotation)
        self.cfgparser["OPTION"]["PLOT_SHOW_MEDIAN"] = str(plotconfig_showMedian)

        if dataconfig_importSkipRows == None:
            self.cfgparser["OPTION"]["DATA_IMPORT_SKIP_ROW_NUMBER"] = str('None')
        else:
            self.cfgparser["OPTION"]["DATA_IMPORT_SKIP_ROW_NUMBER"] = ' '.join(map(str, dataconfig_importSkipRows))
            
        with open("preference.ini", "w") as configfile:
            self.cfgparser.write(configfile)
            configfile.close()