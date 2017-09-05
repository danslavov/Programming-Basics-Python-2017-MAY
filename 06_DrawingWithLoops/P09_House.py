n = int(input())

# make roof
firstRowStars = 0
if n % 2 == 0:
    firstRowStars = 2
else:
    firstRowStars = 1

for i in range((n + 1) // 2):
    print("-" * ((n + 1) // 2 - 1 - i) + "*" * (firstRowStars + 2 * i) + "-" * ((n + 1) // 2 - 1 - i))

# make body
for i in range(n // 2):
    print("|" + "*" * (n - 2) + "|")
