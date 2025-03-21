# Program 1 Batch 5
# Atienza, Rein Gabriel
# BSCPE 1-2

def name():
    """Prompts the user to input their full name and prints it without leading spaces."""
    fullname = input("Please enter your name with spaces on the start: ")
    space_remove = fullname.lstrip()

    print("Your name is: " + space_remove)

name()