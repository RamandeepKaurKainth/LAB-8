import difflib
from book import Book
from dvd import DVD
from journal import Journal
from library_item import LibraryItem
from library_item_generator import LibraryItemGenerator

class Catalogue:
    def __init__(self):
        self.books: list[LibraryItem] = []

    def find_books(self, string):
        found_books = []
        for book in self.books:
            if string.lower() in book.title.lower():
                found_books.append(book)
        if not found_books:
            similar_titles = difflib.get_close_matches(string, [book.title for book in self.books])
            if similar_titles:
                print(f"Book not found. Did you mean one of these titles? {', '.join(similar_titles)}")
            else:
                print("Book not found.")
        return found_books

    def add_book(self, book: LibraryItem):
        if book not in self.books:
            self.books.append(book)
            print(f"Added: {book.title} (Call# {book.call_number})")
        else:
            print(f"Book with call number {book.call_number} already exists.")

    def remove_book(self, call_number):
        for book in self.books:
            if book.call_number == call_number:
                self.books.remove(book)
                print(f"Book with call number {call_number} removed.")
                return
        print(f"Book with call number {call_number} not found.")

    def add_item(self):
        item = LibraryItemGenerator.create_item()
        if item:
            if item not in self.books:
                self.books.append(item)
                print(f"Added: {item.title} (Call# {item.call_number})")
            else:
                
                print(f"Item with call number {item.call_number} already exists.")