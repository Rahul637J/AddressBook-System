'''

@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operation.  

'''

import os
import csv
import pandas as pd

from Mylog import logger_init

log = logger_init("UC_14")

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
        
        """
        Description:
            Adds a new contact to the address book.
        
        Parameters:
            contact (Contact): A contact object containing contact details like name, address, phone, and email.
        
        Return Type:
            str: A message indicating whether the contact was added or already exists.
        """
        
        for existing_contact in self.contacts:
            if contact.firstName == existing_contact.firstName and contact.lastName == existing_contact.lastName:
                log.info(f"Attempted to add duplicate contact: {contact.firstName} {contact.lastName}")
                return f"{contact.firstName} {contact.lastName} is already present."

        self.contacts.append(contact)
        log.info(f"Added contact: {contact.firstName} {contact.lastName}")
        return f"{contact.firstName} is added successfully."

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
            if firstName == contact.firstName:
                contact.lastName = new_values[0] or contact.lastName
                contact.address = new_values[1] or contact.address
                contact.city = new_values[2] or contact.city
                contact.state = new_values[3] or contact.state
                contact.zip = new_values[4] or contact.zip
                contact.phone = new_values[5] or contact.phone
                contact.email = new_values[6] or contact.email
                log.info(f"Updated contact: {contact.firstName} {contact.lastName}")
                return f"{contact.firstName} Data Updated!"
        
        log.warning(f"Contact with first name {firstName} not found for edit.")
        return f"{firstName} is not present in the AddressBook."

    def delete_contact(self, firstName):
        
        """
        Description:
            Delete an existing contact's details in the address book based on the first name provided.
        
        Parameters:
            firstName (str): The first name of the contact to be deleted.
        
        Return Type:
            str: A message indicating that the contact has been deleted.
        """
        
        for contact in self.contacts:
            if firstName == contact.firstName:
                self.contacts.remove(contact)
                log.info(f"Deleted contact: {firstName}")
                return f"{firstName} contact is deleted."
        
        log.warning(f"Contact with first name {firstName} not found for deletion.")
        return f"{firstName} not found in the AddressBook."

    def display_all_contacts(self, search_option):
        
        """
        Description:
            Display all contact's details in the address book based on sorting option.
        
        Parameters:
            search_option (int): Option to sort contacts (1 - First Name, 2 - City, 3 - State).
        
        Return Type:
            list: Sorted list of contact objects based on the given option.
        """
        
        if search_option == 1:
            return sorted(self.contacts, key=lambda contact: contact.firstName)
        elif search_option == 2:
            return sorted(self.contacts, key=lambda contact: contact.city)
        elif search_option == 3:
            return sorted(self.contacts, key=lambda contact: contact.state)
        else:
            log.warning(f"Invalid search option: {search_option}")
            return []
        
    def save_to_csv(self, filename):
        
        """
        Description:
            Save all contacts in the address book to a CSV file.
        
        Parameters:
            filename (str): The name of the CSV file to save the data to.
        
        Return Type:
            str: A message indicating whether the data was saved successfully.
        """
        
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['First Name', 'Last Name', 'Address', 'City', 'State', 'Zip', 'Phone', 'Email'])
            for contact in self.contacts:
                writer.writerow([
                    contact.firstName, contact.lastName, contact.address, contact.city, contact.state,
                    contact.zip, contact.phone, contact.email
                ])
        return f"Data saved to {filename} successfully."

    def load_from_csv(self, filename):
        
        """
        Description:
            Load contacts from a CSV file into the address book.
        
        Parameters:
            filename (str): The name of the CSV file to load data from.
        
        Return Type:
            str: A message indicating whether the data was loaded successfully.
        """
        
        if not os.path.exists(filename):
            return f"{filename} does not exist!"
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            self.contacts = []
            for row in reader:
                contact = Contact(
                    row['First Name'], row['Last Name'], row['Address'], row['City'], row['State'],
                    row['Zip'], row['Phone'], row['Email']
                )
                self.contacts.append(contact)
        return f"Data loaded from {filename} successfully."


