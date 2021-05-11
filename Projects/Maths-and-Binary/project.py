from gamesclasses import Game, BinaryGame, MathsGame
from gametask import printInstructions, getUserScore, updateUserScore

try:
    mathsInstructions = ''' In This game, you will be given a simple arithmetic question.
    Each correct answer gives you one point.
    No points are deducted for wrong answers.'''
    binaryInstructions = '''In this game, you will be given a number in base 10.
    Your task is to convert this value into base 2.
    Each correct answer gives you one point.
    No points are deducted for wrong answers.'''

    bg = BinaryGame()
    mg = MathsGame()
    userName = input("Please enter your name: ")
    score = int(getUserScore(userName))
    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False
    print("Hello %s, your score is %i" % (userName, score))
    userChoice = 0
    while userChoice != "-1":
        game = input("Please pick a game: Maths Game (1) or Binary Game (2): ")
        if game != "1" or game != "2":
            print("You have not selected a valid game type")
        while True:
            try:
                numQuestions = input("Please select the number of questions between 1 to 10")
                num = int(numQuestions)
                break
            except:
                print("The value %s is not a valid number please try again")
                numQuestions = input("Please select a valid number of questions between 1 to 10")
        if game == "1":
            mg.noOfQuestions = num
            printInstructions(mathsInstructions)
            score = score + mg.generateQuestions()
        else:
            bg.noOfQuestions = num
            printInstructions(binaryInstructions)
            score = score + bg.generateQuestions()
        print("Your score is: %i" %(score))
        userChoice = input("Do you wish to quit the game enter -1")
except Exception as e:
