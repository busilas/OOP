#######################################################################
#Recursion Exercise 4
#######################################################################

def reverse_string(input_string):
    # Base case: If the string is empty or has only one character, return the string itself
    if len(input_string) <= 1:
        return input_string
    else:
        # Recursive case: Return the last character of the string concatenated with the reversed rest of the string
        return input_string[-1] + reverse_string(input_string[:-1])

# Test cases
print(reverse_string("cat"))    # Output: tac
print(reverse_string("house"))  # Output: esuoh