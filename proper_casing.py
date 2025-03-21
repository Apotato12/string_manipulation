# Program 5 Batch 5
# Atienza, Rein Gabriel
# BSCPE 1-2

def proper_casing():
    """Prompts the user to input their full name in incorrect casing and prints it in proper casing."""
    fullname = input("Please enter your full name in incorrect casing: ")
    
    correct_casing = fullname.title()
    
    print("Your name is:", correct_casing)

proper_casing()