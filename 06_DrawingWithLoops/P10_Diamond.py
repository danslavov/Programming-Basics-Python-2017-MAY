n = int(input())

firstStarCount = 0
if n % 2 == 0:
    firstStarCount = 2
else:
    firstStarCount = 1
topBottom = "-" * ((n - 1) // 2) + "*" * firstStarCount + "-" * ((n - 1) // 2)

print(topBottom)
for i in range((n + 1) // 2 - 1):
    print("-" * ((n - 1) // 2 - i - 1) + "*" + "-" * (firstStarCount + 2 * i) + "*" + "-" * ((n - 1) // 2 - i - 1))
for i in range((n - 1) // 2 - 1):
    print("-" * (1 + i) + "*" + "-" * (n - 2 * (i + 2)) + "*" + "-" * (1 + i))
if n > 2:
    print(topBottom)
