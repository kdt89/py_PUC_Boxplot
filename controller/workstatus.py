from typing import List
import glob
import os
from controller.setting import Setting


class Status:

    INPUT_READY: bool = False
    SETTING_UPDATE_OK: bool = False
    ERR_MSG: str = ""
    DATA_INPUT_FILE_LIST: List[str] = []
    DETECTED_DATASET_NAME_LIST: List[str] = []


    @staticmethod
    def clear_error_message():
        Status.ERR_MSG = ""
    

    @staticmethod
    def update():
        Status.DATA_INPUT_FILE_LIST = [file for file in glob.glob(Setting.INPUT_DIR + './*.{}'.format(Setting.FILE_EXT))]
        Status.DETECTED_DATASET_NAME_LIST = [os.path.splitext(os.path.basename(file))[0] for file in Status.DATA_INPUT_FILE_LIST]