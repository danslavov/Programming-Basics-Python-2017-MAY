n = int(input())
firstLastRow = "+ " + ("- " * (n-2)) + "+"
middleRow =  "| " + ("- " * (n-2)) + "|"

print(firstLastRow)
for row in range(n-2):
    print(middleRow)
print(firstLastRow)
