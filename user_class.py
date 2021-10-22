from credentials_class import Credential
class User:
    credentials = []
     
    def __init__(self,username, password):
        self.username  = username
        self.password = password
     
     #create credentials   
    def create_new_credential(self, acc_name, acc_username, acc_password):
        new_credential = Credential(acc_name, acc_username, acc_password )
        self.credentials.append(new_credential)
        print("New Credential saved successfully")
        
       #return credentials 
    def see_credentials(self):
        i = 0
        for credential in self.credentials:
            print( str(i) +'  Account: '+credential.acc_name +' Username: '+ credential.acc_username +' Password: '+ credential.acc_password)
            i +=1
            
    #Delete credential
    def delete_credential(self,index):
        self.credentials.pop(index)
        print('Remaining Credentials:')
        self.see_credentials()