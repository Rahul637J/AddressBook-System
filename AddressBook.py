'''

@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operation.  

'''

import pickle
import os

from Mylog import logger_init

log = logger_init("UC_13")

class Contact:
    def __init__(self, firstName, lastName, address, city, state, zip, phone, email):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """
        Description:
            Adds a new contact to the address book.
        
        Parameters:
            contact (Contact): A contact object containing contact details like name, address, phone, and email.
        
        Return Type:
            str: A message indicating whether the contact was added or already exists.
        """
        for existing_contact in self.contacts:
            if contact.firstName == existing_contact.firstName and contact.lastName == existing_contact.lastName:
                log.info(f"Attempted to add duplicate contact: {contact.firstName} {contact.lastName}")
                return f"{contact.firstName} {contact.lastName} is already present."

        self.contacts.append(contact)
        log.info(f"Added contact: {contact.firstName} {contact.lastName}")
        return f"{contact.firstName} is added successfully."

    def edit_contact(self, firstName, new_values):
        """
        Description:
            Edits an existing contact's details in the address book based on the first name provided.
        
        Parameters:
            firstName (str): The first name of the contact to be edited.
            new_values (list): A list containing the new values for the contact fields.
        
        Return Type:
            str: A message indicating that the contact information has been updated.
        """
        for contact in self.contacts:
            if firstName == contact.firstName:
                contact.lastName = new_values[0] or contact.lastName
                contact.address = new_values[1] or contact.address
                contact.city = new_values[2] or contact.city
                contact.state = new_values[3] or contact.state
                contact.zip = new_values[4] or contact.zip
                contact.phone = new_values[5] or contact.phone
                contact.email = new_values[6] or contact.email
                log.info(f"Updated contact: {contact.firstName} {contact.lastName}")
                return f"{contact.firstName} Data Updated!"
        
        log.warning(f"Contact with first name {firstName} not found for edit.")
        return f"{firstName} is not present in the AddressBook."

    def delete_contact(self, firstName):
        """
        Description:
            Delete an existing contact's details in the address book based on the first name provided.
        
        Parameters:
            firstName (str): The first name of the contact to be deleted.
        
        Return Type:
            str: A message indicating that the contact has been deleted.
        """
        for contact in self.contacts:
            if firstName == contact.firstName:
                self.contacts.remove(contact)
                log.info(f"Deleted contact: {firstName}")
                return f"{firstName} contact is deleted."
        
        log.warning(f"Contact with first name {firstName} not found for deletion.")
        return f"{firstName} not found in the AddressBook."

    def display_all_contacts(self, search_option):
        """
        Description:
            Display all contact's details in the address book based on sorting option.
        
        Parameters:
            search_option (int): Option to sort contacts (1 - First Name, 2 - City, 3 - State).
        
        Return Type:
            list: Sorted list of contact objects based on the given option.
        """
        if search_option == 1:
            return sorted(self.contacts, key=lambda contact: contact.firstName)
        elif search_option == 2:
            return sorted(self.contacts, key=lambda contact: contact.city)
        elif search_option == 3:
            return sorted(self.contacts, key=lambda contact: contact.state)
        else:
            log.warning(f"Invalid search option: {search_option}")
            return []
        

class AddressBookManager:
    def __init__(self):
        self.address_books = {}

    def create_address_book(self, address_book_name):
        if address_book_name not in self.address_books:
            self.address_books[address_book_name] = AddressBook()
            return f"{address_book_name} has been created successfully!"
        return f"{address_book_name} already exists!"

    def add_contact(self, address_book_name, contact):
        if address_book_name not in self.address_books:
            return f"{address_book_name} does not exist!"
        return self.address_books[address_book_name].add_contact(contact)

    def edit_contact(self, address_book_name, first_name, new_values):
        if address_book_name not in self.address_books:
            return f"{address_book_name} does not exist!"
        return self.address_books[address_book_name].edit_contact(first_name, new_values)

    def delete_contact(self, address_book_name, first_name):
        if address_book_name not in self.address_books:
            return f"{address_book_name} does not exist!"
        return self.address_books[address_book_name].delete_contact(first_name)

    def display_all_address_books(self):
        return list(self.address_books.keys())

    def display_all_contacts(self, address_book_name, search_option):
        if address_book_name not in self.address_books:
            return f"{address_book_name} does not exist!"
        return self.address_books[address_book_name].display_all_contacts(search_option)

    def search_person_by_city_or_state(self, search_option, search_value):
        person = {}
        for address_book_name, address_book in self.address_books.items():
            result = address_book.search_person_by_city_or_state(search_option, search_value)
            if result:
                person[address_book_name] = result
        return person

    def get_count_of_person_by_city_or_state(self, search_option, search_value):
        count = 0
        for address_book in self.address_books.values():
            count += address_book.get_count_of_person_by_city_or_state(search_option, search_value)
        return count

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.address_books, file)
        return f"Data saved to {filename} successfully."

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            return f"{filename} does not exist!"
        with open(filename, 'rb') as file:
            self.address_books = pickle.load(file)
        return f"Data loaded from {filename} successfully."
    
    
