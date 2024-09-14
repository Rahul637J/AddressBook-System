'''

@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operation.  

'''

from Mylog import logger_init

log = logger_init("UC_12")

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
        if any(c.firstName == contact.firstName and c.lastName == contact.lastName for c in self.contacts):
            return f"{contact.firstName} {contact.lastName} is already present."
        self.contacts.append(contact)
        log.info(f"Added contact: {contact}")
        return f"{contact.firstName} added successfully."

    def edit_contact(self, firstName, new_values):
        for contact in self.contacts:
            if contact.firstName == firstName:
                contact.lastName = new_values[0] or contact.lastName
                contact.address = new_values[1] or contact.address
                contact.city = new_values[2] or contact.city
                contact.state = new_values[3] or contact.state
                contact.zip = new_values[4] or contact.zip
                contact.phone = new_values[5] or contact.phone
                contact.email = new_values[6] or contact.email
                log.info(f"Edited contact: {contact}")
                return f"{contact.firstName}'s data updated."
        return f"{firstName} not found."

    def delete_contact(self, firstName):
        for contact in self.contacts:
            if contact.firstName == firstName:
                self.contacts.remove(contact)
                log.info(f"Deleted contact: {contact}")
                return f"{firstName} contact deleted."
        return f"{firstName} not found."

    def display_all_contacts(self, search_option):
        if search_option == 1:
            return sorted(self.contacts, key=lambda c: c.firstName)
        elif search_option == 2:
            return sorted(self.contacts, key=lambda c: c.city)
        elif search_option == 3:
            return sorted(self.contacts, key=lambda c: c.state)
        return self.contacts

    def search_person_by_city_or_state(self, search_option, search_value):
        results = [c for c in self.contacts if 
                   (search_option == 1 and c.city.lower() == search_value.lower()) or
                   (search_option == 2 and c.state.lower() == search_value.lower())]
        return results

    def get_count_by_city_or_state(self, search_option, search_value):
        count = len(self.search_person_by_city_or_state(search_option, search_value))
        return count

class AddressBookManager:
    def __init__(self):
        self.address_books = {}

    def create_address_book(self, addressBook_name):
        if addressBook_name not in self.address_books:
            self.address_books[addressBook_name] = AddressBook()
            log.info(f"Created address book: {addressBook_name}")
            return f"{addressBook_name} created successfully."
        return f"{addressBook_name} already exists."

    def get_address_book(self, addressBook_name):
        return self.address_books.get(addressBook_name)

    def add_contact_to_address_book(self, addressBook_name, contact):
        book = self.get_address_book(addressBook_name)
        if book:
            return book.add_contact(contact)
        return f"{addressBook_name} not found."

    def edit_contact_in_address_book(self, addressBook_name, firstName, new_values):
        book = self.get_address_book(addressBook_name)
        if book:
            return book.edit_contact(firstName, new_values)
        return f"{addressBook_name} not found."

    def delete_contact_in_address_book(self, addressBook_name, firstName):
        book = self.get_address_book(addressBook_name)
        if book:
            return book.delete_contact(firstName)
        return f"{addressBook_name} not found."

    def display_all_address_books(self):
        return list(self.address_books.keys())

    def display_contacts_in_address_book(self, addressBook_name, search_option):
        book = self.get_address_book(addressBook_name)
        if book:
            return book.display_all_contacts(search_option)
        return f"{addressBook_name} not found."

    def search_person_by_city_or_state(self, search_option, search_value):
        results = {}
        for name, book in self.address_books.items():
            results[name] = book.search_person_by_city_or_state(search_option, search_value)
        return results

    def get_count_of_person_by_city_or_state(self, search_option, search_value):
        count = 0
        for book in self.address_books.values():
            count += book.get_count_by_city_or_state(search_option, search_value)
        return count

