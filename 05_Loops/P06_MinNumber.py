import sys

n = int(input())
minNumber = sys.maxsize

for i in range(0, n):
    currentNumber = int(input())

    if currentNumber < minNumber:
        minNumber = currentNumber

print(minNumber)