class AddressBookManager:
    
    def __init__(self):

        self.addressBooks = {}

    def create_address_book(self, addressBook_name):
        
        """
        Description:
            Adds a new address book to the manager. If an address book with the same name already exists, it logs a warning and returns an appropriate message.

        Parameters:
            addressBook_name (str): The name of the address book to be created.

        Return Type:
            str: A message indicating success or failure of the operation.
        """
        
        if addressBook_name in self.addressBooks:
            log.warning(f"Address book already exists: {addressBook_name}")
            return f"Address book {addressBook_name} already exists."
        self.addressBooks[addressBook_name] = AddressBook()
        log.info(f"Address book created: {addressBook_name}")
        return f"Address book {addressBook_name} created."

    def add_contact_to_address_book(self, addressBook_name, contact):
        
        """
        Description:
            Adds a contact to the address book identified by addressBook_name. If the address book is not found, it logs an error and returns an appropriate message.

        Parameters:
            addressBook_name (str): The name of the address book where the contact will be added.
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
        Description:
            Updates the details of an existing contact in the address book identified by addressBook_name. If the address book is not found, it logs an error and returns an appropriate message.

        Parameters:
            addressBook_name (str): The name of the address book where the contact will be edited.
            firstName (str): The first name of the contact to be edited.
            new_values (list): A list of new values to update the contact with.

        Return Type:
            str: A message indicating success or failure of the operation.
        """
        
        if addressBook_name in self.addressBooks:
            log.info(f"Editing contact in {addressBook_name}: {firstName}")
            return self.addressBooks[addressBook_name].edit_contact(firstName, new_values)
        
        log.error(f"Address book not found: {addressBook_name}")
        return f"Address book {addressBook_name} not found."

    def delete_contact_in_address_book(self, addressBook_name, firstName):
        
        """
        Description:
            Removes a contact from the address book identified by addressBook_name. If the address book is not found, it logs an error and returns an appropriate message.

        Parameters:
            addressBook_name (str): The name of the address book from which the contact will be deleted.
            firstName (str): The first name of the contact to be deleted.

        Return Type:
            str: A message indicating success or failure of the operation.
        """
        
        if addressBook_name in self.addressBooks:
            log.info(f"Deleting contact from {addressBook_name}: {firstName}")
            return self.addressBooks[addressBook_name].delete_contact(firstName)
        
        log.error(f"Address book not found: {addressBook_name}")
        return f"Address book {addressBook_name} not found."

    def display_contacts_in_address_book(self, addressBook_name, sort_by='first_name'):
        
        """
        Description:
            Retrieves and returns all contacts from the address book identified by addressBook_name, sorted by the specified field. If the address book is not found, it logs an error and returns an empty list.

        Parameters:
            addressBook_name (str): The name of the address book to display contacts from.
            sort_by (str): The field to sort the contacts by (default is 'first_name').

        Return Type:
            list: A list of contacts sorted by the specified field.
        """
        
        if addressBook_name in self.addressBooks:
            log.info(f"Displaying contacts in {addressBook_name}, sorted by {sort_by}.")
            return self.addressBooks[addressBook_name].display_contacts(sort_by)
        
        log.error(f"Address book not found: {addressBook_name}")
        return []

    def search_person_by_city_or_state(self, search_option, search_value):
        
        """
        Description:
            Searches through all address books for contacts that match the specified city or state. Returns a dictionary of results, with address book names as keys and matching contacts as values.

        Parameters:
            search_option (int): Indicates whether to search by city (1) or state (2).
            search_value (str): The city or state to search for.

        Return Type:
            dict: A dictionary where keys are address book names and values are lists of contacts that match the search criteria.
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
        Description:
            Counts the number of contacts across all address books that match the specified city or state.

        Parameters:
            search_option (int): Indicates whether to count by city (1) or state (2).
            search_value (str): The city or state to count contacts for.

        Return Type:
            int: The total count of contacts matching the search criteria.
        """
        
        log.info(f"Counting contacts by {'city' if search_option == 1 else 'state'}: {search_value}")
        count = 0
        for book in self.addressBooks.values():
            count += len(book.search_by_city_or_state(search_option, search_value))
        return count

    def save_all_address_books_to_csv(self, filename):
        
        """
        Description:
            Writes all address books to a CSV file. Each address book is saved as a separate sheet in an Excel file.

        Parameters:
            filename (str): The name of the file to save the address books to.

        Return Type:
            str: A message indicating success or failure of the operation.
        """
        
        try:
            with pd.ExcelWriter(filename) as writer:
                for book_name, book in self.addressBooks.items():
                    df = book.save_to_dataframe()
                    df.to_excel(writer, sheet_name=book_name, index=False)
            log.info(f"All address books saved to {filename} in CSV format.")
            return f"All address books saved to {filename} in CSV format."
        
        except Exception as e:
            log.error(f"Error saving address books to CSV file: {e}")
            return "Error saving address books to CSV file."

    def load_all_address_books_from_csv(self, filename):
        
        """
        Description:
            Reads address books from a CSV file where each address book is stored as a separate sheet in an Excel file. Initializes address books in the manager based on the loaded data.

        Parameters:
            filename (str): The name of the file to load the address books from.

        Return Type:
            str: A message indicating success or failure of the operation.
        """
        
        try:
            self.addressBooks = {}
            
            with pd.ExcelFile(filename) as reader:
                
                for sheet_name in reader.sheet_names:
                    df = pd.read_excel(reader, sheet_name=sheet_name)
                    book = AddressBook()
                    book.contacts = [
                        Contact(row["First Name"], row["Last Name"], row["Address"],
                                row["City"], row["State"], row["Zip"], row["Phone"], row["Email"])
                        for index, row in df.iterrows()
                    ]
                    
                    self.addressBooks[sheet_name] = book
                    
            log.info(f"All address books loaded from {filename} in CSV format.")
            return f"All address books loaded from {filename} in CSV format."
        
        except Exception as e:
            log.error(f"Error loading address books from CSV file: {e}")
            return "Error loading address books from CSV file."

    def save_all_address_books_to_txt(self, filename):
        
        """
        Description:
            Writes all address books to a text file. Each address book is preceded by its name and followed by its contacts.

        Parameters:
            filename (str): The name of the file to save the address books to.

        Return Type:
            str: A message indicating success or failure of the operation.
        """
        
        try:
            with open(filename, 'a') as file:
                for book_name, book in self.addressBooks.items():
                    file.write(f"Address Book: {book_name}\n")
                    for contact in book.contacts:
                        file.write(f"{contact.firstName} {contact.lastName}, {contact.address}, {contact.city}, {contact.state}, {contact.zip}, {contact.phone}, {contact.email}\n")
                    file.write("\n")
            log.info(f"All address books saved to {filename} in TXT format.")
            return f"All address books saved to {filename} in TXT format."
        
        except Exception as e:
            log.error(f"Error saving address books to TXT file: {e}")
            return "Error saving address books to TXT file."

    def load_all_address_books_from_txt(self, filename):
        
        """
        Description:
            Reads address books from a text file where each address book is preceded by its name and followed by its contacts. Initializes address books in the manager based on the loaded data.

        Parameters:
            filename (str): The name of the file to load the address books from.

        Return Type:
            str: A message indicating success or failure of the operation.
        """
        
        try:
            self.addressBooks = {}
            with open(filename, 'r') as file:
                lines = file.readlines()
                current_book_name = None
                
                for line in lines:
                    line = line.strip()
                    
                    if line.startswith("Address Book:"):
                        current_book_name = line.split("Address Book:")[1].strip()
                        self.addressBooks[current_book_name] = AddressBook()
                        
                    elif line:
                        parts = line.split(', ')
                        
                        if len(parts) == 8:
                            contact = Contact(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7])
                            self.addressBooks[current_book_name].contacts.append(contact)
                            
            log.info(f"All address books loaded from {filename} in TXT format.")
            return f"All address books loaded from {filename} in TXT format."
        
        except Exception as e:
            log.error(f"Error loading address books from TXT file: {e}")
            return "Error loading address books from TXT file."


