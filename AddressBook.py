'''
@Author: Rahul 
@Date: 2024-09-14
@Last Modified by: Rahul 
@Last Modified time: 2024-09-14
@Title: Employee wages - Python program to perform phonebook operation.
'''

from Mylog import logger_init
import re

log = logger_init("UC_8")

class Contact:
    def __init__(self, firstName, lastName, address, city, state, zip, phone, email):
        
        if not re.match(r"^[0-9]{6}$", zip):
            raise ValueError("Invalid ZIP code. It should be exactly 6 digits.")
        if not re.match(r"^[0-9]{10}$", phone):
            raise ValueError("Invalid phone number. It should be exactly 10 digits.")
        email_regex = r'^[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}(?:\.[a-zA-Z]{2,3})?$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email address format.")
        
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        for existing_contact in self.contacts:
            if contact.firstName == existing_contact.firstName and contact.lastName == existing_contact.lastName:
                log.info("Contact already present!")
                return f"{contact.firstName} {contact.lastName} is already present in the address book."
        self.contacts.append(contact)
        log.info("Contact added to address book!")
        return f"{contact.firstName} is added successfully."

    def edit_contact(self, firstName, new_values):
        for contact in self.contacts:
            if contact.firstName == firstName:
                
                if new_values[4] and not re.match(r"^[0-9]{6}$", new_values[4]):
                    raise ValueError("New ZIP code must be exactly 6 digits.")
                if new_values[5] and not re.match(r"^[0-9]{10}$", new_values[5]):
                    raise ValueError("New phone number must be exactly 10 digits.")
                if new_values[6] and not re.match(r'^[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}(?:\.[a-zA-Z]{2,3})?$', new_values[6]):
                    raise ValueError("New email address format is invalid.")
                
                contact.lastName = new_values[0] or contact.lastName
                contact.address = new_values[1] or contact.address
                contact.city = new_values[2] or contact.city
                contact.state = new_values[3] or contact.state
                contact.zip = new_values[4] or contact.zip
                contact.phone = new_values[5] or contact.phone
                contact.email = new_values[6] or contact.email
                log.info("Contact updated!")
                return f"{contact.firstName}'s data updated."
        log.info("Contact not found!")
        return f"{firstName} not found in the address book."

    def delete_contact(self, firstName):
        for contact in self.contacts:
            if contact.firstName == firstName:
                self.contacts.remove(contact)
                log.info("Contact deleted!")
                return f"{firstName} contact deleted."
        log.info("Contact not found!")
        return f"{firstName} not found in the address book."

    def display_all_contacts(self):
        if not self.contacts:
            return "Address book is empty."
        return self.contacts

class AddressBookManager:
    def __init__(self):
        self.addressBooks = {}

    def create_address_book(self, addressBook_name):
        if addressBook_name not in self.addressBooks:
            self.addressBooks[addressBook_name] = AddressBook()
            log.info("Address book created!")
            return f"Address book '{addressBook_name}' created successfully."
        log.info("Address book already exists!")
        return f"Address book '{addressBook_name}' already exists."

    def get_address_book(self, addressBook_name):
        return self.addressBooks.get(addressBook_name)

    def display_all_address_books(self):
        log.info("Displaying all address books.")
        return list(self.addressBooks.keys())

    def search_person_by_city_or_state(self, search_option, search_value):
        result = {}
        for addressBook_name, addressBook in self.addressBooks.items():
            result[addressBook_name] = []
            for contact in addressBook.contacts:
                if (search_option == 1 and contact.city.lower() == search_value.lower()) or \
                   (search_option == 2 and contact.state.lower() == search_value.lower()):
                    result[addressBook_name].append(contact)
        return result

