'''

@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operation.  

'''


import json
from Mylog import logger_init
import re


log = logger_init("UC_11")


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

    @staticmethod
    def validate_zip(zip_code):
        
        """
        Validates the ZIP code format.

        Parameters:
            zip_code (str): The ZIP code to validate.

        Return Type:
            bool: True if the ZIP code is in a valid format (6 digits), False otherwise.
        """
        
        return re.match(r"^\d{6}$", zip_code) is not None

    @staticmethod
    def validate_phone(phone_number):
        
        """
        Validates the phone number format.

        Parameters:
            phone_number (str): The phone number to validate.

        Return Type:
            bool: True if the phone number is in a valid format (10 digits), False otherwise.
        """
        
        return re.match(r"^\d{10}$", phone_number) is not None

    @staticmethod
    def validate_email(email_address):
        
        """
        Validates the email address format.

        Parameters:
            email_address (str): The email address to validate.

        Return Type:
            bool: True if the email address is in a valid format, False otherwise.
        """
        
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_address) is not None

    def to_dict(self):
        
        """
        Converts the contact to a dictionary format for serialization.

        Return Type:
            dict: A dictionary representation of the contact.
        """
        
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "phone": self.phone,
            "email": self.email
        }

    @staticmethod
    def from_dict(data):
        
        """
        Creates a contact instance from a dictionary.

        Parameters:
            data (dict): A dictionary representation of the contact.

        Return Type:
            Contact: A contact instance created from the dictionary.
        """
        
        return Contact(
            firstName=data["firstName"],
            lastName=data["lastName"],
            address=data["address"],
            city=data["city"],
            state=data["state"],
            zip=data["zip"],
            phone=data["phone"],
            email=data["email"]
        )

