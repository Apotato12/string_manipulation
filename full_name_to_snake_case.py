fullname = input("Please enter your full name in incorrect casing: ")

snake = '_'.join(word.lower() for word in fullname.split())

print("Your name in snake case is:" + snake)