# Program 10 Batch 5
# Atienza, Rein Gabriel
# BSCPE 1-2

def snake_case():
    """Prompts the user to input their full name in incorrect casing and prints it in snake case."""
    fullname = input("Please enter your full name in incorrect casing: ")
    
    snake = '_'.join(word.lower() for word in fullname.split())
    
    print("Your name in snake case is: " + snake)

snake_case()