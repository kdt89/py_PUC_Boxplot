

    # Attributes
class Status:
    # Variables
    input_ready = False
    setting_update_ok = False
    error_message = ""
    list_import_files = []

    def __init__(self):
        self.set_input_status(False)


    @staticmethod
    def scan_input_files(self):
        self.input_ready = False


    @staticmethod
    def input_ready(self) -> bool:
        return self.input_ready

    @staticmethod
    def set_input_status(status: bool) -> None:
        Status.input_ready = status


    


    @staticmethod
    def clear_error_message():
        Status.error_message = ""
    
    # def get_list_import_files(self) ->list:
    #     return self.list_import_files