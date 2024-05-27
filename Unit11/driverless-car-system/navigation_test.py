import unittest
from navigation import Navigation

class TestNavigation(unittest.TestCase):
    """
    Unit test case for testing the Navigation class.
    """

    def setUp(self):
        """
        Set up the test case environment. Initialize the Navigation instance.
        """
        self.navigation = Navigation()

    def test_initialization(self):
        """
        Test if the Navigation instance is initialized with an empty route.
        """
        # Check if the initial route is an empty list
        self.assertEqual(self.navigation.route, [])

    def test_plan_route(self):
        """
        Test the plan_route method of the Navigation class.
        """
        start = (34.052235, -118.243683)  # Los Angeles coordinates
        destination = (36.169941, -115.139832)  # Las Vegas coordinates
        # Plan a route from start to destination
        route = self.navigation.plan_route(start, destination)
        # Check if the planned route is correct
        self.assertEqual(route, [start, destination])
        # Check if the route attribute is correctly updated
        self.assertEqual(self.navigation.route, [start, destination])

    def test_get_next_waypoint(self):
        """
        Test the get_next_waypoint method of the Navigation class.
        """
        start = (34.052235, -118.243683)  # Los Angeles coordinates
        destination = (36.169941, -115.139832)  # Las Vegas coordinates
        # Plan a route from start to destination
        self.navigation.plan_route(start, destination)
        # Check if the next waypoint is the start point
        self.assertEqual(self.navigation.get_next_waypoint(), start)
        # Check if the next waypoint is the destination
        self.assertEqual(self.navigation.get_next_waypoint(), destination)
        # Check if there are no more waypoints
        self.assertIsNone(self.navigation.get_next_waypoint())

    def test_has_reached_destination(self):
        """
        Test the has_reached_destination method of the Navigation class.
        """
        # Initially, the destination should be considered reached
        self.assertTrue(self.navigation.has_reached_destination())
        start = (34.052235, -118.243683)  # Los Angeles coordinates
        destination = (36.169941, -115.139832)  # Las Vegas coordinates
        # Plan a route from start to destination
        self.navigation.plan_route(start, destination)
        # Check if the destination has not been reached after planning the route
        self.assertFalse(self.navigation.has_reached_destination())
        # Move to the next waypoint (start point)
        self.navigation.get_next_waypoint()
        # Move to the next waypoint (destination)
        self.navigation.get_next_waypoint()
        # Check if the destination is reached after visiting all waypoints
        self.assertTrue(self.navigation.has_reached_destination())

    def test_calculate_distance(self):
        """
        Test the calculate_distance method of the Navigation class.
        """
        point1 = (34.052235, -118.243683)  # Los Angeles coordinates
        point2 = (36.169941, -115.139832)  # Las Vegas coordinates
        # Calculate the distance between point1 and point2
        distance = self.navigation.calculate_distance(point1, point2)
        # Expected distance calculated using Euclidean distance formula
        expected_distance = ((36.169941 - 34.052235)**2 + (-115.139832 - -118.243683)**2)**0.5
        # Check if the calculated distance is almost equal to the expected distance
        self.assertAlmostEqual(distance, expected_distance)

if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
