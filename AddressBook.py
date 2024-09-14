'''

@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operation.  

'''

from Mylog import logger_init

log = logger_init("UC_10")

class Contact:
    def __init__(self, firstName, lastName, address, city, state, zip, phone, email):
        """
        Description:
            Initializes a Contact object with the provided details.

        Parameters:
            firstName (str): The first name of the contact.
            lastName (str): The last name of the contact.
            address (str): The street address of the contact.
            city (str): The city where the contact lives.
            state (str): The state where the contact lives.
            zip (str): The ZIP code of the contact's location.
            phone (str): The contact's phone number.
            email (str): The contact's email address.
        """
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"{self.firstName} {self.lastName}, {self.city}, {self.state}, {self.phone}"


class AddressBook:
    def __init__(self, name):
        """
        Description:
            Initializes an AddressBook object which stores multiple contacts.

        Parameters:
            name (str): The name of the address book.
        """
        self.name = name
        self.contacts = []
        log.info(f"Created AddressBook: {self.name}")

    def add_contact(self, contact):
        """
        Description:
            Adds a new contact to the address book.

        Parameters:
            contact (Contact): A contact object containing contact details like name, address, phone, and email.

        Return Type:
            str: A message indicating success or if the contact already exists.
        """
        for existing_contact in self.contacts:
            if contact.firstName == existing_contact.firstName and contact.lastName == existing_contact.lastName:
                log.warning(f"Contact {contact.firstName} {contact.lastName} already exists in {self.name}.")
                return f"{contact.firstName} {contact.lastName} already exists."
        
        self.contacts.append(contact)
        log.info(f"Added contact {contact.firstName} {contact.lastName} to {self.name}.")
        return f"{contact.firstName} {contact.lastName} added successfully to {self.name}."

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
            if contact.firstName == firstName:
                contact.lastName = new_values[0] or contact.lastName
                contact.address = new_values[1] or contact.address
                contact.city = new_values[2] or contact.city
                contact.state = new_values[3] or contact.state
                contact.zip = new_values[4] or contact.zip
                contact.phone = new_values[5] or contact.phone
                contact.email = new_values[6] or contact.email
                log.info(f"Updated contact {contact.firstName} {contact.lastName} in {self.name}.")
                return f"{contact.firstName}'s data updated in {self.name}."
        
        log.warning(f"Contact {firstName} not found in {self.name}.")
        return f"{firstName} not found in {self.name}."

    def delete_contact(self, firstName):
        """
        Description:
            Deletes a contact by their first name from the address book.

        Parameters:
            firstName (str): The first name of the contact to delete.

        Return Type:
            str: A message indicating whether the deletion was successful or not.
        """
        for contact in self.contacts:
            if contact.firstName == firstName:
                self.contacts.remove(contact)
                log.info(f"Deleted contact {firstName} from {self.name}.")
                return f"{firstName} deleted from {self.name}."
        
        log.warning(f"Contact {firstName} not found in {self.name}.")
        return f"{firstName} not found in {self.name}."

    def display_contacts(self):
        """
        Description:
            Returns all contacts in the address book.

        Return Type:
            list: A list of all contacts in the address book.
        """
        return self.contacts


class AddressBookManager:
    def __init__(self):
        """
        Description:
            Manages multiple address books.
        """
        self.addressBooks = {}
        log.info("Initialized AddressBookManager.")

    def create_address_book(self, name):
        """
        Description:
            Creates a new address book with the specified name.

        Parameters:
            name (str): The name of the new address book.

        Return Type:
            str: A message indicating whether the address book was created or already exists.
        """
        if name not in self.addressBooks:
            self.addressBooks[name] = AddressBook(name)
            log.info(f"Created new address book: {name}")
            return f"Address book '{name}' created successfully."
        
        log.warning(f"Address book '{name}' already exists.")
        return f"Address book '{name}' already exists."

    def get_address_book(self, name):
        """
        Description:
            Retrieves an address book by name.

        Parameters:
            name (str): The name of the address book.

        Return Type:
            AddressBook: The address book object.
        """
        return self.addressBooks.get(name, None)

    def display_all_address_books(self):
        """
        Description:
            Displays the names of all address books.

        Return Type:
            list: A list of all address book names.
        """
        return list(self.addressBooks.keys())

def main():
    manager = AddressBookManager()

    while True:
        option = int(input("Enter:\n1. Create Address Book\n2. Add Contact\n3. Edit Contact\n4. Delete Contact\n5. Display Contacts\n6. Exit\nOption: "))
        
        if option == 1:
            name = input("Enter address book name: ")
            print(manager.create_address_book(name))
        
        elif option == 2:
            name = input("Enter address book name: ")
            address_book = manager.get_address_book(name)
            if address_book:
                contact_data = [
                    input("First Name: "),
                    input("Last Name: "),
                    input("Address: "),
                    input("City: "),
                    input("State: "),
                    input("ZIP: "),
                    input("Phone: "),
                    input("Email: ")
                ]
                contact = Contact(*contact_data)
                print(address_book.add_contact(contact))
            else:
                print(f"Address book '{name}' does not exist.")
        
        elif option == 3:
            name = input("Enter address book name: ")
            address_book = manager.get_address_book(name)
            if address_book:
                firstName = input("Enter first name of the contact to edit: ")
                new_values = [
                    input("New Last Name (leave empty to keep unchanged): "),
                    input("New Address (leave empty to keep unchanged): "),
                    input("New City (leave empty to keep unchanged): "),
                    input("New State (leave empty to keep unchanged): "),
                    input("New ZIP (leave empty to keep unchanged): "),
                    input("New Phone (leave empty to keep unchanged): "),
                    input("New Email (leave empty to keep unchanged): ")
                ]
                print(address_book.edit_contact(firstName, new_values))
            else:
                print(f"Address book '{name}' does not exist.")
        
        elif option == 4:
            name = input("Enter address book name: ")
            address_book = manager.get_address_book(name)
            if address_book:
                firstName = input("Enter first name of the contact to delete: ")
                print(address_book.delete_contact(firstName))
            else:
                print(f"Address book '{name}' does not exist.")
        
        elif option == 5:
            name = input("Enter address book name: ")
            address_book = manager.get_address_book(name)
            if address_book:
                contacts = address_book.display_contacts()
                if contacts:
                    for contact in contacts:
                        print(contact)
                else:
                    print(f"No contacts in '{name}' address book.")
            else:
                print(f"Address book '{name}' does not exist.")
        
        elif option == 6:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
