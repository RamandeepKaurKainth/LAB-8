import difflib
from typing import List, Iterable
from library_item import LibraryItem

class Catalogue:
    def __init__(self):
        self.items: List[LibraryItem] = []

    def add_item(self, item: LibraryItem):
        if any(existing.call_number == item.call_number for existing in self.items):
            print(f"Item with call number {item.call_number} already exists.")
            return
        self.items.append(item)
        print(f"Added: {item.title} (Call# {item.call_number})")

    def remove_item(self, call_number: str):
        before = len(self.items)
        self.items = [i for i in self.items if i.call_number != call_number]
        if len(self.items) < before:
            print(f"Item with call number {call_number} removed.")
        else:
            print(f"Item with call number {call_number} not found.")

    def find_by_title(self, query: str) -> Iterable[LibraryItem]:
        hits = [i for i in self.items if query.lower() in i.title.lower()]
        if hits:
            return hits

        titles = [i.title for i in self.items]
        suggestions = difflib.get_close_matches(query, titles)
        if suggestions:
            print(f"Not found. Did you mean: {', '.join(suggestions)}?")
        else:
            print("No matches.")
        return []

    def display_all(self):
        if not self.items:
            print("No items in catalogue.")
            return
        for item in self.items:
            print("\n" + str(item))
