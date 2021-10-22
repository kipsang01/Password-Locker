import string
from random import *

def main():
    
    users = []
    
    #function to display choices
    def show_options():
        print('Choose what you want to do:\n\
                1. Create new Credential \n\
                2. Display saved Credentials\n\
                3. Delete a Credential\n\
                4. Log Out\n\
                5. Exit')
        
        
    #function login
    def login():
        print('please login now:')
        verify_username = input('Username: ')
        verify_password = input('Password: ')
        
        if verify_username not in users:
            print('User does not exist.Create account first')
            main()
            
        #verify login details
        while verify_username != new_user.username or verify_password != new_user.password:
            print("invalid credentials! Try again")
            verify_username = input('Username: ')
            verify_password = input('Password: ')   
        
    
    #function to generate password  
    def generate_Password():
        characters = string.ascii_letters + string.punctuation  + string.digits
        password =  "".join(choice(characters) for x in range(randint(8, 16)))
        return password  
    
    
    #function for main actions
    def main_actions():    
        show_options()
        option = input()
    
if __name__ == '__main__':
    
    main()