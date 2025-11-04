from factories.book_factory import BookFactory
from factories.dvd_factory import DVDFactory
from factories.journal_factory import JournalFactory


def get_factory_registry():
    """Return dictionary of available factories."""
    return {
        "1": ("Book", BookFactory()),
        "2": ("DVD", DVDFactory()),
        "3": ("Journal", JournalFactory()),
    }


def print_menu():
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Add DVD")
    print("3. Add Journal")
    print("4. Search by title")
    print("5. Display available items")
    print("6. Check out by call number")
    print("7. Return by call number")
    print("8. Remove by call number")
    print("9. Display all items")
    print("0. Quit")
