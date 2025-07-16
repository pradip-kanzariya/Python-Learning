# 5. Data Structures

# Practice Task - 1 | Create a phonebook using dictionaries.
def my_phonebook():
    """
    Contact manager - Gives different functionalities like Create, Update, Delete, Show created contact, Search created contact.
    """
    phone_book = {}
    while True:                                                         # Using 'while' loop for script continous running.
        print("\nWelcome to my phonebook.")
        print("\n--- Phonebook Menu ---")
        print("1. : Add contact")
        print("2. : View All Contacts")
        print("3. : Update contact")
        print("4. : Search Contact")
        print("5. : Delete Contact")
        print("6. : Exit")

        user_input = input("\nEnter your choice (1-6): ").strip()       # User input for check different conditions.

        if user_input == "1":
            print("--- Create Contact ---")
            name_input = input("Enter name : ").strip()
            if name_input in phone_book:
                print(f"Contact Exists  {name_input} : {phone_book[name_input]}")
            else:
                contact_input = input("Enter Number : ").strip()
                phone_book[name_input] = contact_input                          # For add new item in dictionary.
                print(f"New contact '{name_input}' is created successfuly.")

        elif user_input == "2":
            print("--- Contacts ---")
            if phone_book:
                for name, contact in phone_book.items():      # Using dictionary '.items()' method in for loop to get each key, value.
                    print(f"{name} : {contact}")
            else:
                print("Contact not exists.")
            print("--------------------")

        elif user_input == "3":
            print("--- Update Contact ---")
            update_name = input("Enter name you want to update : ").strip()
            if update_name in phone_book:
                update_number = input("Enter new number : ").strip()
                phone_book[update_name] = update_number
                print(f"Contact '{update_name}' updated successfuly.")
            else:
                print("Contact not exists.")

        elif user_input == "4":
            print("--- Search Contact ---")
            search_name = input("Enter search name : ").strip()
            if search_name in phone_book:
                print(f"{search_name} : {phone_book[search_name]}")
            else:
                print("Contact not exists.")

        elif user_input == "5":
            print("--- Delete Contact ---")
            delete_name = input("Enter delete name : ").strip()
            if delete_name in phone_book:
                phone_book.pop(delete_name)                  # Using dictionary '.pop()' method to remove item from dictionary.
                print(f"Contact '{delete_name}' deleted successfuly.")
            else:
                print("Contact not exists.")

        elif user_input == "6":
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


my_phonebook()
