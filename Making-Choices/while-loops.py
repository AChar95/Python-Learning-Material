counter = 5

while counter > 0:
    print("The counter value is: ", counter)
    counter -= 1

j = 0

for i in range(5):
    j = j + 2
    print("i = ", i, ", j = ", j)
    if j == 6:
        break

k = 0

for i in range(5):
    k = k + 2
    print("i = ", i, ", k = ", k)
    if k == 6:
        continue
    print("This won't be printed when k = 6")
