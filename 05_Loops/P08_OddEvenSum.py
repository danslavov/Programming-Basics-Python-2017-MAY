n = int(input())
sumOdd = 0
sumEven = 0

for i in range(1, n + 1):
    num = int(input())

    if i % 2 != 0:
        sumOdd += num
    else:
        sumEven += num

diff = abs(sumOdd - sumEven)

if diff == 0:
    print("Yes\nSum =", sumOdd)
else:
    print("No\nDiff =", diff)
