userAge = 30 # integer
userHeight = 1.8 # float
userFirstName = "Peter" # string literal
otherUserFirstName = 'Laura' # string literal too
userLastName = "Chan"
userName = userFirstName + userLastName # Combines/Concatenates two strings
print(userName)
print(userFirstName.upper())

brand = 'AMD'
exchangeRate = 1.235235245

message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD tp 1 EUR' %(brand, 1299, exchangeRate) #This string uses placeholders (%) where the number in front of the letter (4.2f) represents the length of the value, and .2 repsents the number of decimal place
print(message)

message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.3f} USD tp 1 EUR'.format('AMD', 1299, 1.235235245)
print(message)

message = 'The price of this {} laptop is {} USD and the exchange rate is {} USD tp 1 EUR'.format('AMD', 1299, 1.235235245) # unformated inputs, here the interpreter will input the values in the order they are given in the format( ### ) 
print(message)