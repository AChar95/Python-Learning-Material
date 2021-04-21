import os

def printInstructions(instruction):
    print(instruction)

def getUserScore(userName):
    try:
        scores = open('userScores.txt', 'r')
        for line in scores:
            content = line.split(", ")
            if (content[0] == userName):
                scores.close()
                return content[1]
            scores.close()
            return "-1"
    except IOError:
        print("File userScores.txt cannot be found, creating new file")
        scores = open('userScores.txt', 'w')
        scores.writelines(["Ann, 100", "\nBenny, 102", "\nCarol, 214", "\nDarren, 129"])
        scores.close()
        return "-1"

def updateUserScore(newUser, userName, score):
    if (newUser == True):
        scores = open('userScores.txt', 'a')
        scores.write("\n%s, %s" %(userName, score))
        scores.close()
    else:
        scores = open('userScores.txt', 'r')
        tempFile = open(('userScores.tmp', 'w'))
        for line in scores:
            content = line.split(", ")
            if (content[0] == userName):
                content[1] = score
            scores.writeline([content[0], ", " content[1]])
        scores.close()
        tempFile.close()