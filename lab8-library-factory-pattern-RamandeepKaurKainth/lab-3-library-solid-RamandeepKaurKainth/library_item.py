from abc import ABC, abstractmethod

class LibraryItem(ABC): 
    def __init__(self, title, call_number):
        self.title = title
        self.call_number = call_number

    @abstractmethod
    def __str__(self):
        pass
