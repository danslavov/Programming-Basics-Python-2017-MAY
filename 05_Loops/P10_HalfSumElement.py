import sys

n = int(input())
sum = 0
maxNum = - sys.maxsize - 1

for i in range(0, n):
    currentNum = int(input())
    sum += currentNum
    if currentNum > maxNum:
        maxNum = currentNum

diff = abs(sum - maxNum)

if diff == maxNum:
    print("Yes\nSum =", maxNum)
else:
    print("No\nDiff =", abs(maxNum - diff))
