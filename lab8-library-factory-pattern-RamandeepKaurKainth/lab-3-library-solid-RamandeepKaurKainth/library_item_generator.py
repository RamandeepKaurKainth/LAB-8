from book import Book
from dvd import DVD
from journal import Journal

class LibraryItemGenerator:

    @staticmethod
    def create_item():
        print("Select the type of library item to add:")
        print("1. Book")
        print("2. DVD")
        print("3. Journal")
        choice = input("Enter choice (1-3): ")

        if choice == '1':
            title = input("Enter book title: ")
            call_number = input("Enter call number: ")
            author = input("Enter author: ")
            num_of_copies = int(input("Enter number of copies: "))
            return Book(title, call_number, author, num_of_copies)
        elif choice == '2':
            title = input("Enter DVD title: ")
            call_number = input("Enter call number: ")
            release_date = input("Enter release date: ")
            region_code = int(input("Enter region code: "))
            num_of_copies = int(input("Enter number of copies: "))
            return DVD(title, call_number, release_date, region_code, num_of_copies)
        elif choice == '3':
            title = input("Enter journal title: ")
            call_number = input("Enter call number: ")
            author = input("Enter author: ")
            issue_number = input("Enter issue number: ")
            publisher = input("Enter publisher: ")
            num_of_copies = int(input("Enter number of copies: "))
            return Journal(title, call_number, author, issue_number, publisher, num_of_copies)
        else:
            print("Invalid choice.")
            return None