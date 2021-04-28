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
    print("Hello %s, your score is %i" %(userName, score))
    userChoice = 0
    while userChoice != "-1":
        game = input("Please pick a game: Maths Game (1) or Binary Game (2): ")
        if game != "1" or gmae != "2":
            print("You have not selected a valid game type")
            
        
except Exception as e: