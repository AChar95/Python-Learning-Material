def someFunction(a, b, c=1, d=2, e=3): # formal parameters
    print(a, b, c, d, e)


'''    
Here the function cannot exist as parameters with a default value should be last:
def someIncorrectFunction(p, q=1, r):
    print(p, q, r)
def someCorrectFunction(p, r, q=1):
    print(p, q, r)
'''
someFunction(10, 20)

def addNumbers(*num): # takes in a random amount of values (non-keyword variables)
    sum = 0
    for i in num:
        sum += i
    print(sum)

addNumbers(1,2,3,4,5)

def printMemberAge(**age): # This allows you to take in a random amount of key=value pairs (keyword variables)
    for i, j in age.items():
        print("Name = %s, Age = %s" %(i,j))

printMemberAge(Peter = 30, Jon = 90)

'''
When a function can take in formal, nonkeyworded and keyword variables
Then the following must be used:
def someFunction(farg, *args, **kwargs):
'''