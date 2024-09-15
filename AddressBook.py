'''
@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operation.  
'''

from Mylog import logger_init
import re

log = logger_init("UC_9")

class Contact:
    def __init__(self, firstName, lastName, address, city, state, zip, phone, email):
        # Validation for ZIP code
        if not re.match(r"^\d{6}$", zip):
            raise ValueError("Invalid ZIP code. It should be exactly 6 digits.")
        
        # Validation for Phone number
        if not re.match(r"^\d{10}$", phone):
            raise ValueError("Invalid phone number. It should be exactly 10 digits.")
        
        # Validation for Email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
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

    def add_Contact(self, contact):
        """
        Description:
            Adds a new contact to the address book.
        
        Parameters:
            contact (Contact): A contact object containing contact details.
        
        Return Type:
            str: A message indicating success or failure of the operation.
        """
        for existing_contact in self.contacts:
            if contact.firstName == existing_contact.firstName and contact.lastName == existing_contact.lastName:
                log.warning(f"Contact {contact.firstName} {contact.lastName} already exists.")
                return f"{contact.firstName + ' ' + contact.lastName} already exists in the AddressBook."
        
        self.contacts.append(contact)
        log.info(f"Added contact {contact.firstName}.")
        return f"{contact.firstName} is added successfully to the AddressBook."

    def edit_Contact(self, firstName, new_values):
        """
        Description:
            Edits an existing contact's details in the address book.
        
        Parameters:
            firstName (str): The first name of the contact to be edited.
            new_values (list): New values for the contact fields.
        
        Return Type:
            str: A message indicating the update status.
        """
        for contact in self.contacts:
            if firstName == contact.firstName:
                if new_values[4] and not re.match(r"^\d{6}$", new_values[4]):
                    raise ValueError("New ZIP code must be exactly 6 digits.")
                if new_values[5] and not re.match(r"^\d{10}$", new_values[5]):
                    raise ValueError("New phone number must be exactly 10 digits.")
                if new_values[6] and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', new_values[6]):
                    raise ValueError("New email address format is invalid.")
                
                contact.lastName = new_values[0] or contact.lastName
                contact.address = new_values[1] or contact.address
                contact.city = new_values[2] or contact.city
                contact.state = new_values[3] or contact.state
                contact.zip = new_values[4] or contact.zip
                contact.phone = new_values[5] or contact.phone
                contact.email = new_values[6] or contact.email
                log.info(f"Updated contact {contact.firstName}.")
                return f"{contact.firstName}'s data updated successfully!"
        log.warning(f"Contact {firstName} not found.")
        return f"{firstName} is not present in the AddressBook."

    def delete_Contact(self, firstName):
        """
        Description:
            Deletes a contact from the address book.
        
        Parameters:
            firstName (str): The first name of the contact to delete.
        
        Return Type:
            str: A message indicating the deletion status.
        """
        for contact in self.contacts:
            if firstName == contact.firstName:
                self.contacts.remove(contact)
                log.info(f"Deleted contact {firstName}.")
                return f"{firstName}'s contact is deleted successfully!"
        log.warning(f"Contact {firstName} not found.")
        return f"{firstName} not found in the AddressBook."

    def display_all_contacts(self):
        """
        Description:
            Displays all contacts in the address book.
        
        Return Type:
            list: A list of contact objects.
        """
        return self.contacts

    def search_by_city_or_state(self, search_option, search_value):
        """
        Description:
            Searches for a person in the address book based on city or state.
        
        Parameters:
            search_option (int): Search by city (1) or state (2).
            search_value (str): The value to search for (city or state).
        
        Return Type:
            list: A list of matching contacts.
        """
        results = []
        for contact in self.contacts:
            if (search_option == 1 and contact.city.lower() == search_value.lower()) or \
               (search_option == 2 and contact.state.lower() == search_value.lower()):
                results.append(contact)
        return results


class AddressBookManager:
    def __init__(self):
        self.addressBooks = {}

    def create_Address_Book(self, addressBook_name):
        if addressBook_name not in self.addressBooks:
            self.addressBooks[addressBook_name] = AddressBook()
            log.info(f"Created new AddressBook: {addressBook_name}")
            return f"{addressBook_name} is added successfully!"
        log.warning(f"AddressBook {addressBook_name} already exists.")
        return f"{addressBook_name} already exists. Please add a new one!"

    def display_all_addressBooks(self):
        """
        Description:
            Displays all the address books.
        
        Return Type:
            list: A list of all address book names.
        """
        return list(self.addressBooks.keys())


