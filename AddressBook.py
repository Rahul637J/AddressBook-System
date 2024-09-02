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
             
def main():
    
    obj=AddressBook()

    print("-"*35+"\n| Welcome to Address Book Program |\n"+"-"*35+"\n")
    
    while True:
        option = int(input("Enter :\n"+
                           "       1. Add Contact\n"+
                           "       2. Exit\n"+
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
            
            obj.add_Contact(Contact(*user_data))

        if option == 2:
            print("Program exited!!!")
            return    
    
if __name__=="__main__":
    main()
