import glob
from controller.setting import Setting


class Status:
    # Variables
    INPUT_READY = False
    SETTING_UPDATE_OK = False
    ERR_MSG = ""
    DATA_INPUT_FILE_LIST = []


    @staticmethod
    def clear_error_message():
        Status.ERR_MSG = ""
    

    @staticmethod
    def update():
        Status.DATA_INPUT_FILE_LIST = [file for file in glob.glob(Setting.INPUT_DIR + './*.{}'.format(Setting.FILE_EXT))]


    @staticmethod
    def getDatasetNameList():
        pass