from library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, call_number, author, num_of_copies):
        super().__init__(title, call_number)
        self.author = author
        self.num_of_copies = num_of_copies

    def check_availability(self):
        return self.num_of_copies > 0

    def __str__(self):
        return f"Title: {self.title}\nCall Number: {self.call_number}\nAuthor: {self.author}\nAvailable Copies: {self.num_of_copies}"

