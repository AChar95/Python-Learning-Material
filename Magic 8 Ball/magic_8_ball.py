import sys as s
import random as rand

answer = ("IT IS CERTAIN", "YOU MAY RELY ON IT", "AS i SEE IT, YES", "OUTLOOK LOOKS GOOD", "MOST LIKELY", "IT IS DECIDEDLY SO", "WITHOUT A DOUBT", "YES DEFINITELY")
questions = True

while questions:
    ques = input("Please enter your question here: (Press Enter to exit) ")
    if len(ques) > 0: 
        print(answer[rand.randint(0, len(answer)-1)])
    else:
        s.exit

