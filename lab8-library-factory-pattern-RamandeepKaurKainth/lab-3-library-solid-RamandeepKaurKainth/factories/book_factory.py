from .item_factory import ItemFactory
from book import Book


class BookFactory(ItemFactory):
    def create_item(self) -> Book:
        """Create a Book instance using user input."""
        title = self._prompt("Book Title")
        call_number = self._prompt("Call Number")
        author = self._prompt("Author")
        num_of_copies = self._prompt("Number of Copies", caster=int, default=1) # type: ignore
        return Book(
            title=title,
            call_number=call_number,
            author=author,
            num_of_copies=num_of_copies
        )
