#######################################################################
# Polymorphism Exercise 4
#######################################################################

class Median:
    def calculate_median(self, *args):
        # Convert the variable-length arguments into a list
        numbers = list(args)
        # Sort the numbers in ascending order
        numbers.sort()
        # Calculate the length of the list
        length = len(numbers)

        # Check if the length of the list is even
        if length % 2 == 0:
            # If even, calculate the average of the middle two numbers
            middle_left = numbers[length // 2 - 1]
            middle_right = numbers[length // 2]
            median = (middle_left + middle_right) / 2
        else:
            # If odd, the median is the middle number
            median = numbers[length // 2]

        return median

# Test code
if __name__ == "__main__":
    # Create an instance of Median
    m = Median()

    # Test the calculate_median method with various numbers of parameters
    print(m.calculate_median(3, 5, 1, 4, 2))  # Output: 3
    print(m.calculate_median(8, 6, 4, 2))  # Output: 5.0
    print(m.calculate_median(9, 3, 7))  # Output: 7
    print(m.calculate_median(5, 2))  # Output: 3.5
