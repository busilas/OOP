class Navigation:
    """
    Manages navigation and path planning for the driverless car.

    Attributes:
        route (list): A list of waypoints representing the planned route.
    """

    def __init__(self):
        """
        Initializes a Navigation instance.
        """
        self.route = []

    def plan_route(self, start, destination):
        """
        Plan a route from the start location to the destination.

        Args:
            start (tuple): The starting coordinates (latitude, longitude).
            destination (tuple): The destination coordinates (latitude, longitude).

        Returns:
            list: A list of waypoints from start to destination.
        """
        # For simplicity, this function generates a direct path with dummy waypoints
        self.route = [start, destination]
        return self.route

    def get_next_waypoint(self):
        """
        Get the next waypoint in the planned route.

        Returns:
            tuple: The next waypoint coordinates (latitude, longitude), or None if route is empty.
        """
        if self.route:
            return self.route.pop(0)
        return None

    def has_reached_destination(self):
        """
        Check if the destination has been reached.

        Returns:
            bool: True if the route is empty, indicating destination reached; False otherwise.
        """
        return not self.route

    def calculate_distance(self, point1, point2):
        """
        Calculate the distance between two points.

        Args:
            point1 (tuple): The first point coordinates (latitude, longitude).
            point2 (tuple): The second point coordinates (latitude, longitude).

        Returns:
            float: The distance between the two points.
        """
        # Simplified distance calculation for demonstration purposes
        lat_diff = point2[0] - point1[0]
        lon_diff = point2[1] - point1[1]
        return (lat_diff**2 + lon_diff**2)**0.5
