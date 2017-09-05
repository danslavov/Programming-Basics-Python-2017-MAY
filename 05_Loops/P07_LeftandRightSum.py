n = int(input())
leftSum = 0
rightSum = 0

for i in range(0, n):
    leftSum += int(input())
for i in range(0, n):
    rightSum += int(input())

diff = abs(leftSum - rightSum)

if diff == 0:
    print("Yes, sum =", leftSum)
else:
    print("No, diff =", diff)