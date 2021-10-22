from credentials_class import Credential
from user_class import User
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
        
        if option == '1':
            print('Create new credential:')
            acc_name = input('Enter account name:  ')
            acc_username = input('Enter account Username:  ')
            
            print('Choose password method:\n\
                    1. Input your own Password\n\
                    2. Use system generated password\n')
            password_choice = input('')
            #allow password from user
            if password_choice == '1':
                acc_password = input('Enter password:')
            #generate password  for user
            elif password_choice == '2':
                acc_password = generate_Password()
            else:
                print('invalid input')
                print('Choose password method:\n\
                    1. Input your own Password\n\
                    2. Use system generated password\n')
                
                password_choice = input(' Option: ')
                
            new_user.create_new_credential(acc_name, acc_username, acc_password)
            
            main_actions()
            
        # viewing created credentials  
        elif option == '2':
            new_user.see_credentials()
            
            main_actions()
            
           # deleting a credential
        elif option == '3':
            print('Select the credential you want to delete:')
            new_user.see_credentials()
            length = len(new_user.credentials)
            index = int(input('Option: '))
            while index not in range(0,length) :
                print('invalid selection. Try again')
            new_user.delete_credential(index)
            
            main_actions()
            
        elif option == '4':
            login()
            main_actions()
            
        elif option == '5':
            exit()
        else:
            print('invalid input')
            main_actions()   
     
     
     #start of the program       
    print('Welcome to Password Locker\n Please choose to:\n 1: Create Account\n 2: Login\n 3: Exit')
    user_option =  input()
    
    if user_option == '1':
        
        username = input('Enter your preferred username:  ')
        password = input('Enter your preferred Password:  ')
         
         #save user name and password
        new_user = User(username, password)
        users.append(new_user.username)
        
        login()     
                
          #calling main function  
        main_actions()   
    
if __name__ == '__main__':
    
    main()