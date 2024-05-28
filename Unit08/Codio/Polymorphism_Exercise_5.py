#######################################################################
# Polymorphism Exercise 5
#######################################################################

class Substitute:
    def __init__(self, source_file, answer_file):
        self.source_file = source_file
        self.answer_file = answer_file
        self.words = None
    
    def string_to_list(self):
        '''Read text file, turn it into a
        2D list of words for each line'''
        words = []
        with open(self.source_file, 'r') as file_object:
            lines = file_object.read().split('\n')
            for line in lines:
                words.append(line.split())
        self.words = words
    
    def list_to_string(self):
        '''Convert 2D list back into a 
        string with newline characters'''
        lines = []
        for line in self.words:
            lines.append(' '.join(line))
        string = '\n'.join(lines)
        self.words = string
      
    def swap_words(self):
        self.string_to_list()
        for line in self.words:
            for i in range(len(line)):
                if (i + 1) % 5 == 0:
                    word = line[i]
                    line[i] = 'HELLO'
        self.list_to_string()

class Stars(Substitute):
    def swap_words(self):
        # Convert the text from the source file into a 2D list
        self.string_to_list()

        # Loop through each line in the 2D list
        for line in self.words:
            # Loop through each word in the line
            for i in range(len(line)):
                # Check if the word is the third word (index 2) and has three letters
                if (i + 1) % 3 == 0 and len(line[i]) == 3:
                    # Replace the word with '*' characters matching the number of characters in the word
                    line[i] = '*' * len(line[i])

        # Convert the modified 2D list back into a string
        self.list_to_string()

        # Write the new string to the answer file
        with open(self.answer_file, 'w') as file_object:
            file_object.write(self.words)

# Test code
if __name__ == "__main__":
    # Create an instance of the Stars class
    stars = Stars(source_file='source.txt', answer_file='answer.txt')
    # Call the swap_words method to perform the word swapping
    stars.swap_words()