def main():
    addressbook_manager = AddressBookManager()
    print("-" * 35 + "\n| Welcome to Address Book Program |\n" + "-" * 35 + "\n")
    
    while True:
        option = int(input("Enter :\n" +
                           "       1. Add new AddressBook\n" +
                           "       2. Add Contact\n" +
                           "       3. Edit Contact\n" +
                           "       4. Delete Contact\n" +
                           "       5. Display all contacts in AddressBook\n" +
                           "       6. Search person by city or state\n" +
                           "       7. Exit\n" +
                           "option: "))
        
        if option == 1:
            addressbook_name = input("Enter the name of the new address book: ")
            print("-" * 50 + "\n" + addressbook_manager.create_Address_Book(addressbook_name) + "\n" + "-" * 50)
        
        elif option == 2:
            print(addressbook_manager.display_all_addressBooks())
            addressbook_name = input("Enter the 'AddressBook' name from the above list to add contact: ")

            user_data = [
                "Enter your First Name (eg:'Rahul'): ",
                "Enter your Last Name (eg: J): ",
                "Enter your Address (eg: '176A Teachers colony' ): ",
                "Enter your City (eg: 'Erode'): ",
                "Enter your State (eg: 'Tamil Nadu') ",
                "Enter the Zip code (enter 6 digits): ",
                "Enter your phone number (enter 10 digits): ",
                "Enter your valid email (eg : 'abc123@gmail.com): "
            ]
            user_data = [input(user_input) for user_input in user_data]
            try:
                contact = Contact(*user_data)
                print("-" * 50 + "\n" + addressbook_manager.addressBooks[addressbook_name].add_Contact(contact) + "\n" + "-" * 50)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif option == 3:
            print(addressbook_manager.display_all_addressBooks())
            addressbook_name = input("Enter the AddressBook name from the above list to edit contact: ")
            userName = input("Enter your 'First name to edit contact': ")

            print("Leave the field empty if you don't want to update it.")
            prompts = [
                "Enter new Last Name: ",
                "Enter new Address: ",
                "Enter new City: ",
                "Enter new State: ",
                "Enter new Zip code: ",
                "Enter new Phone Number: ",
                "Enter new Email: "
            ]
            new_values = [input(prompt) for prompt in prompts]
            try:
                print("-" * 50 + "\n" + addressbook_manager.addressBooks[addressbook_name].edit_Contact(userName, new_values) + "\n" + "-" * 50)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif option == 4:
            print(addressbook_manager.display_all_addressBooks())
            addressbook_name = input("Enter one of the AddressBook(s) from above list to delete contact: ")
            firstName = input("Enter the contact's first name to delete: ")
            print("-" * 50 + "\n" + addressbook_manager.addressBooks[addressbook_name].delete_Contact(firstName) + "\n" + "-" * 50)
        
        elif option == 5:
            print(addressbook_manager.display_all_addressBooks())
            addressbook_name = input("Enter one of the AddressBook(s) from above list to find all contacts: ")
            
            contacts = addressbook_manager.addressBooks[addressbook_name].display_all_contacts()
            if contacts:
                for contact in contacts:
                    print("-" * 50 + "\n" + f'''First Name: {contact.firstName}\nLast Name: {contact.lastName}\nAddress: {contact.address}\nCity: {contact.city}\nState: {contact.state}\nZip: {contact.zip}\nPhone: {contact.phone}\nEmail: {contact.email}\n''' + "-" * 50)
            else:
                print("-" * 50 + "\n" + f'"{addressbook_name}" AddressBook is empty. Add contacts first.' + "\n" + "-" * 50)
        
        elif option == 6:
            print("Search by:\n       1. City\n       2. State")
            search_option = int(input("Option: "))
            search_value = input("Enter the city or state to search: ")
            
            for addressBook_name, addressBook in addressbook_manager.addressBooks.items():
                search_results = addressBook.search_by_city_or_state(search_option, search_value)
                if search_results:
                    for contact in search_results:
                        print("-" * 50 + "\n" + f"First Name: {contact.firstName}, Last Name: {contact.lastName}, City: {contact.city}, State: {contact.state}\n" + "-" * 50)
        
        elif option == 7:
            print("-" * 50 + "\n" + "Thanks for using the Address Book application!" + "\n" + "-" * 50)
            break

if __name__ == "__main__":
    main()
