fullname = input("Please enter your full name in incorrect casing: ")

reverse_casing = "".join(char.swapcase() for char in fullname)

print("your name is : " + reverse_casing)