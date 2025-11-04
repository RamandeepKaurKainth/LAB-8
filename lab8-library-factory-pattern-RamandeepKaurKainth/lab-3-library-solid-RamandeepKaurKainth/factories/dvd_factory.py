from .item_factory import ItemFactory
from dvd import DVD


class DVDFactory(ItemFactory):
    def create_item(self) -> DVD:
        title = self._prompt("DVD Title")
        call_number = self._prompt("Call Number")
        release_date = self._prompt("Release Date (YYYY-MM-DD)")
        region_code = self._prompt("Region Code")
        num_of_copies = self._prompt("Number of Copies", caster=int, default=1) # type: ignore

        return DVD(
            title=title,
            call_number=call_number,
            release_date=release_date,
            region_code=region_code,
            num_of_copies=num_of_copies
        )
