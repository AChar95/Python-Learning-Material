import os, csv, sys, random as rand


class magic8ball:
    def __init__(self, name):
        self.name = name
        self.__mQuestions = []
    
    def __startGame(self):
        print("Hello " + self.name)
        uQuestion = True
        answers = ("IT IS CERTAIN", "YOU MAY RELY ON IT", "AS i SEE IT, YES", "OUTLOOK LOOKS GOOD", "MOST LIKELY", "IT IS DECIDEDLY SO", "WITHOUT A DOUBT", "YES DEFINITELY")
        while  uQuestion:
            userQuestion = input("Please ask a question: ")
            if len(userQuestion) > 0:
                self.__mQuestions.append(userQuestion)
                print(answers[rand.randint(0,len(answers)-1)])
            else:
                print("Thank you for playing")
                self.__writeQuestions()
                sys.exit
    
    def __writeQuestions(self):
        try:
            fileName = self.name + ".csv"
            testFile = os.path.isfile(fileName +".csv")
            if testFile == False:
                print("Creating your Question file")    
            file = open(fileName, "a+", newline="")
            wrt = csv.writer(file)
            for question in self.__mQuestions:
                wrt.writerow(question)
            file.close()
            
        except IOError:
            newFile = open(fileName, 'w')
            