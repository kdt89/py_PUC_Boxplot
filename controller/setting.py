import os
import pandas as pd


class Setting:

    rootdir = os.path.abspath('')
    file_ext = 'csv'
    setting_filename = 'setting_plot.csv'
    input_dirname = "Input"
    output_dirname = "Output"
    data_row_to_skipread = [1, 2]


    def __init__(self):
        self.plot_list = pd.DataFrame()
        self.reading_cols = None
        self.input_dir = os.path.abspath(self.input_dirname)
        self.output_dir = os.path.abspath(self.output_dirname)


    def update(self):

        self.plot_list = pd.read_csv(self.setting_filename, index_col=None, sep=',', header=0)
        self.reading_cols = self.plot_list['Item']