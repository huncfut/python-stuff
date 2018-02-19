num = str(input("Daj ciąg: "))
i = 0

def printString(string):
    if len(string) > 0:
        printString(string[0:len(string)-1])
    else:
        print(string[len(string-1)])

printString(num)
