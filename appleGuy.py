yard = []
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

for i in range(rows):
    line = []
    for j in range(cols):
        if j == 0 and i == 0:
            line += [int(input("Enter number of Apples for row %d, column %d: " % (i+1, j+1)))]
        elif i == 0:
            line += [int(input("Enter number of Apples for row %d, column %d: " % (i+1, j+1))) + line[j-1]]
        elif j == 0:
            line += [int(input("Enter number of Apples for row %d, column %d: " % (i+1, j+1))) + yard[i-1][j]]
        elif line[j-1] > yard[i-1][j]:
            line += [int(input("Enter number of Apples for row %d, column %d: " % (i+1, j+1))) + line[j-1]]
        else:
            line += [int(input("Enter number of Apples for row %d, column %d: " % (i+1, j+1))) + yard[i-1][j]]
    yard.append(line)

print(yard[rows-1][cols-1])
