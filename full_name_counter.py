# Program 8 Batch 5
# Atienza, Rein Gabriel
# BSCPE 1-2

def characters_in_fullname():
    """Prompts the user to input their full name and prints the number of characters in the input."""
    fullname = input("Please enter your full name: ")
    
    letter = len(fullname) 
    
    print("Number of characters in the full name:", letter)

characters_in_fullname()