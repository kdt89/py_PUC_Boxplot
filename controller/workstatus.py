import glob

    # Attributes
class Status:
    # Variables
    input_status_ready = False
    setting_update_ok = False
    error_message = ""
    input_status_list_files = []


    @staticmethod
    def clear_error_message():

        Status.error_message = ""
    

    @staticmethod
    def update_list_input_files(input_path: str, file_ext: str):

        Status.input_status_list_files = [file for file in glob.glob(input_path + './*.{}'.format(file_ext))]
    # def get_list_import_files(self) ->list:
    #     return self.list_import_files