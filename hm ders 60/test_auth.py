import unittest
from auth import Authentiactor

class TestAuthenticator(unittest.TestCase):

    def setUp(self):
        self.auth = Authentiactor()

    def test_successful_login(self):
        self.assertTrue(self.auth.login("metehan", "gamerboy"))

    def test_wrong_password(self):
        self.assertFalse(self.auth.login("admin", "wrong"))

    def test_nonexistent_user(self):
        self.assertFalse(self.auth.login("nonexistent", "12345"))

if __name__ == '__main__':
    unittest.main()