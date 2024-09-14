'''

@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operation.  

'''

from Mylog import logger_init

log = logger_init("UC_9")

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


class AddressBook:
    
    def __init__(self):
        self.addressBooks = {}
    
    def create_Address_Book(self, addressBook_name):
        if addressBook_name not in self.addressBooks:
            self.addressBooks[addressBook_name] = []
            log.info(f"Created new AddressBook: {addressBook_name}")
            return f"{addressBook_name} is added successfully!"
        log.warning(f"AddressBook {addressBook_name} already exists.")
        return f"{addressBook_name} already exists. Please add a new one!"
    
    def add_Contact(self, addressBook_Name, contact):
        """
        Description:
            Adds a new contact to the address book.
        
        Parameters:
            contact (Contact): A contact object containing contact details.
        
        Return Type:
            str: A message indicating success or failure of the operation.
        """
        contacts = self.addressBooks[addressBook_Name]
        for list_contact in contacts:
            if contact.firstName == list_contact.firstName and contact.lastName == list_contact.lastName:
                log.warning(f"Contact {contact.firstName} {contact.lastName} already exists in {addressBook_Name}.")
                return f"{contact.firstName + ' ' + contact.lastName} is already present in {addressBook_Name}."
        
        self.addressBooks[addressBook_Name].append(contact)
        log.info(f"Added contact {contact.firstName} to {addressBook_Name}.")
        return f"{contact.firstName} is added successfully to {addressBook_Name}."
    
    def edit_contact(self, addressBook_name, firstName, new_values):
        """
        Description:
            Edits an existing contact's details in the address book.
        
        Parameters:
            firstName (str): The first name of the contact to be edited.
            new_values (list): New values for the contact fields.
        
        Return Type:
            str: A message indicating the update status.
        """
        contacts = self.addressBooks[addressBook_name]
        for contact in contacts: 
            if firstName == contact.firstName:
                contact.lastName = new_values[0] or contact.lastName
                contact.address = new_values[1] or contact.address
                contact.city = new_values[2] or contact.city
                contact.state = new_values[3] or contact.state
                contact.zip = new_values[4] or contact.zip
                contact.phone = new_values[5] or contact.phone
                contact.email = new_values[6] or contact.email
                log.info(f"Updated contact {contact.firstName} in {addressBook_name}.")
                return f"{contact.firstName}'s data updated successfully!"
        log.warning(f"Contact {firstName} not found in {addressBook_name}.")
        return f"{firstName} is not present in the AddressBook!"
    
    def delete_contact(self, addressBook_name, firstName):
        """
        Description:
            Deletes a contact from the address book.
        
        Parameters:
            firstName (str): The first name of the contact to delete.
        
        Return Type:
            str: A message indicating the deletion status.
        """
        contacts = self.addressBooks[addressBook_name]
        for contact in contacts:
            if firstName == contact.firstName:
                contacts.remove(contact)
                log.info(f"Deleted contact {firstName} from {addressBook_name}.")
                return f"{firstName}'s contact is deleted successfully!"
        log.warning(f"Contact {firstName} not found in {addressBook_name}.")
        return f"{firstName} not found in the AddressBook!"
    
    def display_all_addressBooks(self):
        """
        Description:
            Displays all the address books.
        
        Return Type:
            list: A list of all address book names.
        """
        return list(self.addressBooks.keys())
    
    def display_all_contacts(self, addressBook_name):
        """
        Description:
            Displays all contacts in the address book.
        
        Return Type:
            list: A list of contact objects.
        """
        return self.addressBooks[addressBook_name]
    
    def search_Person_by_city_or_state(self, search_option, search_value):
        """
        Description:
            Searches for a person in all address books based on city or state.
        
        Parameters:
            search_option (int): Search by city (1) or state (2).
            search_value (str): The value to search for (city or state).
        
        Return Type:
            dict: A dictionary of matching contacts by address book.
        """
        person = {}
        for addressBook, contacts in self.addressBooks.items():
            if addressBook not in person:
                person[addressBook] = []

            for contact in contacts:
                if (search_option == 1 and contact.city.lower() == search_value.lower()) or \
                   (search_option == 2 and contact.state.lower() == search_value.lower()):
                    person[addressBook].append(contact)
        log.info(f"Searched for contacts by {'city' if search_option == 1 else 'state'}: {search_value}")
        return person


def main():
    addressbook_obj = AddressBook()
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
            print("-" * 50 + "\n" + addressbook_obj.create_Address_Book(addressbook_name) + "\n" + "-" * 50)
        
        elif option == 2:
            print(addressbook_obj.display_all_addressBooks())
            addressbook_name = input("Enter the 'AddressBook' name from the above list to add contact: ")

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
            user_data = [input(user_input) for user_input in user_data]
            print("-" * 50 + "\n" + addressbook_obj.add_Contact(addressbook_name, Contact(*user_data)) + "\n" + "-" * 50)
        
        elif option == 3:
            print(addressbook_obj.display_all_addressBooks())
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
            print("-" * 50 + "\n" + addressbook_obj.edit_contact(addressbook_name, userName, new_values) + "\n" + "-" * 50)
        
        elif option == 4:
            print(addressbook_obj.display_all_addressBooks())
            addressbook_name = input("Enter one of the AddressBook(s) from above list to delete contact: ")
            firstName = input("Enter the contact's first name to delete: ")
            print("-" * 50 + "\n" + addressbook_obj.delete_contact(addressbook_name, firstName) + "\n" + "-" * 50)
        
        elif option == 5:
            print(addressbook_obj.display_all_addressBooks())
            addressbook_name = input("Enter one of the AddressBook(s) from above list to find all contacts: ")
            
            if addressbook_obj.addressBooks[addressbook_name]:
                contacts = addressbook_obj.display_all_contacts(addressbook_name)
                for contact in contacts:
                    print("-" * 50 + "\n" + f'''First Name: {contact.firstName}\nLast Name: {contact.lastName}\nAddress: {contact.address}\nCity: {contact.city}\nState: {contact.state}\nZip: {contact.zip}\nPhone: {contact.phone}\nEmail: {contact.email}\n''' + "-" * 50)
            else:
                print("-" * 50 + "\n" + f'"{addressbook_name}" AddressBook is empty. Add contacts first.' + "\n" + "-" * 50)
        
        elif option == 6:
            print("Search by:\n       1. City\n       2. State")
            search_option = int(input("Option: "))
            search_value = input("Enter the city or state to search: ")
            
            search_result = addressbook_obj.search_Person_by_city_or_state(search_option, search_value)
            for addressBook, contacts in search_result.items():
                if contacts:
                    print("-" * 50 + "\n" + f'In "{addressBook}":')
                    for contact in contacts:
                        print(f'''First Name: {contact.firstName}\nLast Name: {contact.lastName}\nAddress: {contact.address}\nCity: {contact.city}\nState: {contact.state}\nZip: {contact.zip}\nPhone: {contact.phone}\nEmail: {contact.email}\n''' + "-" * 50)
        
        elif option == 7:
            break


if __name__ == "__main__":
    main()
