'''

@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform phonebook operation.  

'''

class Contact:
    
    def __init__(self,firstName,lastName,address,city,state,zip,phone,email):
        
        self.firstName=firstName
        self.lastName=lastName
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        self.phone=phone
        self.email=email

class AddressBook:
    
    def __init__(self):
        self.addressBooks={}
    
    def create_Address_Book(self,addressBook_name):
        
        if addressBook_name not in self.addressBooks:
            self.addressBooks[addressBook_name]=[]
            return f"{addressBook_name} is added successfull!!!"
        
        return f"{addressBook_name} is already exist add new!!!"
    
    def add_Contact(self,addressBook_Name,contact):
        
        """
        Description:
            Adds a new contact to the address book.
        
        Parameters:
            contact (Contact): A contact object containing contact details like name, address, phone, and email.
        
        Return Type:
            None
        """
        
        contacts=self.addressBooks[addressBook_Name]
        for list_contact in contacts:
            if contact.firstName == list_contact.firstName and contact.lastName == list_contact.lastName:
                return f"{contact.firstName +" " +contact.lastName} is already present in contact try with differen AddressBook"    
        
        self.addressBooks[addressBook_Name].append(contact)
        return f"{contact.firstName} is added successfully to the {addressBook_Name} AddressBook"
    
    def edit_contact(self, addressBook_name, firstName, new_values):
        
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
        
        contacts = self.addressBooks[addressBook_name]
        
        for contact in contacts: 
                if firstName != contact.firstName:
                            return f"{firstName} is not present in the AddressBook!!!"
                
                contact.lastName = new_values[0] or contact.lastName
                contact.address = new_values[1] or contact.address
                contact.city = new_values[2] or contact.city
                contact.state = new_values[3] or contact.state
                contact.zip_code = new_values[4] or contact.zip
                contact.phone = new_values[5] or contact.phone
                contact.email = new_values[6] or contact.email

                return f"{contact.firstName} Data Updated!!!"
                    
    def delete_contact(self,addressBook_name,firstName):
            
        """
        Description:
            Delete an existing contact's details in the address book based on the first name provided.
        Parameters:
            firstName (str): The first name of the contact to be delete.
        Return Type:
            str: A message indicating that the contact information has been updated.
        """
        
        contacts = self.addressBooks[addressBook_name]
            
        for contact in contacts:
            
            if firstName != contact.firstName:
                return firstName+" not found in 'AddressBook'"

            self.contacts.remove(contact)
            return firstName+" contact is deleted!!!"
    
    def display_all_addressBooks(self):
            
        """
        Description:
            Displaying all the addressbook..
        Parameters:
            None
        Return Type:
            str: A message indicating that the contact information has been updated.
        """    
        
        return list(self.addressBooks.keys())
            
    def display_all_contacts(self,addressBook_name):
            
        """
        Description:
            Displaying all contact's details in the address book..
        Parameters:
            None:
        Return Type:
            Tuple: All the data of the contact.
        """
        
        contacts = self.addressBooks[addressBook_name]    
            
        for contact in contacts:
            
            return contact.firstName,contact.lastName,contact.address,contact.city,contact.state,contact.zip,contact.phone,contact.email
                
def main():
    
    addressbook_obj=AddressBook()

    print("-"*35+"\n| Welcome to Address Book Program |\n"+"-"*35+"\n")
    
    while True:
        option = int(input("Enter :\n"+
                           "       1. Add new AddressBook\n"+
                           "       2. Add Contact\n"+
                           "       3. Edit Contact\n"+
                           "       4. Delete Contact\n"+
                           "       5. Display all contacts in AddressBook\n"+                                     
                           "       6. Exit\n"+
                           "option: "))
        
        if option == 1:
            
            addressbook_name=input("Enter the name of the new address book: ")
            print("-"*50+"\n"+addressbook_obj.create_Address_Book(addressbook_name)+"\n"+"-"*50)
            
        if option == 2:
            
            print(addressbook_obj.display_all_addressBooks())

            addressbook_name=input("Enter the 'AddressBook' name from above list to add contact: ")

                          
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

            print("-"*50+"\n"+addressbook_obj.add_Contact(addressbook_name,Contact(*user_data))+"\n"+"-"*50)
        
        if option == 3:
            
            print(addressbook_obj.display_all_addressBooks())
            
            addressbook_name=input("Enter the AddressBook name from the above list to edit contact: ")

            userName=input("Enter your 'First name to edit contact': ")
                
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

            print("-"*50+"\n"+addressbook_obj.edit_contact(addressbook_name,userName,new_values)+"\n"+"-"*50)
            
        if option == 4:
            
            print(addressbook_obj.display_all_addressBooks())
            
            addressbook_name=input("Enter one of the AddressBook(s) from above list to delete contact: ")
            
            firstName=input("Enter the contact firstName to delete: ")    
            print("-"*50+"\n"+addressbook_obj.delete_contact(addressbook_name,firstName)+"\n"+"-"*50)
        
        if option == 5:
            
            print(addressbook_obj.display_all_addressBooks())
            addressbook_name=input("Enter one of the AddressBook(s) from above list to find all contacts:")
            
            if addressbook_obj.addressBooks[addressbook_name]:
                firstName,lastName,address,city,state,zip,phone,email=addressbook_obj.display_all_contacts(addressbook_name)
                print("-"*50+"\n"+f"First Name: {firstName}\nLast Name: {lastName}\nAddress: {address}\nCity: {city}\nState: {state}\nZip: {zip}\nPhone: {phone}\nEmail: {email}\n"+"-"*50)
            
            else:
                print("-"*50+"\n"+f'"{addressbook_name}" AddressBook is empty add contacts first'+"\n"+"-"*50)    
               
        if option == 6:
            print("Program exited!!!")
            return    
    
if __name__=="__main__":
    main()
