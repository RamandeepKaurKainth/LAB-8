from library import Library
from menu import get_factory_registry, print_menu


def main():
    lib = Library()
    registry = get_factory_registry()  
    print("Welcome to the Library Management System (Factory Pattern)")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice in ("1", "2", "3"):
            label, factory = registry[choice]
            print(f"\nAdding a new {label}...")
            item = factory.create_item()
            lib.catalogue.add_item(item)

        elif choice == "4":
            q = input("Title contains: ").strip()
            hits = lib.catalogue.find_by_title(q)
            for h in hits:
                print("\n" + str(h))

        elif choice == "5":
            lib.display_available()

        elif choice == "6":
            cn = input("Call Number to check out: ").strip()
            lib.check_out(cn)

        elif choice == "7":
            cn = input("Call Number to return: ").strip()
            lib.return_item(cn)

        elif choice == "8":
            cn = input("Call Number to remove: ").strip()
            lib.catalogue.remove_item(cn)

        elif choice == "9":
            lib.catalogue.display_all()

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
