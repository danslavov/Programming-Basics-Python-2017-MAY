import sys

n = int(input())
maxNumber = -sys.maxsize - 1

for i in range(0, n):
    currentNumber = int(input())

    if currentNumber > maxNumber:
        maxNumber = currentNumber

print(maxNumber)
