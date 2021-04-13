inputFile = open('GitHub-Mark-Light-120px-plus.jpg', 'rb')
outputFile = open('myotherimage.jpg', 'wb')

img = inputFile.read(10)
while len(img):
    outputFile.write(img)
    img = inputFile.read(10)
    
inputFile.close()
outputFile.close()

remove('GitHub-Mark-Light-120px-plus.png') # will remove file GitHub-Mark-Light-120px-plus.png
rename('GitHub-Mark-Light-120px-plus.jpg', 'GitHub-Mark.jpg')