pets = ['cats', 'dogs', 'hamster', 'tortoise']

for myPets in pets:
    print(myPets)

pets.append('rabbit')

for index, myPets in enumerate(pets):
    print(index, myPets)

age = {'Peter': 55, 'Jon': 30}

for i in age:
    print(i) # Prints off only Peter and Jon

for i in age:
    print("%s is %d years old" % (i, age[i])) # Prints off Peter is 55 years old

for i, j in age.items():
    print("Name = %s, Age = %d" % (i, j)) # Prints off Peter is 55 years old

message = 'Hello'

for i in message:
    print(i)

for i in range(3,10):
    print(i)

for i in range(5):
    print(i)
    
for i in range(2,10,2):
    print(i)
