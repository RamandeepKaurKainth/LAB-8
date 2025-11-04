from library_item import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title: str, call_number: str, release_date: str, region_code: str, num_of_copies: int = 1, **kwargs):
        super().__init__(title=title, call_number=call_number, num_of_copies=num_of_copies, **kwargs)
        self.release_date = release_date
        self.region_code = region_code

    def __str__(self) -> str:
        return (
            f"[DVD]\n"
            f"Title: {self.title}\n"
            f"Call Number: {self.call_number}\n"
            f"Release Date: {self.release_date}\n"
            f"Region Code: {self.region_code}\n"
            f"Available Copies: {self.num_of_copies}"
        )
