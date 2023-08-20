


    # Attributes
class WorkStatus:
    # Variables
    _input_ready = False
    list_import_files = []

    def __init__(self):
        self.set_input_status(False)


    def scan_input_files(self):

        self._input_ready = False


    def input_ready(self) -> bool:
        return self._input_ready


    def set_input_status(self, status: bool) -> None:
        self._input_ready = status


    def get_list_import_files(self) ->list:
        return self.list_import_files