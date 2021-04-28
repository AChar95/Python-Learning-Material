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
            while True:
                try:
                    userResult = input("Please enter %i in binary: " %(base10))
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
                