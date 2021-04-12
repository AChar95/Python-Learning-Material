myName = input("Please enter your name: ")
myAge = input("Please enter your age: ")

print("Hello World, my name is", myName, "and I am", myAge, "years old")

myAge2 = input("Hi %s, please enter your age:" %(myName))
myAge3 = input("Hi {}, please enter your age:".format(myName))

print("Hello World, my name is %s and I am %i years old" %(myName, int(myAge)))

print('''Hello World,
My name is James and 
I am 20 years old.''') # This is how you can do a multi-line output

print("Hello\tWorld") #\ is an escape character, allowing additional functionality such as \t for tab, \n for new line
print("Hello\nWorld")
print("\\") # prints \
print("I am 5'11\" tall") # when using " for a string \" will let you add " to the string
print('I am 5\'11" tall') # when using ' for a string \' will let you add ' to the string
print(r'Hello\tWorld') # This will write out the raw string, e.g. Hello\tWorld rather than Hello   World