def main():
    manager = AddressBookManager()
    print("-" * 35 + "\n| Welcome to Address Book Program |\n" + "-" * 35 + "\n")

    while True:
        option = int(input("Enter:\n"
                           " 1. Add new Address Book\n"
                           " 2. Add Contact\n"
                           " 3. Edit Contact\n"
                           " 4. Delete Contact\n"
                           " 5. Display all contacts in Address Book\n"
                           " 6. Search person by city or state\n"
                           " 7. Exit\n"
                           "Option: "))

        if option == 1:
            addressBook_name = input("Enter the name of the new address book: ")
            print("-" * 50 + "\n" + manager.create_address_book(addressBook_name) + "\n" + "-" * 50)

        elif option == 2:
            print(manager.display_all_address_books())
            addressBook_name = input("Enter the Address Book name to add a contact: ")

            contact_data = [
                "Enter your First Name (eg:'Rahul'): ",
                "Enter your Last Name (eg: J): ",
                "Enter your Address (eg: '176A Teachers colony' ): ",
                "Enter your City (eg: 'Erode'): ",
                "Enter your State (eg: 'Tamil Nadu') ",
                "Enter the Zip code (enter 6 digits): ",
                "Enter your phone number (enter 10 digits): ",
                "Enter your valid email (eg : 'abc123@gmail.com): "
            ]

            user_data = [input(prompt) for prompt in contact_data]
            
            try:
                contact = Contact(*user_data)
                addressBook = manager.get_address_book(addressBook_name)
                
                if addressBook:
                    print("-" * 50 + "\n" + addressBook.add_contact(contact) + "\n" + "-" * 50)
                    
                else:
                    print("Address Book not found.")
            except ValueError as e:
                print(f"Error: {e}")

        elif option == 3:
            print(manager.display_all_address_books())
            addressBook_name = input("Enter the Address Book name to edit a contact: ")
            firstName = input("Enter the first name of the contact to edit: ")

            prompts = [
                "Enter new Last Name: ",
                "Enter new Address: ",
                "Enter new City: ",
                "Enter new State: ",
                "Enter new Zip Code: ",
                "Enter new Phone Number: ",
                "Enter new Email: "
            ]
            new_values = [input(prompt) for prompt in prompts]

            addressBook = manager.get_address_book(addressBook_name)
            if addressBook:
                try:
                    print("-" * 50 + "\n" + addressBook.edit_contact(firstName, new_values) + "\n" + "-" * 50)
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Address Book not found.")

        elif option == 4:
            print(manager.display_all_address_books())
            addressBook_name = input("Enter the Address Book name to delete a contact: ")
            firstName = input("Enter the first name of the contact to delete: ")

            addressBook = manager.get_address_book(addressBook_name)
            if addressBook:
                print("-" * 50 + "\n" + addressBook.delete_contact(firstName) + "\n" + "-" * 50)
            else:
                print("Address Book not found.")

        elif option == 5:
            print(manager.display_all_address_books())
            addressBook_name = input("Enter the Address Book name to display all contacts: ")

            addressBook = manager.get_address_book(addressBook_name)
            if addressBook:
                contacts = addressBook.display_all_contacts()
                if isinstance(contacts, str):
                    print(contacts)
                else:
                    for contact in contacts:
                        print(f"First Name: {contact.firstName}, Last Name: {contact.lastName}, City: {contact.city}, State: {contact.state}, Email: {contact.email}")
            else:
                print("Address Book not found.")

        elif option == 6:
            search_option = int(input("Enter 1 to search by 'City', 2 to search by 'State': "))
            search_value = input("Enter the value to search: ")
            results = manager.search_person_by_city_or_state(search_option, search_value)

            if results:
                for addressBook_name, contacts in results.items():
                    if contacts:
                        print(f"Address Book: {addressBook_name}")
                        for contact in contacts:
                            print(f"First Name: {contact.firstName}, City: {contact.city}, State: {contact.state}")
                    else:
                        print(f"No matching contacts in {addressBook_name}.")
            else:
                print("No matching contacts found.")

        elif option == 7:
            print("Program exited.")
            return

if __name__ == "__main__":
    main()
