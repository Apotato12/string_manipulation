fullname = input("Please enter your full name in incorrect casing: ")

capitalization = ''.join(word.capitalize() for word in fullname.split())

print("Your name in Pascal Case is:" + capitalization)