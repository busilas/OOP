import turtle

t = turtle.Turtle()

def recursive_tree(branch_length, angle, t):
    """Draw a tree recursively"""
    if branch_length > 5:
        t.forward(branch_length)  # Draw the main branch
        t.right(angle)  # Turn right for the next branch
        recursive_tree(branch_length - 15, angle, t)  # Recursively draw a smaller branch
        t.left(angle * 2)  # Turn left for the branch to the left
        recursive_tree(branch_length - 15, angle, t)  # Recursively draw a smaller branch to the left
        t.right(angle)  # Turn right to align back
        t.backward(branch_length)  # Move back to the main branch
        
recursive_tree(45, 20, t)  # Start drawing the tree
turtle.mainloop()  # Keep the window open