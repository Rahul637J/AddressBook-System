
'''

@Author: Rahul 
@Date: 2024-09-02
@Last Modified by: Rahul 
@Last Modified time: 2024-09-02
@Title: Employee wages - Python program to perform AddressBook operation.  

'''

from Mylog import logger_init 

log = logger_init("UC_1")

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
             
def main():

    log.info("Ability to create contact")
    print("-"*35+"\n| Welcome to Address Book Program |\n"+"-"*35+"\n")
    
if __name__=="__main__":
    main()
    