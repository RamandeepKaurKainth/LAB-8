from library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title: str, call_number: str, author: str, num_of_copies: int = 1, **kwargs):
        super().__init__(title=title, call_number=call_number, num_of_copies=num_of_copies, **kwargs)
        self.author = author

    def __str__(self) -> str:
        return (
            f"[Book]\n"
            f"Title: {self.title}\n"
            f"Call Number: {self.call_number}\n"
            f"Author: {self.author}\n"
            f"Available Copies: {self.num_of_copies}"
        )
