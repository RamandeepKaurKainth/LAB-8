from library_item import LibraryItem

class Journal(LibraryItem):
    def __init__(self, title: str, call_number: str, author: str, issue_number: str, publisher: str, num_of_copies: int = 1, **kwargs):
        super().__init__(title=title, call_number=call_number, num_of_copies=num_of_copies, **kwargs)
        self.author = author
        self.issue_number = issue_number
        self.publisher = publisher

    def __str__(self) -> str:
        return (
            f"[Journal]\n"
            f"Title: {self.title}\n"
            f"Call Number: {self.call_number}\n"
            f"Author: {self.author}\n"
            f"Issue Number: {self.issue_number}\n"
            f"Publisher: {self.publisher}\n"
            f"Available Copies: {self.num_of_copies}"
        )