def main():
    manager = AddressBookManager()
    
    while True:
        try:
            option = int(input("""\
            Address Book Menu:
            1. Create Address Book
            2. Add Contact
            3. Edit Contact
            4. Delete Contact
            5. Display Contacts
            6. Search Person by City or State
            7. Get Count of Persons by City or State
            8. Save All Address Books to CSV
            9. Load All Address Books from CSV
            10. Save All Address Books to TXT
            11. Load All Address Books from TXT
            12. Exit
            Option: """))

            if option == 1:
                addressBook_name = input("Enter address book name: ")
                print(manager.create_address_book(addressBook_name))

            elif option == 2:
                print(manager.addressBooks.keys())
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
                    [   "Enter your First Name (eg:'Rahul'): ",
                        "Enter your Last Name (eg: J): ",
                        "Enter your Address (eg: '176A Teachers colony' ): ",
                        "Enter your City (eg: 'Erode'): ",
                        "Enter your State (eg: 'Tamil Nadu') ",
                        "Enter the Zip code (enter 6 digits): ",
                        "Enter your phone number (enter 10 digits): ",
                        "Enter your valid email (eg : 'abc123@gmail.com): "]
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
                filename = input("Enter filename to save all address books (CSV format): ")
                print(manager.save_all_address_books_to_csv(filename))

            elif option == 9:
                filename = input("Enter filename to load all address books (CSV format): ")
                print(manager.load_all_address_books_from_csv(filename))

            elif option == 10:
                filename = input("Enter filename to save all address books (TXT format): ")
                print(manager.save_all_address_books_to_txt(filename))

            elif option == 11:
                filename = input("Enter filename to load all address books (TXT format): ")
                print(manager.load_all_address_books_from_txt(filename))

            elif option == 12:
                print("Exiting...")
                break

            else:
                print("Invalid option. Please try again.")

        except Exception as e:
            log.error(f"An error occurred: {e}")
            print("An error occurred. Please try again.")

if __name__ == "__main__":
    main()
