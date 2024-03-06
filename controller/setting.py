from __future__ import annotations
import os
from typing import List


class Setting:

    ROOTDIR = os.path.abspath('')
    FILE_EXT: str = 'csv'
    LOCAL_FIGURECONFIG_FILENAME: str = 'setting_plot.csv'
    
    INPUT_DIR = os.path.abspath("Input")
    OUTPUT_DIR = os.path.abspath("Output")
    LIST_FIGURE_IMAGES: List[str] = []
    DATA_ROW_TO_SKIPREAD: List[int] = [1, 2]

    WIDTH_HEIGHT_RATIO: float = 1.48 # following Minitab software Boxplot style
    MAX_WIDTH: float = 10.5
    MAX_HEIGHT: float = 4.65
    DATASET_NAME_LIST_IN_PLOT: List[str] = []

    @staticmethod
    def update():
        pass
        # Update the plot item in local database of setting to class object


