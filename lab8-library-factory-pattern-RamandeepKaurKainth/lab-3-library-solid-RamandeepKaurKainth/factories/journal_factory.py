from .item_factory import ItemFactory
from journal import Journal


class JournalFactory(ItemFactory):
    def create_item(self) -> Journal:
        title = self._prompt("Journal Title")
        call_number = self._prompt("Call Number")
        author = self._prompt("Author")
        issue_number = self._prompt("Issue Number")
        publisher = self._prompt("Publisher")
        num_of_copies = self._prompt("Number of Copies", caster=int, default=1) # type: ignore

        return Journal(
            title=title,
            call_number=call_number,
            author=author,
            issue_number=issue_number,
            publisher=publisher,
            num_of_copies=num_of_copies
        )
