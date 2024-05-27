import unittest
from unittest.mock import patch, MagicMock
from driverless_car_system import DriverlessCarSystem
from passenger_interaction import User, PassengerInteraction

class TestDriverlessCarSystem(unittest.TestCase):
    """
    Unit test class for the DriverlessCarSystem class.
    """

    def setUp(self):
        """
        Set up the test case with an instance of DriverlessCarSystem.
        """
        self.system = DriverlessCarSystem()

    @patch('builtins.input', side_effect=['testuser', 'testpassword'])
    @patch('builtins.print')
    @patch('passenger_interaction.User.__init__', lambda self: None)
    def test_login_successful(self, mock_print, mock_input):
        """
        Test successful login with correct username and password.
        """
        # Create a test user and add to the system's user list
        user = User()
        user.account_name = 'testuser'
        user.password = 'testpassword'
        user.first_name = 'Test'
        user.last_name = 'User'
        self.system.users.append(user)

        # Mock the verify_password method to return True
        with patch.object(User, 'verify_password', return_value=True):
            self.system.login()

        # Check that the current user is set correctly and login message is printed
        self.assertEqual(self.system.current_user, user)
        mock_print.assert_called_with('Login successful! Welcome Test User.')

    @patch('builtins.input', side_effect=['testuser'])
    @patch('builtins.print')
    def test_login_user_not_found(self, mock_print, mock_input):
        """
        Test login attempt with a username that is not found in the system.
        """
        # Attempt to log in with a non-existent user
        self.system.login()
        # Ensure no user is logged in and correct error message is printed
        self.assertIsNone(self.system.current_user)
        mock_print.assert_called_with('User not found. Please sign up first.')

    @patch('builtins.input', side_effect=['testuser', 'wrongpassword'])
    @patch('builtins.print')
    @patch('passenger_interaction.User.__init__', lambda self: None)
    def test_login_incorrect_password(self, mock_print, mock_input):
        """
        Test login attempt with correct username but incorrect password.
        """
        # Create a test user and add to the system's user list
        user = User()
        user.account_name = 'testuser'
        user.password = 'testpassword'
        user.first_name = 'Test'
        user.last_name = 'User'
        self.system.users.append(user)

        # Mock the verify_password method to return False
        with patch.object(User, 'verify_password', return_value=False):
            self.system.login()

        # Ensure no user is logged in and correct error message is printed
        self.assertIsNone(self.system.current_user)
        mock_print.assert_called_with('Incorrect password. Please try again.')

    @patch('builtins.print')
    @patch('passenger_interaction.User.__init__', lambda self: None)
    def test_logout(self, mock_print):
        """
        Test logging out when a user is currently logged in.
        """
        # Create a test user and set as the current user
        user = User()
        user.account_name = 'testuser'
        user.first_name = 'Test'
        user.last_name = 'User'
        self.system.current_user = user
        # Perform logout
        self.system.logout()
        # Ensure no user is logged in and logout message is printed
        self.assertIsNone(self.system.current_user)
        mock_print.assert_called_with('Logging out user: testuser')

    @patch('builtins.print')
    def test_logout_no_user_logged_in(self, mock_print):
        """
        Test logging out when no user is currently logged in.
        """
        # Attempt to log out with no current user
        self.system.logout()
        # Ensure correct message is printed
        mock_print.assert_called_with('No user is currently logged in.')

    @patch('builtins.input', side_effect=['FirstName', 'LastName', 'accountname', 'password', 'email@example.com'])
    @patch('builtins.print')
    @patch('passenger_interaction.User.__init__', lambda self: None)
    def test_signup(self, mock_print, mock_input):
        """
        Test user signup with valid details.
        """
        # Perform user signup
        self.system.signup()
        # Ensure one user is added to the system and success message is printed
        self.assertEqual(len(self.system.users), 1)
        mock_print.assert_called_with('User signed up successfully!')

if __name__ == '__main__':
    unittest.main()
