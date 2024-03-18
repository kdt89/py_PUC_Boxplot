from model.csv_database import CSV_Database
from model.figureconfig import FigureConfigList


class Model:

    def __init__(self):
        self.database = CSV_Database()
        self.figureconfig_list = FigureConfigList()
