from typing import List

# OBSERVER DESIGN PATTERN
from util.observer import Observer 
from model.csv_database import CSV_Database


class Model:

    _observers: List[Observer] = []
    _status = ""

    def __init__(self):
        self.database = CSV_Database()

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


