number = int(input("Please enter a number (0-1000): "))

if 0 <= number <= 1000:
    formatted_number = f"{number:06}"
    
    print("Formatted number:", formatted_number)