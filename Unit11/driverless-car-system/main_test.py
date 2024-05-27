import unittest
from unittest.mock import patch, MagicMock
from driverless_car_system import DriverlessCarSystem

class TestDriverlessCarSystem(unittest.TestCase):
    """
    Unit test case for testing the DriverlessCarSystem class.
    """

    def setUp(self):
        """
        Set up the test case environment. Initialize the DriverlessCarSystem instance.
        """
        self.system = DriverlessCarSystem()

    @patch.object(DriverlessCarSystem, 'main_menu')
    def test_main_menu_called(self, mock_main_menu):
        """
        Test if the 'main_menu' method is called exactly once.
        
        Args:
            mock_main_menu (MagicMock): Mocked 'main_menu' method of DriverlessCarSystem.
        """
        # Call the main_menu method
        self.system.main_menu()
        # Check if the main_menu method was called once
        mock_main_menu.assert_called_once()

    def test_driverless_car_system_initialization(self):
        """
        Test if the DriverlessCarSystem instance is correctly initialized.
        """
        # Check if the system is an instance of DriverlessCarSystem
        self.assertIsInstance(self.system, DriverlessCarSystem)

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
