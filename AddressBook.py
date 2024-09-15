'''
@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operation.  
'''

from Mylog import logger_init
import re

log = logger_init("UC_11")

class Contact:

    def __init__(self, firstName, lastName, address, city, state, zip, phone, email):
        
        """
        Initializes a new contact with the provided details.

        Parameters:
            firstName (str): First name of the contact.
            lastName (str): Last name of the contact.
            address (str): Address of the contact.
            city (str): City of the contact.
            state (str): State of the contact.
            zip (str): ZIP code of the contact.
            phone (str): Phone number of the contact.
            email (str): Email address of the contact.
        """
        
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
            zip_code (str): ZIP code to be validated.

        Return Type:
            bool: True if the ZIP code is valid, False otherwise.
        """
        
        return re.match(r"^\d{6}$", zip_code) is not None

    @staticmethod
    def validate_phone(phone_number):
        
        """
        Validates the phone number format.

        Parameters:
            phone_number (str): Phone number to be validated.

        Return Type:
            bool: True if the phone number is valid, False otherwise.
        """
        
        return re.match(r"^\d{10}$", phone_number) is not None

    @staticmethod
    def validate_email(email_address):
        
        """
        Validates the email address format.

        Parameters:
            email_address (str): Email address to be validated.

        Return Type:
            bool: True if the email address is valid, False otherwise.
        """
        
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_address) is not None

class AddressBook:
    
    def __init__(self):
      
        self.contacts = []

    def add_contact(self, contact):
        
        """
        Adds a new contact to the address book, ensuring no duplicates.

        Parameters:
            contact (Contact): A contact object containing contact details.

        Return Type:
            str: A message indicating success or failure of the operation.
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
            firstName (str): The first name of the contact to be edited.
            new_values (list): A list of new values for the contact's details, where each entry corresponds to
                               Last Name, Address, City, State, Zip, Phone, and Email respectively.

        Return Type:
            str: A message indicating the result of the edit operation.
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
            firstName (str): The first name of the contact to be deleted.

        Return Type:
            str: A message indicating the result of the delete operation.
        """
        
        for contact in self.contacts:
            if contact.firstName == firstName:
                self.contacts.remove(contact)
                log.info(f"Contact deleted: {firstName}")
                return f"{firstName}'s contact deleted."
            
        log.warning(f"Contact not found: {firstName}")
        return f"{firstName} not found."

    def display_contacts(self):
        
        """
        Returns a list of all contacts in the address book, sorted by first name.

        Return Type:
            list: A list of Contact objects sorted by first name.
        """
        
        log.info("Displaying all contacts.")
        return sorted(self.contacts, key=lambda contact: contact.firstName)

    def search_by_city_or_state(self, search_option, search_value):
        
        """
        Searches for contacts by city or state.

        Parameters:
            search_option (int): Indicates the search criterion: 1 for city, 2 for state.
            search_value (str): The city or state to search for.

        Return Type:
            list: A list of Contact objects matching the search criterion.
        """
        
        log.info(f"Searching contacts by {'city' if search_option == 1 else 'state'}: {search_value}")
        results = [contact for contact in self.contacts if
                   (search_option == 1 and contact.city.lower() == search_value.lower()) or
                   (search_option == 2 and contact.state.lower() == search_value.lower())]
        
        return results

class AddressBookManager:
  
    def __init__(self):
      
        self.addressBooks = {}

    def create_address_book(self, addressBook_name):
        
        """
        Creates a new address book if it does not already exist.

        Parameters:
            addressBook_name (str): The name of the address book to be created.

        Return Type:
            str: A message indicating success or failure of the creation operation.
        """
        
        if addressBook_name not in self.addressBooks:
            self.addressBooks[addressBook_name] = AddressBook()
            log.info(f"Address book created: {addressBook_name}")
            return f"{addressBook_name} created successfully."
        
        log.warning(f"Attempted to create duplicate address book: {addressBook_name}")
        return f"{addressBook_name} already exists."

    def add_contact_to_address_book(self, addressBook_name, contact):
        
        """
        Adds a contact to a specific address book.

        Parameters:
            addressBook_name (str): The name of the address book to which the contact will be added.
            contact (Contact): A contact object containing contact details.

        Return Type:
            str: A message indicating success or failure of the operation.
        """
        
        if addressBook_name in self.addressBooks:
            log.info(f"Adding contact to {addressBook_name}: {contact.firstName} {contact.lastName}")
            return self.addressBooks[addressBook_name].add_contact(contact)
        
        log.error(f"Address book not found: {addressBook_name}")
        return f"Address book {addressBook_name} not found."

    def edit_contact_in_address_book(self, addressBook_name, firstName, new_values):
        
        """
        Edits a contact's details in a specific address book.

        Parameters:
            addressBook_name (str): The name of the address book where the contact is located.
            firstName (str): The first name of the contact to be edited.
            new_values (list): A list of new values for the contact's details, where each entry corresponds to
                               Last Name, Address, City, State, Zip, Phone, and Email respectively.

        Return Type:
            str: A message indicating the result of the edit operation.
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
            addressBook_name (str): The name of the address book where the contact is located.
            firstName (str): The first name of the contact to be deleted.

        Return Type:
            str: A message indicating the result of the delete operation.
        """
        
        if addressBook_name in self.addressBooks:
            log.info(f"Deleting contact in {addressBook_name}: {firstName}")
            return self.addressBooks[addressBook_name].delete_contact(firstName)
        
        log.error(f"Address book not found: {addressBook_name}")
        return f"Address book {addressBook_name} not found."

    def display_all_address_books(self):
        
        """
        Returns a list of all address book names.

        Return Type:
            list: A list of names of all address books.
        """
        
        log.info("Displaying all address books.")
        return list(self.addressBooks.keys())

    def display_contacts_in_address_book(self, addressBook_name):
        
        """
        Displays all contacts in a specific address book.

        Parameters:
            addressBook_name (str): The name of the address book.

        Return Type:
            list: A list of Contact objects in the specified address book.
        """
        
        if addressBook_name in self.addressBooks:
            log.info(f"Displaying contacts in {addressBook_name}")
            return self.addressBooks[addressBook_name].display_contacts()
        
        log.error(f"Address book not found: {addressBook_name}")
        return []

    def search_person_by_city_or_state(self, search_option, search_value):
        
        """
        Searches for contacts across all address books by city or state.

        Parameters:
            search_option (int): Indicates the search criterion: 1 for city, 2 for state.
            search_value (str): The city or state to search for.

        Return Type:
            dict: A dictionary where the keys are address book names and the values are lists of Contact objects
                  that match the search criterion.
        """
        
        log.info(f"Searching across all address books by {'city' if search_option == 1 else 'state'}: {search_value}")
        results = {}
        
        for book_name, address_book in self.addressBooks.items():
            contacts = address_book.search_by_city_or_state(search_option, search_value)
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
        
        count = 0
        log.info(f"Counting contacts by {'city' if search_option == 1 else 'state'}: {search_value}")
        
        for address_book in self.addressBooks.values():
            count += len(address_book.search_by_city_or_state(search_option, search_value))
        return count

def main():
    manager = AddressBookManager()

    while True:
        try:
            option = int(input("Choose an option:\n"
                               "1. Create Address Book\n"
                               "2. Add Contact\n"
                               "3. Edit Contact\n"
                               "4. Delete Contact\n"
                               "5. Display Contacts\n"
                               "6. Search by City or State\n"
                               "7. Count by City or State\n"
                               "8. Exit\nOption: "))

            if option == 1:
                addressBook_name = input("Enter address book name: ")
                print(manager.create_address_book(addressBook_name))

            elif option == 2:
                print(manager.display_all_address_books())
                addressBook_name = input("Enter address book name: ")
                contact_data = [
                    input(f"Enter {field}: ") for field in
                    ["First Name", "Last Name", "Address", "City", "State", "Zip", "Phone", "Email"]
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
                print(manager.display_all_address_books())
                addressBook_name = input("Enter address book name: ")
                firstName = input("Enter the first name of the contact to edit: ")
                new_values = [
                    input(f"Enter new {field} (leave empty to skip): ") for field in
                    [   "Enter your First Name (eg:'Rahul'): ",
                        "Enter your Last Name (eg: J): ",
                        "Enter your Address (eg: '176A Teachers colony' ): ",
                        "Enter your City (eg: 'Erode'): ",
                        "Enter your State (eg: 'Tamil Nadu') ",
                        "Enter the Zip code (enter 6 digits): ",
                        "Enter your phone number (enter 10 digits): ",
                        "Enter your valid email (eg : 'abc123@gmail.com): "]
                ]
                if new_values[4] and not Contact.validate_zip(new_values[4]):
                    print("Invalid ZIP code format.")
                    continue
                if new_values[5] and not Contact.validate_phone(new_values[5]):
                    print("Invalid phone number format.")
                    continue
                if new_values[6] and not Contact.validate_email(new_values[6]):
                    print("Invalid email address format.")
                    continue
                print(manager.edit_contact_in_address_book(addressBook_name, firstName, new_values))

            elif option == 4:
                print(manager.display_all_address_books())
                addressBook_name = input("Enter address book name: ")
                firstName = input("Enter the first name of the contact to delete: ")
                print(manager.delete_contact_in_address_book(addressBook_name, firstName))

            elif option == 5:
                print(manager.display_all_address_books())
                addressBook_name = input("Enter address book name: ")
                contacts = manager.display_contacts_in_address_book(addressBook_name)
                if contacts:
                    for contact in contacts:
                        print(f"{contact.firstName} {contact.lastName}: {contact.address}, {contact.city}, {contact.state}, {contact.zip}, {contact.phone}, {contact.email}")
                else:
                    print("No contacts found.")

            elif option == 6:
                search_option = int(input("Search by 1. City 2. State: "))
                if search_option not in [1, 2]:
                    print("Invalid search option.")
                    continue
                search_value = input("Enter the value: ")
                results = manager.search_person_by_city_or_state(search_option, search_value)
                if results:
                    for book_name, contacts in results.items():
                        print(f"Address Book: {book_name}")
                        for contact in contacts:
                            print(f"{contact.firstName} {contact.lastName}: {contact.address}, {contact.city}, {contact.state}, {contact.zip}, {contact.phone}, {contact.email}")
                else:
                    print("No contacts found.")

            elif option == 7:
                search_option = int(input("Count by 1. City 2. State: "))
                if search_option not in [1, 2]:
                    print("Invalid count option.")
                    continue
                search_value = input("Enter the value: ")
                count = manager.get_count_of_person_by_city_or_state(search_option, search_value)
                print(f"Total count of persons: {count}")

            elif option == 8:
                print("Exiting the program.")
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
