userInput = input("Please enter either 1 or 2: ")

if userInput == "1":
    print("Hello World")
    print("How cool is this?")
elif userInput == "2":
    print("Python is easy to learn")
    print("It's lots of fun")
else:
    print("You did not enter a valid number")

num1 = 12 if userInput == "1" else 13
print(num1)