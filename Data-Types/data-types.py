userAge = 30 # integer
userHeight = 1.8 # float
userFirstName = "Peter" # string literal
otherUserFirstName = "Laura" # string literal too
userLastName = "Chan"
userName = userFirstName + userLastName # Combines/Concatenates two strings
print(userName)
print(userFirstName.upper())

brand = "AMD"
exchangeRate = 1.235235245

message = "The price of this %s laptop is %d USD and the exchange rate is %4.2f USD tp 1 EUR" %(brand, 1299, exchangeRate) #This string uses placeholders (%) where the number in front of the letter (4.2f) represents the length of the value, and .2 repsents the number of decimal place
print(message)

message = "The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.3f} USD tp 1 EUR".format("AMD", 1299, 1.235235245)
print(message)

message = "The price of this {} laptop is {} USD and the exchange rate is {} USD tp 1 EUR".format("AMD", 1299, 1.235235245) # unformated inputs, here the interpreter will input the values in the order they are given in the format( ### ) 
print(message)

int("2") # this will convert the value to 2.05 
str(2.05) # this will effectively convert it to "2.05"
float("2") # This will return 2.0
float(2)  # This will return 2.0
userAgeList = [30,25,50,55,21]
user1Age = userAgeList[1] 
print(user1Age) # Will return 25

user2Age = userAgeList[2:5] # this will slice the array and return 50,55,21 [#:n!] # will indicate the index from the original array that the new array will start from. n this is the end value of the array, and is n-1 of the original array

del userAgeList[2] # this will return the following array [30,25,55,21]
userAgeList.append(5) # This will return the following array [30,25,55,21,5]
userAgeList[3] = 23 # This will return the following array [30,25,55,23,5]

# Tuples are a list of values whose values cannot be modified
monthsOfTheYear = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
print(monthsOfTheYear[1]) # Feb
print(monthsOfTheYear[-3]) # Oct

# Dictionary is a list of key: value pairs
userDictionary = { "Peter":50, "John":31, "Alex":40, "Alvin":"Not Available"}
print(userDictionary["Alex"]) # 40

userDictionary = dict(Peter=50, John=31, Alex=40, Alvin="Not Available")
print(userDictionary["Alvin"]) # Not Available

userDictionary["Alvin"] = 21 # This reassigns 21 to Alvin, overwriting "Not Available"
print(userDictionary["Alvin"]) # 21

emptyDictionary = { } # empty dictionary
print(emptyDictionary)
emptyDictionary["Jon"] = 40
print(emptyDictionary)

del emptyDictionary["Jon"] # this will return an empty dictionary
print(emptyDictionary)