class AddressBook:
    def __init__(self):
       
        self.contacts = []

    def add_contact(self, contact):
        
        """
        Adds a new contact to the address book, ensuring no duplicates.

        Parameters:
            contact (Contact): The contact to add to the address book.

        Return Type:
            str: A message indicating whether the contact was added successfully or if it was a duplicate.
        """
        
        for existing_contact in self.contacts:
            if contact.firstName == existing_contact.firstName and contact.lastName == existing_contact.lastName:
                log.warning(f"Attempted to add duplicate contact: {contact.firstName} {contact.lastName}")
                return f"{contact.firstName} {contact.lastName} is already in the address book."
            
        self.contacts.append(contact)
        log.info(f"Contact added: {contact.firstName} {contact.lastName}")
        return f"{contact.firstName} {contact.lastName} added successfully."

    def edit_contact(self, firstName, new_values):
        
        """
        Edits an existing contact's details based on the provided first name and new values.

        Parameters:
            firstName (str): The first name of the contact to edit.
            new_values (list of str): A list of new values for the contact's details, with empty strings indicating no change.

        Return Type:
            str: A message indicating whether the contact was updated successfully or if it was not found.
        """
        
        for contact in self.contacts:
            if contact.firstName == firstName:
                log.info(f"Editing contact: {firstName}")
                contact.lastName = new_values[0] or contact.lastName
                contact.address = new_values[1] or contact.address
                contact.city = new_values[2] or contact.city
                contact.state = new_values[3] or contact.state
                new_zip = new_values[4] or contact.zip
                new_phone = new_values[5] or contact.phone
                new_email = new_values[6] or contact.email
                
                if new_zip and not Contact.validate_zip(new_zip):
                    return "Invalid ZIP code format."
                if new_phone and not Contact.validate_phone(new_phone):
                    return "Invalid phone number format."
                if new_email and not Contact.validate_email(new_email):
                    return "Invalid email address format."
                
                contact.zip = new_zip
                contact.phone = new_phone
                contact.email = new_email
                
                log.info(f"Contact updated: {contact.firstName} {contact.lastName}")
                return f"{contact.firstName}'s details updated."
            
        log.warning(f"Contact not found: {firstName}")
        return f"{firstName} not found."

    def delete_contact(self, firstName):
        
        """
        Deletes a contact from the address book based on the provided first name.

        Parameters:
            firstName (str): The first name of the contact to delete.

        Return Type:
            str: A message indicating whether the contact was deleted successfully or if it was not found.
        """
        
        for contact in self.contacts:
            if contact.firstName == firstName:
                self.contacts.remove(contact)
                log.info(f"Contact deleted: {firstName}")
                return f"{firstName}'s contact deleted."
        log.warning(f"Contact not found: {firstName}")
        return f"{firstName} not found."

    def display_contacts(self, sort_by='first_name'):
        
        """
        Returns a list of all contacts in the address book, sorted by the specified field.

        Parameters:
            sort_by (str): The field to sort contacts by. Options are 'first_name', 'last_name', 'city', 'state', or 'zip'. Default is 'first_name'.

        Return Type:
            list of Contact: A list of contacts sorted by the specified field.
        """
        
        log.info(f"Displaying contacts sorted by {sort_by}.")
        if sort_by == 'first_name':
            sorted_contacts = sorted(self.contacts, key=lambda contact: contact.firstName)
        elif sort_by == 'last_name':
            sorted_contacts = sorted(self.contacts, key=lambda contact: contact.lastName)
        elif sort_by == 'city':
            sorted_contacts = sorted(self.contacts, key=lambda contact: contact.city)
        elif sort_by == 'state':
            sorted_contacts = sorted(self.contacts, key=lambda contact: contact.state)
        elif sort_by == 'zip':
            sorted_contacts = sorted(self.contacts, key=lambda contact: contact.zip)
        else:
            sorted_contacts = self.contacts

        return sorted_contacts

    def search_by_city_or_state(self, search_option, search_value):
        
        """
        Searches for contacts by city or state.

        Parameters:
            search_option (int): Indicates the search criterion: 1 for city, 2 for state.
            search_value (str): The city or state to search for.

        Return Type:
            list of Contact: A list of contacts matching the search criterion.
        """
        
        log.info(f"Searching contacts by {'city' if search_option == 1 else 'state'}: {search_value}")
        results = [contact for contact in self.contacts if
                   (search_option == 1 and contact.city.lower() == search_value.lower()) or
                   (search_option == 2 and contact.state.lower() == search_value.lower())]
        return results

    def save_to_file(self, filename):
        
        """
        Saves the address book to a file in JSON format.

        Parameters:
            filename (str): The name of the file to save the address book to.

        Return Type:
            str: A message indicating whether the address book was saved successfully or if an error occurred.
        """
        
        try:
            with open(filename, 'w') as file:
                json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)
            log.info(f"Address book saved to {filename}.")
            return f"Address book saved to {filename}."
        
        except Exception as e:
            log.error(f"Error saving address book to file: {e}")
            return "Error saving address book."

    def load_from_file(self, filename):
        
        """
        Loads the address book from a file in JSON format.

        Parameters:
            filename (str): The name of the file to load the address book from.

        Return Type:
            str: A message indicating whether the address book was loaded successfully or if an error occurred.
        """
        
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.contacts = [Contact.from_dict(contact) for contact in data]
            log.info(f"Address book loaded from {filename}.")
            return f"Address book loaded from {filename}."
        
        except Exception as e:
            log.error(f"Error loading address book from file: {e}")
            return "Error loading address book."

