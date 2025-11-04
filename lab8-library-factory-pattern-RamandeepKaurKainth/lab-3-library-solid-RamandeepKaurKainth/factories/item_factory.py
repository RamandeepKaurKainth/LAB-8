from abc import ABC, abstractmethod
from typing import Any
from library_item import LibraryItem


class ItemFactory(ABC):
    @abstractmethod
    def create_item(self) -> LibraryItem:
        """Subclasses must implement item creation."""
        pass

    # Helper to collect inputs with labels and optional type casting
    def _prompt(self, label: str, caster=str, default=None) -> Any:
        """Safely prompt the user and cast to the desired type."""
        while True:
            raw = input(f"{label}: ").strip()
            if not raw and default is not None:
                return default
            try:
                return caster(raw)
            except (ValueError, TypeError):
                print(f"Invalid input for {label}. Please try again.")
