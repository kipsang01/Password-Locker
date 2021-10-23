import password_locker
from user_class import User
import unittest


class Test_password_locker(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User('psang','1234') # create user

    
    def test_user(self):
        self.assertEqual(self.new_user.username, 'psang')
        self.assertEqual(self.new_user.password, '1234')
        
        
        
        
if __name__ == "__main__":
    unittest.main()
        