def main():
    manager = AddressBookManager()

    while True:
        print("\nAddress Book Manager")
        print("1. Create Address Book")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Display All Address Books")
        print("7. Search Person by City/State")
        print("8. Get Count of Person by City/State")
        print("9. Save Address Book to File")
        print("10. Load Address Book from File")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter address book name: ")
            print(manager.create_address_book(name))
        
        elif choice == '2':
            address_book_name = input("Enter address book name: ")
            if address_book_name not in manager.address_books:
                print(f"Address book {address_book_name} does not exist.")
                continue
            
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            address = input("Enter address: ")
            city = input("Enter city: ")
            state = input("Enter state: ")
            zip = input("Enter zip: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")

            contact = Contact(firstName, lastName, address, city, state, zip, phone, email)
            print(manager.add_contact(address_book_name, contact))
        
        elif choice == '3':
            address_book_name = input("Enter address book name: ")
            if address_book_name not in manager.address_books:
                print(f"Address book {address_book_name} does not exist.")
                continue

            firstName = input("Enter the first name of the contact to edit: ")
            new_values = [
                input("Enter new last name (leave blank to keep unchanged): "),
                input("Enter new address (leave blank to keep unchanged): "),
                input("Enter new city (leave blank to keep unchanged): "),
                input("Enter new state (leave blank to keep unchanged): "),
                input("Enter new zip (leave blank to keep unchanged): "),
                input("Enter new phone (leave blank to keep unchanged): "),
                input("Enter new email (leave blank to keep unchanged): ")
            ]
            print(manager.edit_contact(address_book_name, firstName, new_values))
        
        elif choice == '4':
            address_book_name = input("Enter address book name: ")
            if address_book_name not in manager.address_books:
                print(f"Address book {address_book_name} does not exist.")
                continue

            firstName = input("Enter the first name of the contact to delete: ")
            print(manager.delete_contact(address_book_name, firstName))
        
        elif choice == '5':
            address_book_name = input("Enter address book name: ")
            if address_book_name not in manager.address_books:
                print(f"Address book {address_book_name} does not exist.")
                continue

            print("Sort by: 1. First Name 2. City 3. State")
            search_option = int(input("Enter your choice: "))
            contacts = manager.display_all_contacts(address_book_name, search_option)
            for contact in contacts:
                print(contact)
        
        elif choice == '6':
            print("Address Books:")
            books = manager.display_all_address_books()
            for book in books:
                print(book)
        
        elif choice == '7':
            print("Search by: 1. City 2. State")
            search_option = int(input("Enter your choice: "))
            search_value = input("Enter city or state: ")
            results = manager.search_person_by_city_or_state(search_option, search_value)
            for book, contacts in results.items():
                print(f"Address Book: {book}")
                for contact in contacts:
                    print(contact)
        
        elif choice == '8':
            print("Search by: 1. City 2. State")
            search_option = int(input("Enter your choice: "))
            search_value = input("Enter city or state: ")
            count = manager.get_count_of_person_by_city_or_state(search_option, search_value)
            print(f"Count of contacts: {count}")

        elif choice == '9':
            filename = input("Enter filename to save data: ")
            print(manager.save_to_file(filename))
        
        elif choice == '10':
            filename = input("Enter filename to load data from: ")
            print(manager.load_from_file(filename))

        elif choice == '11':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again!!!.")

if __name__ == "__main__":
    main()
