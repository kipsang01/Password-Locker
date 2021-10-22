from credentials_class import Credential
class User:
    credentials = []
     
    def __init__(self,username, password):
        self.username  = username
        self.password = password
        
    def create_new_credential(self, acc_name, acc_username, acc_password):
        new_credential = Credential(acc_name, acc_username, acc_password )
        self.credentials.append(new_credential)
        print("New Credential saved successfully")