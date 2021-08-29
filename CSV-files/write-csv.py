import csv

newRow = ["1004","Neil", "Harris", "HR"]
file = open("example.csv", "a")

wrt = csv.writer(file)
wrt.writerow(newRow)
file.close()