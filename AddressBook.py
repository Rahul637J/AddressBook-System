'''
@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operation.  
'''

import re
import Mylog

log = Mylog.logger_init("UC_5")

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
    
    @staticmethod
    def validate_data(user_data):
        
        """
        Description:
            Validates user Email, Phone number, and Zip code.
        
        Parameters:
            user_data (list): The user data in list format.
        
        Return Type:
            Returns a boolean indicating whether all validations passed.
        """
        
        email, phone, zip_code = user_data[7], user_data[6], user_data[5]
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        phone_pattern = r'^\d{10}$'
        
        zip_pattern = r'^\d{6})?$'
        
        is_email_valid = re.match(email_pattern, email) is not None
        is_phone_valid = re.match(phone_pattern, phone) is not None
        is_zip_valid = re.match(zip_pattern, zip_code) is not None
        
        return is_email_valid and is_phone_valid and is_zip_valid

class AddressBook:
    
    def __init__(self):
        self.contacts = []
    
    def add_Contact(self, contact):
        
        """
        Description:
            Adds a new contact to the address book if all validations pass.
        
        Parameters:
            contact (Contact): A contact object containing contact details like name, address, phone, and email.
        
        Return Type:
            None
        """
        
        if Contact.validate_data([contact.firstName, contact.lastName, contact.address, contact.city, contact.state, contact.zip, contact.phone, contact.email]):
            self.contacts.append(contact)
            log.info("Contact added in addressbook")
            
        else:
            log.error("Failed to add contact due to validation error")
    
    def edit_contact(self, firstName, new_values):
        
        """
        Description:
            Edits an existing contact's details in the address book based on the first name provided.
            Only fields with new values are updated; otherwise, existing data remains unchanged.
        
        Parameters:
            firstName (str): The first name of the contact to be edited.
            new_values (list): A list containing the new values for the contact fields.
        
        Return Type:
            str: A message indicating that the contact information has been updated.
        """
        
        for contact in self.contacts:
            if firstName == contact.firstName:
                new_contact = Contact(
                    new_values[0] or contact.firstName,
                    new_values[1] or contact.lastName,
                    new_values[2] or contact.address,
                    new_values[3] or contact.city,
                    new_values[4] or contact.state,
                    new_values[5] or contact.zip,
                    new_values[6] or contact.phone,
                    new_values[7] or contact.email
                )
                if Contact.validate_data([new_contact.firstName, new_contact.lastName, new_contact.address, new_contact.city, new_contact.state, new_contact.zip, new_contact.phone, new_contact.email]):
                    self.contacts[self.contacts.index(contact)] = new_contact
                    log.info("Contact edited successfully")
                    return "User Data Updated!!!"
                else:
                    log.error("Failed to update contact due to validation error")
                    return "Validation error in new data"
        
        log.info("Contact not found")
        return "Contact not found"
    
    def delete_contact(self, firstName):
        """
        Description:
            Deletes an existing contact's details in the address book based on the first name provided.
        
        Parameters:
            firstName (str): The first name of the contact to be deleted.
        
        Return Type:
            str: A message indicating that the contact has been deleted.
        """
        for contact in self.contacts:
            if firstName == contact.firstName:
                self.contacts.remove(contact)
                log.info("Contact deleted")
                return f"{firstName} contact is deleted!!!"
        
        log.info("Contact not found")
        return f"{firstName} not found in 'AddressBook'"
    
    def display_all_contacts(self):
        
        """
        Description:
            Displays all contacts' details in the address book.
        
        Parameters:
            None
        
        Return Type:
            List of tuples: All the data of the contacts.
        """
        
        return [(contact.firstName, contact.lastName, contact.address, contact.city, contact.state, contact.zip, contact.phone, contact.email) for contact in self.contacts]

def main():
    addressbook_obj = AddressBook()
    print("-" * 35 + "\n| Welcome to Address Book Program |\n" + "-" * 35 + "\n")
    
    while True:
        option = int(input("Enter :\n" +
                           "       1. Add Contact\n" +
                           "       2. Edit Contact\n" +
                           "       3. Delete Contact\n" +
                           "       4. Display all contacts\n" +                                     
                           "       5. Exit\n" +
                           "option: "))
        
        if option == 1:
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
            
            new_contact = Contact(*user_data)
            addressbook_obj.add_Contact(new_contact)
        
        elif option == 2:
            
            userName = input("Enter your 'First name to edit contact': ")
            print("Leave the field empty if you don't want to update it.")
            prompts = [
                "Enter new First Name: ",
                "Enter new Last Name: ",
                "Enter new Address: ",
                "Enter new City: ",
                "Enter new State: ",
                "Enter new Zip code: ",
                "Enter new Phone Number: ",
                "Enter new Email: "
            ]
            new_values = [input(prompt) for prompt in prompts]
            print(addressbook_obj.edit_contact(userName, new_values))
        
        elif option == 3:
            
            firstName = input("Enter the contact firstName to delete: ")
            print(addressbook_obj.delete_contact(firstName))
        
        elif option == 4:
            
            contacts = addressbook_obj.display_all_contacts()
            for contact in contacts:
                print("-" * 50 + "\n" +
                      f"First Name: {contact[0]}\n" +
                      f"Last Name: {contact[1]}\n" +
                      f"Address: {contact[2]}\n" +
                      f"City: {contact[3]}\n" +
                      f"State: {contact[4]}\n" +
                      f"Zip: {contact[5]}\n" +
                      f"Phone: {contact[6]}\n" +
                      f"Email: {contact[7]}\n" +
                      "-" * 50)
        
        elif option == 5:
            
            print("Program exited!!!")
            return

if __name__ == "__main__":
    main()