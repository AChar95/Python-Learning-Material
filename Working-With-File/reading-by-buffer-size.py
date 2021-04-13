inputFile = open('myfile.txt', 'r')
outputFile = open('myoutputfile.txt', 'w')

msg = inputFile.read(10)
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10) # The 10 here is the number of bytes python will read at one pass

inputFile.close()
outputFile.close()