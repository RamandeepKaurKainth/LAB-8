from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title: str, call_number: str, num_of_copies: int = 1, **kwargs):
        self._title = title
        self._call_number = call_number
        self._num_of_copies = int(num_of_copies)

    @property
    def title(self) -> str:
        return self._title

    @property
    def call_number(self) -> str:
        return self._call_number

    @property
    def num_of_copies(self) -> int:
        return self._num_of_copies

    @num_of_copies.setter
    def num_of_copies(self, value: int):
        self._num_of_copies = max(0, int(value))

    @property
    def available(self) -> bool:
        return self._num_of_copies > 0

    def check_out(self) -> bool:
        if self.available:
            self._num_of_copies -= 1
            return True
        return False

    def return_one(self):
        self._num_of_copies += 1

    @abstractmethod
    def __str__(self) -> str:
        ...
