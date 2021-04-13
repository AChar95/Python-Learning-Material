f = open('myfile.txt','r') # r -> read mode,     w -> write mode,    a -> append    r+ -> read & write
firstLine = f.readline()
secondLine = f.readline()
print(firstLine)
print(secondLine)


for line in f:
    print(line, end = '') # readline appends \n to the end of the line, using the end = '' will remove that
    
f.close()