class AddressBookManager:
    def __init__(self):
       
        self.addressBooks = {}

    def create_address_book(self, addressBook_name):
        
        """
        Creates a new address book with the given name.

        Parameters:
            addressBook_name (str): The name of the new address book.

        Return Type:
            str: A message indicating whether the address book was created successfully or if it already exists.
        """
        
        if addressBook_name in self.addressBooks:
            log.warning(f"Address book already exists: {addressBook_name}")
            return f"Address book {addressBook_name} already exists."
        
        self.addressBooks[addressBook_name] = AddressBook()
        log.info(f"Address book created: {addressBook_name}")
        return f"Address book {addressBook_name} created."

    def add_contact_to_address_book(self, addressBook_name, contact):
        
        """
        Adds a contact to a specific address book.

        Parameters:
            addressBook_name (str): The name of the address book to add the contact to.
            contact (Contact): The contact to add.

        Return Type:
            str: A message indicating whether the contact was added successfully or if the address book was not found.
        """
        
        if addressBook_name in self.addressBooks:
            log.info(f"Adding contact to {addressBook_name}: {contact.firstName} {contact.lastName}")
            return self.addressBooks[addressBook_name].add_contact(contact)
        
        log.error(f"Address book not found: {addressBook_name}")
        return f"Address book {addressBook_name} not found."

    def edit_contact_in_address_book(self, addressBook_name, firstName, new_values):
        
        """
        Edits a contact in a specific address book.

        Parameters:
            addressBook_name (str): The name of the address book containing the contact.
            firstName (str): The first name of the contact to edit.
            new_values (list of str): A list of new values for the contact's details.

        Return Type:
            str: A message indicating whether the contact was updated successfully or if the address book or contact was not found.
        """
        
        if addressBook_name in self.addressBooks:
            log.info(f"Editing contact in {addressBook_name}: {firstName}")
            return self.addressBooks[addressBook_name].edit_contact(firstName, new_values)
        
        log.error(f"Address book not found: {addressBook_name}")
        return f"Address book {addressBook_name} not found."

    def delete_contact_in_address_book(self, addressBook_name, firstName):
        
        """
        Deletes a contact from a specific address book.

        Parameters:
            addressBook_name (str): The name of the address book containing the contact.
            firstName (str): The first name of the contact to delete.

        Return Type:
            str: A message indicating whether the contact was deleted successfully or if the address book or contact was not found.
        """
        
        if addressBook_name in self.addressBooks:
            log.info(f"Deleting contact from {addressBook_name}: {firstName}")
            return self.addressBooks[addressBook_name].delete_contact(firstName)
        
        log.error(f"Address book not found: {addressBook_name}")
        return f"Address book {addressBook_name} not found."

    def display_contacts_in_address_book(self, addressBook_name, sort_by='first_name'):
        
        """
        Displays all contacts in a specific address book, sorted by the specified field.

        Parameters:
            addressBook_name (str): The name of the address book to display contacts from.
            sort_by (str): The field to sort contacts by. Options are 'first_name', 'last_name', 'city', 'state', or 'zip'. Default is 'first_name'.

        Return Type:
            list of Contact: A list of contacts sorted by the specified field.
        """
        
        if addressBook_name in self.addressBooks:
            log.info(f"Displaying contacts in {addressBook_name}, sorted by {sort_by}.")
            return self.addressBooks[addressBook_name].display_contacts(sort_by)
        
        log.error(f"Address book not found: {addressBook_name}")
        return []

    def search_person_by_city_or_state(self, search_option, search_value):
        
        """
        Searches for contacts across all address books by city or state.

        Parameters:
            search_option (int): Indicates the search criterion: 1 for city, 2 for state.
            search_value (str): The city or state to search for.

        Return Type:
            dict: A dictionary where keys are address book names and values are lists of contacts matching the search criterion.
        """
        
        log.info(f"Searching all address books by {'city' if search_option == 1 else 'state'}: {search_value}")
        results = {}
        
        for book_name, book in self.addressBooks.items():
            contacts = book.search_by_city_or_state(search_option, search_value)
            if contacts:
                results[book_name] = contacts
        return results

    def get_count_of_person_by_city_or_state(self, search_option, search_value):
        
        """
        Returns the count of contacts across all address books by city or state.

        Parameters:
            search_option (int): Indicates the search criterion: 1 for city, 2 for state.
            search_value (str): The city or state to count contacts for.

        Return Type:
            int: The total number of contacts matching the search criterion.
        """
        
        log.info(f"Counting contacts by {'city' if search_option == 1 else 'state'}: {search_value}")
        count = 0
        
        for book in self.addressBooks.values():
            count += len(book.search_by_city_or_state(search_option, search_value))
        return count

    def save_all_address_books_to_file(self, filename):
        
        """
        Saves all address books to a file in JSON format.

        Parameters:
            filename (str): The name of the file to save the address books to.

        Return Type:
            str: A message indicating whether all address books were saved successfully or if an error occurred.
        """
        
        try:
            with open(filename, 'w') as file:
                data = {
                    book_name: {
                        "contacts": [contact.to_dict() for contact in book.contacts]
                    }
                    for book_name, book in self.addressBooks.items()
                }
                json.dump(data, file, indent=4)
            log.info(f"All address books saved to {filename}.")
            return f"All address books saved to {filename}."
        
        except Exception as e:
            log.error(f"Error saving address books to file: {e}")
            return "Error saving address books."

    def load_all_address_books_from_file(self, filename):
        
        """
        Loads all address books from a file in JSON format.

        Parameters:
            filename (str): The name of the file to load the address books from.

        Return Type:
            str: A message indicating whether all address books were loaded successfully or if an error occurred.
        """
        
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.addressBooks = {}
                for book_name, book_data in data.items():
                    book = AddressBook()
                    book.contacts = [Contact.from_dict(contact) for contact in book_data["contacts"]]
                    self.addressBooks[book_name] = book
            log.info(f"All address books loaded from {filename}.")
            return f"All address books loaded from {filename}."
        
        except Exception as e:
            log.error(f"Error loading address books from file: {e}")
            return "Error loading address books."

