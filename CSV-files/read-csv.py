import csv

file = open("example.csv", "r")

reading = csv.reader(file, delimiter=",")
for line in reading:
    print(line)
    
file.close