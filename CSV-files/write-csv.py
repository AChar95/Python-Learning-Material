import csv

newRow = ["1004","Neil", "Harris", "HR"]
file = open("example.csv", "a", newline="")

wrt = csv.writer(file)
wrt.writerow(newRow)
file.close()
file = open("example.csv", "r",newline="")
rdr = csv.reader(file)
for line in rdr:
    if line[0] == "1004":
        print("Neil Harris added to the csv")
file.close