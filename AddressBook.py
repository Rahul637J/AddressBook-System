'''
@Author: Rahul
@Date: 2024-09-02
@Last Modified by: Rahul
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operations.
'''

from Mylog import logger_init
import re

log = logger_init("UC_7")

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
                log.info("Contact already exists")
                return f"{contact.firstName} {contact.lastName} is already in the address book."
        
        self.contacts.append(contact)
        log.info("Contact added to the address book.")
        return f"{contact.firstName} has been added successfully."
    
    def edit_contact(self, firstName, new_values):
        for contact in self.contacts:
            if firstName == contact.firstName:

                if new_values[0] and not re.match(r"^[a-zA-Z]+$", new_values[0]):
                    raise ValueError("New last name must contain only alphabets.")
                contact.lastName = new_values[0] or contact.lastName
                
                if new_values[1] and not re.match(r"^[a-zA-Z\s]+$", new_values[1]):
                    raise ValueError("New address must contain only alphabets and spaces.")
                contact.address = new_values[1] or contact.address
                
                if new_values[2] and not re.match(r"^[a-zA-Z\s]+$", new_values[2]):
                    raise ValueError("New city must contain only alphabets and spaces.")
                contact.city = new_values[2] or contact.city
                
                if new_values[3] and not re.match(r"^[a-zA-Z\s]+$", new_values[3]):
                    raise ValueError("New state must contain only alphabets and spaces.")
                contact.state = new_values[3] or contact.state
                
                if new_values[4] and not re.match(r"^[0-9]{6}$", new_values[4]):
                    raise ValueError("New ZIP code must be exactly 6 digits.")
                contact.zip = new_values[4] or contact.zip
                
                if new_values[5] and not re.match(r"^[0-9]{10}$", new_values[5]):
                    raise ValueError("New phone number must be exactly 10 digits.")
                contact.phone = new_values[5] or contact.phone
                
                if new_values[6] and not re.match(r'^[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}(?:\.[a-zA-Z]{2,3})?$', new_values[6]):
                    raise ValueError("New email address format is invalid.")
                contact.email = new_values[6] or contact.email
                
                log.info("Contact edited successfully.")
                return f"{contact.firstName}'s information has been updated."
        
        log.info("Contact not found.")
        return f"{firstName} not found in the address book."
    
    def delete_contact(self, firstName):
        for contact in self.contacts:
            if contact.firstName == firstName:
                self.contacts.remove(contact)
                log.info("Contact deleted.")
                return f"{firstName}'s contact has been deleted."
        
        log.info("Contact not found.")
        return f"{firstName} not found in the address book."
    
    def display_contacts(self):
        log.info("Displaying all contacts.")
        return [(c.firstName, c.lastName, c.address, c.city, c.state, c.zip, c.phone, c.email) for c in self.contacts]

class AddressBookManager:
    
    def __init__(self):
        self.addressBooks = {}
    
    def create_address_book(self, name):
        if not re.match(r"^[a-zA-Z0-9\s]+$", name):
            raise ValueError("Address book name can only contain alphabets, numbers, and spaces.")
        if name not in self.addressBooks:
            self.addressBooks[name] = AddressBook()
            log.info("Address book created.")
            return f"{name} has been created successfully."
        
        log.info("Address book already exists.")
        return f"{name} already exists. Please choose a different name."
    
    def add_contact_to_book(self, book_name, contact):
        if book_name in self.addressBooks:
            return self.addressBooks[book_name].add_contact(contact)
        
        log.info("Address book not found.")
        return f"Address book '{book_name}' does not exist."
    
    def edit_contact_in_book(self, book_name, firstName, new_values):
        if book_name in self.addressBooks:
            return self.addressBooks[book_name].edit_contact(firstName, new_values)
        
        log.info("Address book not found.")
        return f"Address book '{book_name}' does not exist."
    
    def delete_contact_from_book(self, book_name, firstName):
        if book_name in self.addressBooks:
            return self.addressBooks[book_name].delete_contact(firstName)
        
        log.info("Address book not found.")
        return f"Address book '{book_name}' does not exist."
    
    def display_all_books(self):
        log.info("Displaying all address books.")
        return list(self.addressBooks.keys())
    
    def display_contacts_in_book(self, book_name):
        if book_name in self.addressBooks:
            return self.addressBooks[book_name].display_contacts()
        
        log.info("Address book not found.")
        return f"Address book '{book_name}' does not exist."

def main():
    manager = AddressBookManager()

    print("-" * 35 + "\n| Welcome to Address Book Program |\n" + "-" * 35 + "\n")
    
    while True:
        option = int(input("Enter :\n" +
                           "1. Add new Address Book\n" +
                           "2. Add Contact\n" +
                           "3. Edit Contact\n" +
                           "4. Delete Contact\n" +
                           "5. Display all Contacts\n" +
                           "6. Exit\n" +
                           "Option: "))
        
        if option == 1:
            name = input("Enter the name of the new address book: ")
            try:
                print("-" * 50 + "\n" + manager.create_address_book(name) + "\n" + "-" * 50)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif option == 2:
            book_name = input("Enter the Address Book name: ")
            contact_info = [input(f"Enter {field}: ") for field in [[
                "Enter your First Name (eg:'Rahul'): ",
                "Enter your Last Name (eg: J): ",
                "Enter your Address (eg: '176A Teachers colony' ): ",
                "Enter your City (eg: 'Erode'): ",
                "Enter your State (eg: 'Tamil Nadu') ",
                "Enter the Zip code (enter 6 digits): ",
                "Enter your phone number (enter 10 digits): ",
                "Enter your valid email (eg : 'abc123@gmail.com): "
            ]]]
            try:
                contact = Contact(*contact_info)
                print("-" * 50 + "\n" + manager.add_contact_to_book(book_name, contact) + "\n" + "-" * 50)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif option == 3:
            book_name = input("Enter the Address Book name: ")
            firstName = input("Enter the First Name of the contact to edit: ")
            print("Leave the field blank if you don't want to update it.")
            new_values = [input(f"New {field}: ") for field in ["Last Name", "Address", "City", "State", "Zip", "Phone", "Email"]]
            try:
                print("-" * 50 + "\n" + manager.edit_contact_in_book(book_name, firstName, new_values) + "\n" + "-" * 50)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif option == 4:
            book_name = input("Enter the Address Book name: ")
            firstName = input("Enter the First Name of the contact to delete: ")
            print("-" * 50 + "\n" + manager.delete_contact_from_book(book_name, firstName) + "\n" + "-" * 50)
        
        elif option == 5:
            book_name = input("Enter the Address Book name: ")
            contacts = manager.display_contacts_in_book(book_name)
            if isinstance(contacts, str):
                print(contacts)
            else:
                for contact in contacts:
                    print(f"First Name: {contact[0]}, Last Name: {contact[1]}, Address: {contact[2]}, City: {contact[3]}, State: {contact[4]}, Zip: {contact[5]}, Phone: {contact[6]}, Email: {contact[7]}")
        
        elif option == 6:
            print("Program exited!")
            break

if __name__ == "__main__":
    main()
