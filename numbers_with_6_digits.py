# Program 2 Batch 5
# Atienza, Rein Gabriel
# BSCPE 1-2

def number_6_digits():
    """Prompts the user to input a number (0-1000) and prints it in 6-digit format."""
    number = int(input("Please enter a number (0-1000): "))
    

    if 0 <= number <= 1000:
        formatted_number = f"{number:06}"
        print("Formatted number:", formatted_number)

number_6_digits()