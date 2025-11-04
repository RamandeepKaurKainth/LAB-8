from catalogue import Catalogue

class Library:
    def __init__(self):
        self.catalogue = Catalogue()

    def check_out(self, call_number):
        for book in self.catalogue.books:
            if book.call_number == call_number:
                if book.check_availability():
                    book.num_of_copies -= 1
                    print(f"Book with call number {call_number} checked out successfully.")
                    return
                else:
                    print(f"Book with call number {call_number} is not available for check out.")
                    return
        print(f"Book with call number {call_number} not found.")

    def return_book(self, call_number):
        for book in self.catalogue.books:
            if book.call_number == call_number:
                book.num_of_copies += 1
                print(f"Book with call number {call_number} returned successfully.")
                return
        print(f"Book with call number {call_number} not found.")

    def display_available_books(self):
        if not self.catalogue.books:
            print("No books available.")
        else:
            for book in self.catalogue.books:
                print("\n" + str(book))

