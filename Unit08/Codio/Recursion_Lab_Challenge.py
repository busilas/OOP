def recursive_power(base, exponent):
    # Base case: If the exponent is 0, return 1
    if exponent == 0:
        return 1
    # Recursive case for positive exponents
    elif exponent > 0:
        # Recursively multiply base with recursive_power(base, exponent - 1)
        return base * recursive_power(base, exponent - 1)
    # Recursive case for negative exponents
    else:
        # Calculate 1 divided by recursive_power(base, -exponent) for negative exponents
        return 1 / recursive_power(base, -exponent)

# Test cases
print(recursive_power(5, 3))  # Output: 125
print(recursive_power(4, 5))  # Output: 1024