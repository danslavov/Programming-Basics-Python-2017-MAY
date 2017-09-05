n = int(input())
isFirst = True
for i in range(1111, 10000):
    firstDigit = i // 1000
    secondDigit = (i // 100) % 10
    thirdDigit = (i // 10) % 10
    fourthDigit = i % 10
    if firstDigit == 0 or secondDigit == 0 or thirdDigit == 0 or fourthDigit == 0:
        continue
    elif n % firstDigit == 0 and n % secondDigit == 0 and \
        n % thirdDigit == 0 and n % fourthDigit == 0:
        if isFirst:
            print(i, end="")
            isFirst = False
        else:
            print(" " + str(i), end="")
