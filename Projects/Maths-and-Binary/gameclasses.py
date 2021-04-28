class Game:
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions
    
    @property
    def noOfQuestions(self):
        return self._noOfQuestions
    
    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            print("Minimum number of Questions = 1\nSetting the number of questions to 1")
            self._noOfQuestions = 1
        elif value > 10:
            print("Maximum number of Questions = 10\nSetting the number of questions to 10")
            self._noOfQuestions = 10
        else:
            self._noOfQuestions = value

class BinaryGame:
    def generateQuestions(self):
        from random import randint
        score = 0
        for i in range(self.noOfQuestions):
            base10 = randint(1,100)
            userResult = input("Please enter %i in binary: " %(base10))
            while True:
                try:
                    answer = int(userResult, base=2)
                    if answer == base10:
                        print("Congradulations, you have given the correct answer")
                        self.score += 1
                        break
                    else:
                        print("That was incorrect, the correct answer is {:b}.".format(base10))
                        break
                except:
                    print("The value you provide %s, is not binary, please try again" %(userResult))
                    userResult = input("Please enter a new value for %i in binary: " %(base10))
        return score

class MathsGame:
    def generateQuestions(self):
        from random import randint
        score = 0
        numberList = [0,0,0,0,0]
        symbolList = ['','','','']
        operatorList = {1:"+", 2:"-", 3:"*", 4:"**"}
        for i in range(self.noOfQuestions):
            for index in range(0,4):
                numberList[index] = randint(1,9)
            for index in range(0,4):
                if index > 0 and symbolList[index-1] == "**":
                    symbolList[index] = operatorList[randint(1,3)]
                else:
                    symbolList[index] = operatorList[randint(1,4)]
            questionList = str(numberList[0])
            for z in range(0,4):
                if z+1 <= 5:
                    questionList = questionList + symbolList[z] + str(numberList[z+1])
                else:
                    break
            result = eval(questionList)
            questionList.replace("**", "^")
            userResult = input("Please evaluate %s: " %(questionList))
            while True:
                try:
                    answer = int(userResult)
                    if userResult == result:
                        print("Congradulations, you got the answer correct")
                        score += 1
                        break
                    else: 
                        print("Incorrect the correct answer is %i" %(result))
                        break
                except:
                    print("The value provided %s, is not a valid integer. Please try again" %(userAnswer))
                    userResult = input("Please enter a new answer for %s: " %(questionList))
        return score

                