def main():
    manager = AddressBookManager()
    print("-" * 35 + "\n| Welcome to Address Book Program |\n" + "-" * 35 + "\n")
    
    while True:
        option = int(input("Enter:\n" +
                           "       1. Add new AddressBook\n" +
                           "       2. Add Contact\n" +
                           "       3. Edit Contact\n" +
                           "       4. Delete Contact\n" +
                           "       5. Display all contacts in AddressBook\n" +
                           "       6. Search person by city or state\n" +
                           "       7. Get Count of contacts by 'City' or 'State'\n" +
                           "       8. Exit\n" +
                           "Option: "))
        
        if option == 1:
            addressBook_name = input("Enter the name of the new address book: ")
            print("-" * 50 + "\n" + manager.create_address_book(addressBook_name) + "\n" + "-" * 50)
        
        elif option == 2:
            print(manager.display_all_address_books())
            addressBook_name = input("Enter the 'AddressBook' name to add contact: ")
            user_data = [
                "Enter your First Name: ",
                "Enter your Last Name: ",
                "Enter your Address: ",
                "Enter your City: ",
                "Enter your State: ",
                "Enter the Zip code: ",
                "Enter your phone number: ",
                "Enter your valid email: "
            ]
            contact_data = [input(prompt) for prompt in user_data]
            contact = Contact(*contact_data)
            print("-" * 50 + "\n" + manager.add_contact_to_address_book(addressBook_name, contact) + "\n" + "-" * 50)
        
        elif option == 3:
            print(manager.display_all_address_books())
            addressBook_name = input("Enter the AddressBook name to edit contact: ")
            firstName = input("Enter the first name of the contact to edit: ")
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
            print("-" * 50 + "\n" + manager.edit_contact_in_address_book(addressBook_name, firstName, new_values) + "\n" + "-" * 50)
        
        elif option == 4:
            print(manager.display_all_address_books())
            addressBook_name = input("Enter the AddressBook name to delete contact: ")
            firstName = input("Enter the first name of the contact to delete: ")
            print("-" * 50 + "\n" + manager.delete_contact_in_address_book(addressBook_name, firstName) + "\n" + "-" * 50)
        
        elif option == 5:
            search_option = int(input("Enter 1 to sort by 'First Name'\nEnter 2 to sort by 'City'\nEnter 3 to sort by 'State'\nOption: "))
            print(manager.display_all_address_books())
            addressBook_name = input("Enter the AddressBook name to display all contacts: ")
            contacts = manager.display_contacts_in_address_book(addressBook_name, search_option)
            if contacts:
                for contact in contacts:
                    print("-" * 50 + "\n" + f'''First Name: {contact.firstName}\nLast Name: {contact.lastName}\nAddress: {contact.address}\nCity: {contact.city}\nState: {contact.state}\nZip: {contact.zip}\nPhone: {contact.phone}\nEmail: {contact.email}\n''' + "-" * 50)
            else:
                print("-" * 50 + "\n" + f'"{addressBook_name}" AddressBook is empty. Please add contacts first.' + "\n" + "-" * 50)
        
        elif option == 6:
            search_option = int(input("Enter 1 to search by 'City'\nEnter 2 to search by 'State'\nOption: "))
            search_value = input("Enter the city/state to search: ")
            results = manager.search_person_by_city_or_state(search_option, search_value)
            if results:
                for name, contacts in results.items():
                    print(f"\nIn AddressBook '{name}':")
                    for contact in contacts:
                        print(f"{contact.firstName} {contact.lastName}")
            else:
                print("No contacts found.")
        
        elif option == 7:
            search_option = int(input("Enter 1 to get count by 'City'\nEnter 2 to get count by 'State'\nOption: "))
            search_value = input("Enter the city/state to get the count of contacts: ")
            count = manager.get_count_of_person_by_city_or_state(search_option, search_value)
            print(f"Total number of contacts in city/state '{search_value}' are: {count}")
        
        elif option == 8:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
