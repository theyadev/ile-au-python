import os

os.system('cls')

Table1X = 5
Table1Y = 1
Table2X = Table1X + 40
Table2Y = Table1Y

FormatPrefix = "\033["
PositionSuffix = "H"

def printAt(posX, posY,text):
    print(f"{FormatPrefix}{posY};{posX}{PositionSuffix}{text}")

for i in range(10):
    if i % 2 == 0:
        printAt(Table1X, Table1Y + 1 + (i * 2), "Pair")
    else:
        printAt(Table2X, Table2Y + 1 + (i* 2), "Impair")
print("\nFin\n")