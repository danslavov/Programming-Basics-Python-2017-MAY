n = int(input())
l = int(input())
result = ""

for firstDigit in range(1, n + 1):
    for secondDigit in range(1, n + 1):
        for firstLetter in range(0, l):
            for secondLetter in range(0, l):
                for thirdDigit in range(
                        max(firstDigit, secondDigit) + 1, n + 1):
                    result += "{0}{1}{2}{3}{4} ".format(
                        firstDigit, secondDigit, chr(firstLetter + 97),
                        chr(secondLetter + 97), thirdDigit)

print(result.strip())
