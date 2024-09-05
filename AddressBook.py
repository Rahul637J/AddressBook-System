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
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"    

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
            str: A message with the first name for contact added.
        """
        
        contacts = self.addressBooks[addressBook_Name]
        
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
            list: Return all the addressbook in the list format.
        """    
        
        return list(self.addressBooks.keys())
            
    def display_all_contacts(self,addressBook_name,search_option):
            
        """
        Description:
            Displaying all contact's details in the address book..
        Parameters:
            None:
        Return Type:
            Tuple: All the data of the contact.
        """
        
        if search_option == 1:
            return sorted(self.addressBooks[addressBook_name], key=lambda contact: contact.firstName)
        
        elif search_option == 2:
            return sorted(self.addressBooks[addressBook_name], key=lambda contact: contact.city)
        
        elif search_option == 3:
            return sorted(self.addressBooks[addressBook_name], key=lambda contact: contact.state)
        
        else:
            return None

    def search_Person_by_city_or_state(self, search_option, search_value):
        
        """
        Description:
            Search the person in all contact's details in the address book..
        Parameters:
            search_option (int): Int value to search by city or state
            search_value (str): The input value to search across all the addressbook  
        Return Type:
            person (dict): All the contact which matches the person name.
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
            Search the person in all contact's details in the address book..
        Parameters:
            search_option (int): Int value to search by city or state
            search_value (str): The input value to search across all the addressbook  
        Return Type:
            countOf_contacts (int): Count of the contacts which all matches the input values
        """
        
        countOf_countacts=0
        
        for addressBook, contacts in self.addressBooks.items():

            for contact in contacts:
                if (search_option == 1 and contact.city.lower() == search_value.lower()) or \
                   (search_option == 2 and contact.state.lower() == search_value.lower()):
                    countOf_countacts+=1
    
        return countOf_countacts
                 
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
                           "       6. Search person by city or state\n"+
                           "       7. Get Count of contacts by 'City' or 'State'\n"                                     
                           "       8. Exit\n"+
                           "option: "))
        
        if option == 1:
            
            addressbook_name=input("Enter the name of the new address book: ")
            print("-"*50+"\n"+addressbook_obj.create_Address_Book(addressbook_name)+"\n"+"-"*50)
            
        elif option == 2:
            
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
        
        elif option == 3:
            
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
            
        elif option == 4:
            
            print(addressbook_obj.display_all_addressBooks())
            
            addressbook_name=input("Enter one of the AddressBook(s) from above list to delete contact: ")
            
            firstName=input("Enter the contact firstName to delete: ")    
            print("-"*50+"\n"+addressbook_obj.delete_contact(addressbook_name,firstName)+"\n"+"-"*50)
        
        elif option == 5:
            
            search_option = int(input("Enter 1 to sort by 'First Name'\nEnter 2 to sort by 'City'\nEnter 3 to sort by 'State'\nOption: "))
            
            print(addressbook_obj.display_all_addressBooks())

            addressbook_name = input("Enter one of the AddressBook(s) from the above list to find all contacts: ")

            if addressbook_obj.addressBooks[addressbook_name]:
                contacts = addressbook_obj.display_all_contacts(addressbook_name,search_option)

                if not contacts:
                    print("Invalid input")
                
                else:    
                    for contact in contacts:
                        print("-"*50+"\n"+f'''First Name: {contact.firstName}\nLast Name: {contact.lastName}\nAddress: {contact.address}\nCity: {contact.city}\nState: {contact.state}\nZip: {contact.zip}\nPhone: {contact.phone}\nEmail: {contact.email}\n'''+"-"*50)

            else:
                print("-" * 50+"\n"+f'"{addressbook_name}" AddressBook is empty, please add contacts first.'+"\n"+"-" * 50)
        
        elif option == 6:
            search_option = int(input("Enter 1 to search by 'City'\nEnter 2 to search by 'State'\nOption: "))
            search_value = input("Enter the value to search: ")
            results = addressbook_obj.search_Person_by_city_or_state(search_option, search_value)
            
            if results:
                
                for addressBook, contacts in results.items():
                    
                    if contacts:
                        print("-"*50)
                        print(f"Address Book: {addressBook}")
                        for contact in contacts:
                            print(f"First Name: {contact.firstName}")
                            print(f"Last Name: {contact.lastName}")
                            print(f"City: {contact.city}")
                            print(f"State: {contact.state}")
                            print(f"Phone: {contact.phone}")
                            print(f"Email: {contact.email}")
                            print("-"*50)
                    else:
                        print(f"No matching contacts found in {addressBook}.")
            else:
                print(f"No matching contacts found in {search_value}.")
        
        elif option == 7:
            
            search_option = int(input("Enter 1 to search by 'City'\nEnter 2 to search by 'State'\nOption: "))
            search_value = input("Enter the value to search: ")
            
            print("-"*30+"\n"+f"{addressbook_obj.get_countOf_Person_by_city_or_state(search_option, search_value)} contact(s) found"+"\n"+"-"*30)
                    
        elif option == 8:
            print("Program exited!!!")
            return    
    
if __name__=="__main__":
    main()
    