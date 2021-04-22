import os

def printInstructions(instruction):
    print(instruction)

def getUserScore(userName):
    try:
        scoresFile = open('userScores.txt', 'r')
        for line in scoresFile:
            content = line.split(", ")
            if (content[0] == userName):
                scoresFile.close()
                return content[1]
            scoresFile.close()
            return "-1"
    except IOError:
        print("File userScores.txt cannot be found, creating new file")
        scoresFile = open('userScores.txt', 'w')
        scoresFile.writelines(["Ann, 100", "\nBenny, 102", "\nCarol, 214", "\nDarren, 129"])
        scoresFile.close()
        return "-1"

def updateUserScore(newUser, userName, score):
    if newUser == True:
        scoresFile = open('userScores.txt', 'a')
        scoresFile.write("\n%s, %s" %(userName, score))
        scoresFile.close()
    else:
        scoresFile = open('userScores.txt', 'r')
        tempFile = open(('userScores.tmp', 'w'))
        for line in scoresFile:
            content = line.split(", ")
            if content[0] == userName:
                tempFile.write(userName + ", " + score + "\n")
            else:
                tempFile.write(line)
            
        scoresFile.close()
        tempFile.close()
        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')