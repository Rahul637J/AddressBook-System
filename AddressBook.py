'''

@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operation.  

'''

import pandas as pd
import json

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
        self.addressBooks = {}
    
    def create_Address_Book(self, addressBook_name):
        if addressBook_name not in self.addressBooks:
            self.addressBooks[addressBook_name] = []
            return f"{addressBook_name} is added successfully!"
        return f"{addressBook_name} already exists. Add new one!"
    
    def add_Contact(self, addressBook_Name, contact):
        """
        Description:
            Adds a new contact to the address book.
        
        Parameters:
            addressBook_Name (str): The name of the address book to which the contact will be added.
            contact (Contact): A contact object containing contact details like name, address, phone, and email.
        
        Return Type:
            str: A message indicating whether the contact was added successfully or already exists.
        """
        contacts = self.addressBooks[addressBook_Name]
        for list_contact in contacts:
            if contact.firstName == list_contact.firstName and contact.lastName == list_contact.lastName:
                return f"{contact.firstName} {contact.lastName} is already present in contact list. Try a different address book."
        self.addressBooks[addressBook_Name].append(contact)
        return f"{contact.firstName} added successfully to the {addressBook_Name} AddressBook"
    
    def edit_contact(self, addressBook_name, firstName, new_values):
        """
        Description:
            Edits an existing contact's details in the address book based on the first name provided.
            Only fields with new values are updated, otherwise, existing data remains unchanged.
        
        Parameters:
            addressBook_name (str): The name of the address book containing the contact.
            firstName (str): The first name of the contact to be edited.
            new_values (list): A list containing the new values for the contact fields. If no new value is 
                               provided for a field, the old value is retained.
        
        Return Type:
            str: A message indicating that the contact information has been updated.
        """
        contacts = self.addressBooks[addressBook_name]
        for contact in contacts:
            if firstName != contact.firstName:
                return f"{firstName} is not present in the AddressBook!"
            
            contact.lastName = new_values[0] or contact.lastName
            contact.address = new_values[1] or contact.address
            contact.city = new_values[2] or contact.city
            contact.state = new_values[3] or contact.state
            contact.zip = new_values[4] or contact.zip
            contact.phone = new_values[5] or contact.phone
            contact.email = new_values[6] or contact.email
            return f"{contact.firstName} Data Updated!"
                
    def delete_contact(self, addressBook_name, firstName):
        """
        Description:
            Deletes an existing contact's details in the address book based on the first name provided.
        
        Parameters:
            addressBook_name (str): The name of the address book containing the contact.
            firstName (str): The first name of the contact to be deleted.
        
        Return Type:
            str: A message indicating that the contact has been deleted.
        """
        contacts = self.addressBooks[addressBook_name]
        for contact in contacts:
            if firstName != contact.firstName:
                return f"{firstName} not found in '{addressBook_name}' AddressBook"
            self.addressBooks[addressBook_name].remove(contact)
            return f"{firstName} contact is deleted!"
    
    def display_all_addressBooks(self):
        """
        Description:
            Displays all address books.
        
        Parameters:
            None
        
        Return Type:
            list: A list of all address book names.
        """
        return list(self.addressBooks.keys())
    
    def display_all_contacts(self, addressBook_name, search_option):
        """
        Description:
            Displays all contacts in the address book, sorted by the given option.
        
        Parameters:
            addressBook_name (str): The name of the address book.
            search_option (int): Option to sort contacts (1 - First Name, 2 - City, 3 - State, 4 - No Sort).
        
        Return Type:
            list: A list of contacts sorted based on the search option.
        """
        if search_option == 1:
            return sorted(self.addressBooks[addressBook_name], key=lambda contact: contact.firstName)
        elif search_option == 2:
            return sorted(self.addressBooks[addressBook_name], key=lambda contact: contact.city)
        elif search_option == 3:
            return sorted(self.addressBooks[addressBook_name], key=lambda contact: contact.state)
        elif search_option == 4:
            return self.addressBooks[addressBook_name]
        else:
            return None

    def search_Person_by_city_or_state(self, search_option, search_value):
        """
        Description:
            Searches for persons in all address books by city or state.
        
        Parameters:
            search_option (int): Option to search by city (1) or state (2).
            search_value (str): The value to search for.
        
        Return Type:
            dict: A dictionary of address books and matching contacts.
        """
        person = {}
        for addressBook, contacts in self.addressBooks.items():
            if addressBook not in person:
                person[addressBook] = []
            for contact in contacts:
                if (search_option == 1 and contact.city.lower() == search_value.lower()) or \
                   (search_option == 2 and contact.state.lower() == search_value.lower()):
                    person[addressBook].append(contact)
        return person
    
    def get_countOf_Person_by_city_or_state(self, search_option, search_value):
        """
        Description:
            Gets the count of persons in all address books by city or state.
        
        Parameters:
            search_option (int): Option to search by city (1) or state (2).
            search_value (str): The value to search for.
        
        Return Type:
            int: The count of matching contacts.
        """
        countOf_contacts = 0
        for addressBook, contacts in self.addressBooks.items():
            for contact in contacts:
                if (search_option == 1 and contact.city.lower() == search_value.lower()) or \
                   (search_option == 2 and contact.state.lower() == search_value.lower()):
                    countOf_contacts += 1
        return countOf_contacts

    def write_data_in_file(self, search_option):
        """
        Description:
            Writes all address book data to an external file in the specified format.
        
        Parameters:
            search_option (int): Option to write in 'txt' (1), 'csv' (2), or 'json' (3).
        
        Return Type:
            str: The file name to which the data was written.
        """
        all_contacts = []
        for addressBook, contacts in self.addressBooks.items():
            for contact in contacts:
                contact_data = {
                    'Address Book': addressBook,
                    'First Name': contact.firstName,
                    'Last Name': contact.lastName,
                    'Address': contact.address,
                    'City': contact.city,
                    'State': contact.state,
                    'ZIP': contact.zip,
                    'Phone': contact.phone,
                    'Email': contact.email
                }
                all_contacts.append(contact_data)

        df = pd.DataFrame(all_contacts)
        file_name = None

        if search_option == 1:
            file_name = 'address_book_data.txt'
            with open(file_name, 'w') as file:
                file.write(df.to_string(index=False)) 
        elif search_option == 2:
            file_name = 'address_book_data.csv'
            df.to_csv(file_name, index=False)
        elif search_option == 3:
            file_name = 'address_book_data.json'
            df.to_json(file_name, orient='records', lines=True)    
        
        return file_name

    def save_to_json(self, filename):
        """
        Description:
            Saves the address book data to a JSON file.
        
        Parameters:
            filename (str): The name of the JSON file.
        
        Return Type:
            str: The name of the JSON file.
        """
        all_contacts = []
        for addressBook, contacts in self.addressBooks.items():
            for contact in contacts:
                contact_data = {
                    'Address Book': addressBook,
                    'First Name': contact.firstName,
                    'Last Name': contact.lastName,
                    'Address': contact.address,
                    'City': contact.city,
                    'State': contact.state,
                    'ZIP': contact.zip,
                    'Phone': contact.phone,
                    'Email': contact.email
                }
                all_contacts.append(contact_data)
        with open(filename, 'w') as file:
            json.dump(all_contacts, file, indent=4)
        return filename

    def load_from_json(self, filename):
        """
        Description:
            Loads address book data from a JSON file.
        
        Parameters:
            filename (str): The name of the JSON file.
        
        Return Type:
            str: A message indicating the number of contacts loaded.
        """
        with open(filename, 'r') as file:
            all_contacts = json.load(file)

        for contact_data in all_contacts:
            contact = Contact(
                firstName=contact_data['First Name'],
                lastName=contact_data['Last Name'],
                address=contact_data['Address'],
                city=contact_data['City'],
                state=contact_data['State'],
                zip=contact_data['ZIP'],
                phone=contact_data['Phone'],
                email=contact_data['Email']
            )
            address_book_name = contact_data['Address Book']
            if address_book_name not in self.addressBooks:
                self.addressBooks[address_book_name] = []
            self.addressBooks[address_book_name].append(contact)
        
        return f"{len(all_contacts)} contacts loaded from {filename}"

def main():
    
    address_book_manager = AddressBook()
    while True:
        print("1. Create Address Book")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Display All Address Books")
        print("6. Display All Contacts")
        print("7. Search Person by City or State")
        print("8. Get Count of Person by City or State")
        print("9. Write Data to File")
        print("10. Save Address Book to JSON")
        print("11. Load Address Book from JSON")
        print("12. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            addressBook_name = input("Enter Address Book Name: ")
            print(address_book_manager.create_Address_Book(addressBook_name))
        
        elif choice == 2:
            addressBook_name = input("Enter Address Book Name: ")
            contact = Contact(
                firstName=input("First Name: "),
                lastName=input("Last Name: "),
                address=input("Address: "),
                city=input("City: "),
                state=input("State: "),
                zip=input("ZIP: "),
                phone=input("Phone: "),
                email=input("Email: ")
            )
            print(address_book_manager.add_Contact(addressBook_name, contact))
        
        elif choice == 3:
            addressBook_name = input("Enter Address Book Name: ")
            firstName = input("Enter First Name of Contact to Edit: ")
            new_values = [
                input("New Last Name (leave blank to keep current): "),
                input("New Address (leave blank to keep current): "),
                input("New City (leave blank to keep current): "),
                input("New State (leave blank to keep current): "),
                input("New ZIP (leave blank to keep current): "),
                input("New Phone (leave blank to keep current): "),
                input("New Email (leave blank to keep current): ")
            ]
            print(address_book_manager.edit_contact(addressBook_name, firstName, new_values))
        
        elif choice == 4:
            addressBook_name = input("Enter Address Book Name: ")
            firstName = input("Enter First Name of Contact to Delete: ")
            print(address_book_manager.delete_contact(addressBook_name, firstName))
        
        elif choice == 5:
            print("Address Books:", address_book_manager.display_all_addressBooks())
        
        elif choice == 6:
            addressBook_name = input("Enter Address Book Name: ")
            search_option = int(input("Enter Search Option (1 - First Name, 2 - City, 3 - State, 4 - No Sort): "))
            contacts = address_book_manager.display_all_contacts(addressBook_name, search_option)
            for contact in contacts:
                print(contact)
        
        elif choice == 7:
            search_option = int(input("Enter Search Option (1 - City, 2 - State): "))
            search_value = input("Enter Search Value: ")
            persons = address_book_manager.search_Person_by_city_or_state(search_option, search_value)
            for addressBook, contacts in persons.items():
                print(f"Address Book: {addressBook}")
                for contact in contacts:
                    print(contact)
        
        elif choice == 8:
            search_option = int(input("Enter Search Option (1 - City, 2 - State): "))
            search_value = input("Enter Search Value: ")
            count = address_book_manager.get_countOf_Person_by_city_or_state(search_option, search_value)
            print(f"Count of persons: {count}")
        
        elif choice == 9:
            search_option = int(input("Enter File Format Option (1 - txt, 2 - csv, 3 - json): "))
            filename = address_book_manager.write_data_in_file(search_option)
            print(f"Data written to {filename}")
        
        elif choice == 10:
            filename = input("Enter JSON file name to save to: ")
            print(f"Data saved to {address_book_manager.save_to_json(filename)}")
        
        elif choice == 11:
            filename = input("Enter JSON file name to load from: ")
            
            print(address_book_manager.load_from_json(filename))
        
        elif choice == 12:
            break

if __name__ == "__main__":
    main()