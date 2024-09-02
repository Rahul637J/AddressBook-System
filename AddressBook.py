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
        self.contacts=dict()
    
    def add_Contact(self,userName,contact):
        self.contacts[userName]=contact
             
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
            
            obj.add_Contact(user_data[0],Contact(*user_data))

        if option == 2:
            print("Program exited!!!")
            return    
    
if __name__=="__main__":
    main()
