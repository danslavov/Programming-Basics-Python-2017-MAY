n = int(input())
firstRow = "/" + "^" * (n // 2) + "\\" + "_" * (2 * (n - (n // 2) - 2)) + "/" + "^" * (n // 2) + "\\"
middleSpaces = "|" + " " * (2 * n - 2) + "|"
middleSpacesUnderscore = "|" + " " * (n // 2 + 1) + "_" * (2 * (n - (n // 2) - 2)) + " " * (n // 2 + 1) + "|"
lastRow = "\\" + "_" * (n // 2) + "/" + " " * (2 * (n - (n // 2) - 2)) + "\\" + "_" * (n // 2) + "/"

print(firstRow)
for i in range(n // 2):
    print(middleSpaces)
if n > 4:
    print(middleSpacesUnderscore)
print(lastRow)
