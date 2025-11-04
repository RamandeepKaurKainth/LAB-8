from library_item import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title, call_number, release_date, region_code, num_of_copies):
        super().__init__(title, call_number)
        self.release_date = release_date
        self.region_code = region_code
        self.num_of_copies = num_of_copies

    def check_availability(self):
        return self.num_of_copies > 0

    def __str__(self):
        return f"Title: {self.title}\nCall Number: {self.call_number}\nRelease Date: {self.release_date}\nRegion Code: {self.region_code}\nAvailable Copies: {self.num_of_copies}"