def main():
    manager = AddressBookManager()
    
    while True:
        try:
            option = int(input("""
            Address Book Menu:
            1. Create Address Book
            2. Add Contact
            3. Edit Contact
            4. Delete Contact
            5. Display Contacts
            6. Search Person by City or State
            7. Get Count of Persons by City or State
            8. Save Address Books to File
            9. Load Address Books from File
            10. Exit
            Option: """))

            if option == 1:
                addressBook_name = input("Enter address book name: ")
                print(manager.create_address_book(addressBook_name))

            elif option == 2:
                print(manager.display_all_address_books())
                addressBook_name = input("Enter address book name: ")
                contact_data = [
                    input(f"Enter {field}: ") for field in
                    [   "Enter your First Name (eg:'Rahul'): ",
                        "Enter your Last Name (eg: J): ",
                        "Enter your Address (eg: '176A Teachers colony' ): ",
                        "Enter your City (eg: 'Erode'): ",
                        "Enter your State (eg: 'Tamil Nadu') ",
                        "Enter the Zip code (enter 6 digits): ",
                        "Enter your phone number (enter 10 digits): ",
                        "Enter your valid email (eg : 'abc123@gmail.com): "]
                ]
                if not Contact.validate_zip(contact_data[5]):
                    print("Invalid ZIP code format.")
                    continue
                if not Contact.validate_phone(contact_data[6]):
                    print("Invalid phone number format.")
                    continue
                if not Contact.validate_email(contact_data[7]):
                    print("Invalid email address format.")
                    continue
                contact = Contact(*contact_data)
                print(manager.add_contact_to_address_book(addressBook_name, contact))

            elif option == 3:
                addressBook_name = input("Enter address book name: ")
                firstName = input("Enter the first name of the contact to edit: ")
                new_values = [
                    input(f"Enter new {field} (leave blank to keep current): ") for field in
                    ["Last Name", "Address", "City", "State", "Zip", "Phone", "Email"]
                ]
                print(manager.edit_contact_in_address_book(addressBook_name, firstName, new_values))

            elif option == 4:
                addressBook_name = input("Enter address book name: ")
                firstName = input("Enter the first name of the contact to delete: ")
                print(manager.delete_contact_in_address_book(addressBook_name, firstName))

            elif option == 5:
                addressBook_name = input("Enter address book name: ")
                sort_by = input("Enter field to sort by (first_name, last_name, city, state, zip): ")
                contacts = manager.display_contacts_in_address_book(addressBook_name, sort_by)
                for contact in contacts:
                    print(contact)

            elif option == 6:
                search_option = int(input("Search by (1) City or (2) State: "))
                search_value = input("Enter the value to search: ")
                results = manager.search_person_by_city_or_state(search_option, search_value)
                for book_name, contacts in results.items():
                    print(f"Address Book: {book_name}")
                    for contact in contacts:
                        print(contact)

            elif option == 7:
                search_option = int(input("Count by (1) City or (2) State: "))
                search_value = input("Enter the value to count: ")
                count = manager.get_count_of_person_by_city_or_state(search_option, search_value)
                print(f"Total count: {count}")

            elif option == 8:
                filename = input("Enter filename to save all address books: ")
                print(manager.save_all_address_books_to_file(filename))

            elif option == 9:
                filename = input("Enter filename to load all address books from: ")
                print(manager.load_all_address_books_from_file(filename))

            elif option == 10:
                print("Exiting...")
                break

            else:
                print("Invalid option. Please try again.")

        except Exception as e:
            log.error(f"An error occurred: {e}")
            print("An error occurred. Please try again.")

if __name__ == "__main__":
    main()