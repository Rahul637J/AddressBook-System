import re
from Mylog import logger_init

log = logger_init("UC_6")

class Contact:
    def __init__(self, firstName, lastName, address, city, state, zip, phone, email):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.state = state
        
        # Validating zip code (should be exactly 6 digits)
        if not re.fullmatch(r'\d{6}', zip):
            raise ValueError("Zip code must be exactly 6 digits!")
        self.zip = zip
        
        # Validating phone number (should be exactly 10 digits)
        if not re.fullmatch(r'\d{10}', phone):
            raise ValueError("Phone number must be exactly 10 digits!")
        self.phone = phone
        
        # Validating email with provided regex pattern
        email_pattern = r'^[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$'
        if not re.fullmatch(email_pattern, email):
            raise ValueError("Invalid email format!")
        self.email = email

class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []
        
    def add_contact(self, contact):
        log.info("Contact added to addressbook")
        self.contacts.append(contact)
        
    def edit_contact(self, firstName, new_values):
        for contact in self.contacts:
            if firstName == contact.firstName:
                contact.lastName = new_values[0] or contact.lastName
                contact.address = new_values[1] or contact.address
                contact.city = new_values[2] or contact.city
                contact.state = new_values[3] or contact.state
                
                # Validate new values if provided
                if new_values[4]:
                    if not re.fullmatch(r'\d{6}', new_values[4]):
                        raise ValueError("Zip code must be exactly 6 digits!")
                    contact.zip = new_values[4]
                    
                if new_values[5]:
                    if not re.fullmatch(r'\d{10}', new_values[5]):
                        raise ValueError("Phone number must be exactly 10 digits!")
                    contact.phone = new_values[5]
                    
                if new_values[6]:
                    email_pattern = r'^[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$'
                    if not re.fullmatch(email_pattern, new_values[6]):
                        raise ValueError("Invalid email format!")
                    contact.email = new_values[6]

                log.info("Contact updated")
                return f"{firstName}'s contact updated!"
        log.info("Contact not found")
        return f"{firstName} not found in the address book!"
        
    def delete_contact(self, firstName):
        for contact in self.contacts:
            if firstName == contact.firstName:
                self.contacts.remove(contact)
                log.info("Contact deleted")
                return f"{firstName}'s contact deleted!"
        log.info("Contact not found")
        return f"{firstName} not found in the address book!"
    
    def display_contacts(self):
        log.info("Displaying all contacts")
        return [contact for contact in self.contacts]

class AddressBookManager:
    def __init__(self):
        self.addressBooks = {}
        
    def create_address_book(self, name):
        if name not in self.addressBooks:
            self.addressBooks[name] = AddressBook(name)
            log.info(f"Address book '{name}' created")
            return f"Address book '{name}' created successfully!"
        log.info("Address book already exists")
        return f"Address book '{name}' already exists!"
    
    def get_address_books(self):
        log.info("Retrieving all address books")
        return list(self.addressBooks.keys())
    
    def get_address_book(self, name):
        return self.addressBooks.get(name, None)

def main():
    manager = AddressBookManager()

    print("-" * 35 + "\n| Welcome to Address Book Program |\n" + "-" * 35 + "\n")

    while True:
        option = int(input("Enter:\n"
                           "1. Add new AddressBook\n"
                           "2. Add Contact\n"
                           "3. Edit Contact\n"
                           "4. Delete Contact\n"
                           "5. Display all contacts\n"
                           "6. Exit\n"
                           "Option: "))

        if option == 1:
            addressBook_name = input("Enter the name of the new address book: ")
            print("-" * 50 + "\n" + manager.create_address_book(addressBook_name) + "\n" + "-" * 50)

        elif option == 2:
            print(manager.get_address_books())
            addressBook_name = input("Enter the 'AddressBook' name from above list to add contact: ")

            addressBook = manager.get_address_book(addressBook_name)
            if not addressBook:
                print(f"'{addressBook_name}' AddressBook not found!!!")
                continue

            try:
                user_data = [
                    input("Enter your First Name: "),
                    input("Enter your Last Name: "),
                    input("Enter your Address: "),
                    input("Enter your City: "),
                    input("Enter your State: "),
                    input("Enter the Zip code: "),
                    input("Enter your phone number: "),
                    input("Enter your valid email: ")
                ]

                contact = Contact(*user_data)
                addressBook.add_contact(contact)
            except ValueError as ve:
                print(f"Error: {ve}")

        elif option == 3:
            print(manager.get_address_books())
            addressBook_name = input("Enter the AddressBook name from the above list to edit contact: ")

            addressBook = manager.get_address_book(addressBook_name)
            if not addressBook:
                print(f"'{addressBook_name}' AddressBook not found!!!")
                continue

            userName = input("Enter your 'First name' to edit contact: ")
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
                print(addressBook.edit_contact(userName, new_values))
            except ValueError as ve:
                print(f"Error: {ve}")

        elif option == 4:
            print(manager.get_address_books())
            addressBook_name = input("Enter the AddressBook name to delete contact: ")

            addressBook = manager.get_address_book(addressBook_name)
            if not addressBook:
                print(f"'{addressBook_name}' AddressBook not found!!!")
                continue

            firstName = input("Enter the contact's first name to delete: ")
            print(addressBook.delete_contact(firstName))

        elif option == 5:
            print(manager.get_address_books())
            addressBook_name = input("Enter the AddressBook name to view contacts: ")

            addressBook = manager.get_address_book(addressBook_name)
            if not addressBook:
                print(f"'{addressBook_name}' AddressBook not found!!!")
                continue

            for contact in addressBook.display_contacts():
                print("-" * 50)
                print(f"First Name: {contact.firstName}\nLast Name: {contact.lastName}\nAddress: {contact.address}\nCity: {contact.city}\nState: {contact.state}\nZip: {contact.zip}\nPhone: {contact.phone}\nEmail: {contact.email}")
                print("-" * 50)

        elif option == 6:
            print("Program exited!!!")
            return

if __name__ == "__main__":
    main()
