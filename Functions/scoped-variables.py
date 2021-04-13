message1 = "Global Variable"

def myFunction():
    print("\nINSIDE THE FUNCTION")
    #Global variables are available inside a function
    print(message1)
    #Declaring a local variable
    message2 = "Local Variable"
    print(message2)
    
    
'''
As this function does not have any parameters
when we call it, we simply just write myFunction()
'''

myFunction()

print("\nOUTSIDE THE FUNCTION")
print(message1) #Global variables are accessible outside the function
#print(message2) # When uncommented this line will cause an error

message3 = "Global Variable (shares the same name as the local variable)"
def myScopedFunction():
    message3 = "Local Variable (shares the same name as the global variable)"
    print("\nINSIDE THE FUNCTION")
    print(message3)
myScopedFunction()
print("\nOUTSIDE THE FUNCTION")
print(message3)