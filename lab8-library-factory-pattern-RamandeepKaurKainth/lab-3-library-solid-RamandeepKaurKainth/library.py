from catalogue import Catalogue

class Library:
    def __init__(self):
        self.catalogue = Catalogue()

    def check_out(self, call_number: str):
        for item in self.catalogue.items:
            if item.call_number == call_number:
                if item.check_out():
                    print(f"{call_number} checked out successfully.")
                else:
                    print(f"{call_number} is not available for check out.")
                return
        print(f"{call_number} not found.")

    def return_item(self, call_number: str):
        for item in self.catalogue.items:
            if item.call_number == call_number:
                item.return_one()
                print(f"{call_number} returned successfully.")
                return
        print(f"{call_number} not found.")

    def display_available(self):
        any_printed = False
        for item in self.catalogue.items:
            if item.available:
                any_printed = True
                print("\n" + str(item))
        if not any_printed:
            print("No available items.")
