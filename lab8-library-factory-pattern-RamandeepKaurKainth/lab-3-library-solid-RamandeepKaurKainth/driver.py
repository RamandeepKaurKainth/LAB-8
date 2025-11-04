from book import Book
from library import Library

def main():
    my_library = Library()

    print("Welcome to the Library Management System")

    # Adding books to the library
    book1 = Book("The Catcher in the Rye", "C123", "J.D. Salinger", 3)
    book2 = Book("To Kill a Mockingbird", "M456", "Harper Lee", 5)

    for _ in range(3):
        print("\nAdd a new library item:")
        my_library.catalogue.add_item()

    # Display available books
    print("\nAvailable item in the library:")
    my_library.display_available_books()

    # Find books by title
    search_title = input("\nEnter book title to search: ")
    found_books = my_library.catalogue.find_books(search_title)
    if found_books:
        print("\nItems found:")
        for item in found_books:
            print(item)

    # Check out a book
    call_number = input("\nEnter call number of the book to check out: ")   
    my_library.check_out(call_number)
    my_library.display_available_books()

    # Return a book
    call_number = input("\nEnter call number of the book to return: ")
    my_library.return_item(call_number)
    my_library.display_available_books()

    # Remove a book
    call_number = input("\nEnter call number of the book to remove: ")
    my_library.remove_item(call_number)
    my_library.display_available_books()

if __name__ == "__main__":
    main()
