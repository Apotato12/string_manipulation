# Program 9 Batch 5
# Atienza, Rein Gabriel
# BSCPE 1-2

def pascal_case():
    """Prompts the user to input their full name in incorrect casing and prints it in Pascal Case."""
    fullname = input("Please enter your full name in incorrect casing: ")
    
    capitalization = ''.join(word.capitalize() for word in fullname.split())
    
    print("Your name in Pascal Case is: " + capitalization)

pascal_case()