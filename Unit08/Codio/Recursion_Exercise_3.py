#######################################################################
#Recursion Exercise 3
#######################################################################

def bunny_ears(bunnies):
    # Base case: If there are no bunnies, return 0 ears
    if bunnies == 0:
        return 0
    else:
        # Recursive case: Return 2 ears for the current bunny 
        # and add the ears of the rest of the bunnies (bunnies - 1)
        return 2 + bunny_ears(bunnies - 1)

# Test cases
print(bunny_ears(8))  # Output: 16
print(bunny_ears(0))  # Output: 0