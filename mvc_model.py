from typing import List
import pandas as pd
from util.observer import Observer # OBSERVER DESIGN PATTERN
from model.csvdata import CSV_Data
from pandas import DataFrame

class Model:

    _observers: List[Observer] = []
    _status = ""

    def __init__(self):

        self.database = CSV_Data()

    '''
    Define normal class method
    '''

    '''
    Define inherited method from Observer class
    '''    
    def attach(self, observer: Observer) -> None:
       self._observers.append(observer)

    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)    


    """
    Trigger an update in each subscriber.
    """
    def notify(self) -> None:

        for observer in self._observers:
            observer.update(self)


# class PlotList:

#     pass

#     class PlotItem:

#         name = ""
#         upper_limit = 0
#         lower_limit = 0



    # def import_csv_file(self, csv_filepath: str, reading_col, reading_skip_rows: list):

    #     # Checking csv_filepath direct to a file or not
    #     if len(reading_col) == 0:
    #         reading_col = None

    #     if len(reading_skip_rows) == 0:
    #         reading_skip_rows = None
            
    #     df = pd.read_csv(csv_filepath, index_col=None, 
    #                      sep=',', header=0, 
    #                      usecols=reading_col, skiprows=reading_skip_rows)

    #     # Remove duplicated rows
    #     df = df.drop_duplicates()
    #     # Merging data frames into one frame
    #     try:
    #         if not df.empty:
    #             self.database = pd.concat([self.database, df], axis=0, ignore_index=True)

    #     except:
    #         return None

