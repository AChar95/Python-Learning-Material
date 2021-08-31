def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck % x == 0):
            return False
    return True


answer = checkIfPrime(13)

print(answer)

# Alternative function that uses the return

def addNums(arg1, arg2):
    total = arg1 + arg2
    return total

newTotal = addNums(3,6) # This is useful to reuse the variable or to call it elsewhere

print(newTotal)