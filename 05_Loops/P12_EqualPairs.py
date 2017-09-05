n = int(input())
previousValue = 0
maxDiff = 0
equalValues = True

for i in range(0, 2 * n, 2):
    firstNum = int(input())
    secondNum = int(input())
    value = firstNum + secondNum

    if i == 0:
        previousValue = value

    if value != previousValue:
        equalValues = False
        diff = abs(previousValue - value)

        if diff > maxDiff:
            maxDiff = diff

    previousValue = value

if equalValues:
    print("Yes, value=" + str(previousValue))
else:
    print("No, maxdiff=" + str(maxDiff))
