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
            dataset_labelrotation = int(self.cfgparser["OPTION"]["DATASET_LABEL_ROTATION"])
            if 0 > dataset_labelrotation:
                dataset_labelrotation = 0
        except:
            dataset_labelrotation = 0

        try:
            show_median = self.cfgparser["OPTION"]["PLOT_SHOW_MEDIAN"]
            if show_median == 'True': # string type
                show_median = True # bool type
            elif show_median == 'False':
                show_median = False
            else:
                show_median = False
        except:
            show_median = False

        try:
            rowskip = self.cfgparser["OPTION"]["DATA_IMPORT_SKIP_ROW_NUMBER"]
            if rowskip == 'None':
                rowskip = None
            else:
                rowskip = rowskip.split(' ')
                rowskip = [num for num in rowskip if type(num) == int]
                rowskip = list(map(int, rowskip))
                rowskip = [row for row in rowskip if row >= 0]
                if len(rowskip) == 0:
                    rowskip = None
        except:
            rowskip = None

        Setting.OPTS_PLOTCONFIG_DATASET_LABEL_ROTATION = dataset_labelrotation
        Setting.OPTS_PLOTCONFIG_SHOW_MEDIAN = show_median
        Setting.OPTS_DATACONFIG_IMPORT_SKIP_ROW = rowskip


    def saveSetting(
            self,
            plotconfig_datasetLabelRotation: int,
            plotconfig_showMedian: bool,
            dataconfig_importSkipRow: List[int]
            ) -> None:
        # argument validation
        if type(plotconfig_datasetLabelRotation) != int:
            plotconfig_datasetLabelRotation = 0
        if not plotconfig_datasetLabelRotation in [0, 45, 90]:
            plotconfig_datasetLabelRotation = 0
        
        if type(plotconfig_showMedian) != bool:
            plotconfig_showMedian = False

        if type(dataconfig_importSkipRow) != int:
            dataconfig_importSkipRow = 0
        if dataconfig_importSkipRow < 0:
            dataconfig_importSkipRow = 0

        Setting.OPTS_PLOTCONFIG_DATASET_LABEL_ROTATION = plotconfig_datasetLabelRotation
        Setting.OPTS_PLOTCONFIG_SHOW_MEDIAN = plotconfig_showMedian
        Setting.OPTS_DATACONFIG_IMPORT_SKIP_ROW = dataconfig_importSkipRow

        self.cfgparser["OPTION"]["DATASET_LABEL_ROTATION"] = str(plotconfig_datasetLabelRotation)
        self.cfgparser["OPTION"]["PLOT_SHOW_MEDIAN"] = str(plotconfig_showMedian)

        if dataconfig_importSkipRow == None:
            self.cfgparser["OPTION"]["DATA_IMPORT_SKIP_ROW_NUMBER"] = str('None')
        else:
            self.cfgparser["OPTION"]["DATA_IMPORT_SKIP_ROW_NUMBER"] = ' '.join(map(str, dataconfig_importSkipRow))
            
        with open("preference.ini", "w") as configfile:
            self.cfgparser.write(configfile)
            configfile.close()