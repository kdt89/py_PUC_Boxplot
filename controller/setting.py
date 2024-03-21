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

    # Local preference which load from local and show on UI
    OPTS_LOCAL_FILENAME = 'preference.ini'
    # Rotation of Dataset label on Plot Figure. # 0: no rotation
    OPTS_PLOTCONFIG_DATASET_LABEL_ROTATION: int = 0
    OPTS_PLOTCONFIG_SHOW_MEDIAN: bool = False
    OPTS_MEDIAN_FONT_SIZE: int = 6
    OPTS_DATACONFIG_IMPORT_SKIP_ROW = [1, 2]  # List of integer

    # following Minitab software Boxplot style
    PICTURE_WIDTH_HEIGHT_RATIO: float = 1.48
    PICTURE_MAX_WIDTH: float = 10.5
    PICTURE_MAX_HEIGHT: float = 4.65
    PLOTCONFIG_DATASET_NAME_LIST: List[str] = []

    def __init__(self):
        self.cfgparser = configparser.ConfigParser()
        self.cfgparser.optionxform = str  # preserve case when read/write from/to INI file
        self.loadSetting()

    def loadSetting(self) -> None:
        self.cfgparser.read("preference.ini")

        # Initialization
        dataset_labelrotation = 0
        rowskip = ""
        show_median = False
        median_fontsize = 6
        # PARSING VALUE FROM LOCAL FILE
        try:
            dataset_labelrotation = self.cfgparser["OPTION"]["DATASET_LABEL_ROTATION"]
        except:
            pass
        try:
            rowskip = self.cfgparser["OPTION"]["DATA_IMPORT_SKIP_ROW_NUMBER"]
        except:
            pass
        try:
            show_median = self.cfgparser["OPTION"]["PLOT_SHOW_MEDIAN"]
        except:
            pass
        try:
            median_fontsize = self.cfgparser["OPTION"]["MEDIAN_FONT_SIZE"]
        except:
            pass

        # Handle data type
        try:
            dataset_labelrotation = int(dataset_labelrotation)
        except:
            dataset_labelrotation = 0

        if show_median == 'None':
            show_median = False
        elif show_median == 'True':
            show_median = True
        else:
            show_median = False

        if not median_fontsize == None:
            median_fontsize = 6  # default value
        elif median_fontsize.isnumeric():
            median_fontsize = int(median_fontsize)
            if not median_fontsize in (3, 10):
                median_fontsize = 6  # default value
        else:
            median_fontsize = 6

        if type(rowskip) == str:
            rowskip = rowskip.split(' ')
            # Filter out non-numeric string
            rowskip = [num for num in rowskip if num.isnumeric()]
            rowskip = list(map(int, rowskip))
            rowskip = [row for row in rowskip if row >= 0]
            if len(rowskip) == 0:
                rowskip = None
        else:
            rowskip = None

        # save to Setting object
        Setting.OPTS_PLOTCONFIG_DATASET_LABEL_ROTATION = dataset_labelrotation
        Setting.OPTS_PLOTCONFIG_SHOW_MEDIAN = show_median  # must be boolean
        Setting.OPTS_MEDIAN_FONT_SIZE = median_fontsize
        Setting.OPTS_DATACONFIG_IMPORT_SKIP_ROW = rowskip  # must be None or list integer

    def saveSetting(
            self,
            plotconfig_datasetLabelRotation: int,
            plotconfig_showMedian: bool,
            plotconfig_medianFontSize: int,
            dataconfig_importSkipRows: List[int]
    ) -> None:
        # argument validation
        if type(plotconfig_datasetLabelRotation) != int:
            plotconfig_datasetLabelRotation = 0
        if not plotconfig_datasetLabelRotation in [0, 45, 90]:
            plotconfig_datasetLabelRotation = 0

        if type(plotconfig_showMedian) != bool:
            plotconfig_showMedian = False

        if type(plotconfig_medianFontSize) != int:
            plotconfig_medianFontSize = 6

        if type(dataconfig_importSkipRows) != list:
            dataconfig_importSkipRows = None
        else:
            dataconfig_importSkipRows = [
                num for num in dataconfig_importSkipRows if type(num) == int]

        Setting.OPTS_PLOTCONFIG_DATASET_LABEL_ROTATION = plotconfig_datasetLabelRotation
        Setting.OPTS_PLOTCONFIG_SHOW_MEDIAN = plotconfig_showMedian
        Setting.OPTS_MEDIAN_FONT_SIZE = plotconfig_medianFontSize
        Setting.OPTS_DATACONFIG_IMPORT_SKIP_ROW = dataconfig_importSkipRows

        self.cfgparser["OPTION"]["DATASET_LABEL_ROTATION"] = str(
            plotconfig_datasetLabelRotation)
        self.cfgparser["OPTION"]["PLOT_SHOW_MEDIAN"] = str(
            plotconfig_showMedian)
        self.cfgparser["OPTION"]["MEDIAN_FONT_SIZE"] = str(
            plotconfig_medianFontSize)

        if dataconfig_importSkipRows == None:
            self.cfgparser["OPTION"]["DATA_IMPORT_SKIP_ROW_NUMBER"] = str(
                'None')
        else:
            self.cfgparser["OPTION"]["DATA_IMPORT_SKIP_ROW_NUMBER"] = ' '.join(
                map(str, dataconfig_importSkipRows))

        with open("preference.ini", "w") as configfile:
            self.cfgparser.write(configfile)
            configfile.close()
