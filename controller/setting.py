from __future__ import annotations
import os
from PyQt6.QtCore import QSettings
from typing import List


class Setting:

    ROOTDIR = os.path.abspath('')
    FILE_EXT: str = 'csv'
    LOCAL_FIGURECONFIG_FILENAME: str = 'Plot Config.csv'
    
    INPUT_DIR = os.path.abspath("Input")
    OUTPUT_DIR = os.path.abspath("Output")
    LIST_FIGURE_IMAGES: List[str] = []
    DATA_ROW_TO_SKIPREAD: List[int] = [1, 2]

    OPTS_LOCAL_FILENAME = 'preference.ini'
    OPTS_DATASET_LABEL_ROTATION: int = 0 # Rotation of Dataset label on Plot Figure. # 0: no rotation
    OPTS_SHOW_MEDIAN_LINE: bool = False
    OPTS_NUMBER_OF_ROW_SKIP_IMPORT_DATA: int = 0

    WIDTH_HEIGHT_RATIO: float = 1.48 # following Minitab software Boxplot style
    MAX_WIDTH: float = 10.5
    MAX_HEIGHT: float = 4.65
    DATASET_NAME_LIST_IN_PLOT: List[str] = []

    def __init__(self):
        INI_FORMAT = QSettings.Format.IniFormat
        INI_PARENT = None

        # INI file does not contain keys, then initialize it
        try:
            self.pref = QSettings(self.OPTS_LOCAL_FILENAME, INI_FORMAT, INI_PARENT)
            if not self.pref.contains('PREFERENCE/DATASET_LABEL_ROTATION'):
                pass
        except Exception as e:
            return
    
    def update(self):
        pass
        # Update the plot item in local database of setting to class object

    def setINI_DATASET_LABEL_ROTATION(self, val: str)->None:
        # self.pref.setValue(self.'DATASET_LABEL_ROTATION', val)
        # self.saved_settings.sync()
