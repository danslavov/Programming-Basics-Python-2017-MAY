import sys

n = int(input())
oddSum = 0.0
oddMin = sys.maxsize
oddMax = - sys.maxsize - 1
evenSum = 0.0
evenMin = sys.maxsize
evenMax = - sys.maxsize - 1

for i in range(1, n + 1):
    curNum = float(input())

    if i % 2 != 0:
        oddSum += curNum
        if curNum > oddMax:
            oddMax = curNum
        if curNum < oddMin:
            oddMin = curNum
    else:
        evenSum += curNum
        if curNum > evenMax:
            evenMax = curNum
        if curNum < evenMin:
            evenMin = curNum

if oddMin == sys.maxsize:
    oddMin = "No"
if oddMax == - sys.maxsize - 1:
    oddMax = "No"
if evenMin == sys.maxsize:
    evenMin = "No"
if evenMax == - sys.maxsize - 1:
    evenMax = "No"

print("OddSum={}, OddMin={}, OddMax={}, "
      "EvenSum={}, EvenMin={}, EvenMax={}"
      .format(oddSum, oddMin, oddMax,
              evenSum, evenMin, evenMax))