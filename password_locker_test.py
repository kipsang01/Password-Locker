import password_locker
from user_class import User
import unittest


class Test_password_locker(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User('psang','1234') # create user
        self.new_user.create_new_credential( 'Twitter', 'psang254', '0000')

    
    def test_user(self):
        self.assertEqual(self.new_user.username, 'psang')
        self.assertEqual(self.new_user.password, '1234')
        
    def test_credential_created(self):
        self.assertEqual(len(self.new_user.credentials),1) 
        
    def test_delete_credential(self):
        self.new_user.credentials =[{ 'Facebook', 'psang254', '22334'}]
        self.new_user.delete_credential(0)
        self.assertEqual(len(self.new_user.credentials),0)
        
        
if __name__ == "__main__":
    unittest.main()
        