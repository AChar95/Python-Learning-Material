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
    import randint from random
    
    def generateQuestions(self, score = 0):