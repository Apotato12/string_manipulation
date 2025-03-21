# Program 6 Batch 5
# Atienza, Rein Gabriel
# BSCPE 1-2
def reverse_casing():
    """asks the user to input their full name in incorrect casing and prints each character with reversed casing."""
    fullname = input("Please enter your full name in incorrect casing: ")

    reverse_casing = "".join(char.swapcase() for char in fullname)

    print("your name is : " + reverse_casing)

reverse_casing()