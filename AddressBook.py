'''

@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operation.  

'''

class Contact:
    
    def __init__(self,firstName,lastname,address,city,state,zip,phone,email):
        
        self.firstName=firstName
        self.lastName=lastname
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        self.phone=phone
        self.email=email

class AddressBook:
    
    def __init__(self):
        self.contacts=list()
    
    def add_Contact(self,contact):
        
        """
        Description:
            Adds a new contact to the address book.
        
        Parameters:
            contact (Contact): A contact object containing contact details like name, address, phone, and email.
        
        Return Type:
            None
        """
        
        self.contacts.append(contact)
    
    def edit_contact(self,firstName,new_values):
        
        """
        Description:
            Edits an existing contact's details in the address book based on the first name provided.
            Only fields with new values are updated, otherwise, existing data remains unchanged.
        
        Parameters:
            firstName (str): The first name of the contact to be edited.
            new_values (list): A list containing the new values for the contact fields. If no new value is 
                               provided for a field, the old value is retained.
        
        Return Type:
            str: A message indicating that the contact information has been updated.
        """
        
        for contact in self.contacts:
            
            if firstName == contact.firstName:
                
                contact.firstName = new_values[0] or contact.firstName
                contact.lastName = new_values[1] or contact.lastName
                contact.address = new_values[2] or contact.address
                contact.city = new_values[3] or contact.city
                contact.state = new_values[4] or contact.state
                contact.zip_code = new_values[5] or contact.zip_code
                contact.phone = new_values[6] or contact.phone
                contact.email = new_values[7] or contact.email

            return "User Data Updated!!!"
            
def main():
    
    addressbook_obj=AddressBook()

    print("-"*35+"\n| Welcome to Address Book Program |\n"+"-"*35+"\n")
    
    while True:
        option = int(input("Enter :\n"+
                           "       1. Add Contact\n"+
                           "       2. Edit Contact\n"+
                           "       3. Exit\n"+
                           "option: "))
        
        if option == 1:
            
            user_data=[
                "Enter your First Name: ",
                "Enter your Last Name: ",
                "Enter your Address: ",
                "Enter your City: ",
                "Enter your State: ",
                "Enter the Zip code: ",
                "Enter your phone number: ",
                "Enter your valid email: "
                ]

            user_data=[input(user_input) for user_input in user_data]
            
            addressbook_obj.add_Contact(Contact(*user_data))
        
        if option == 2:
            
            userName=input("Enter your 'First name to edit contact': ")
            
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

            print(addressbook_obj.edit_contact(userName,new_values))
            
        if option == 3:
            print("Program exited!!!")
            return    
    
if __name__=="__main__":
    main()
