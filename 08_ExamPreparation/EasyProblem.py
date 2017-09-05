import decimal

n = int(input())
numberSum = n * (n + 1) / 2
remainder = decimal.Decimal(numberSum) % 1000000007
result = decimal.Decimal(remainder) * decimal.Decimal(remainder)
print("{0:.0f}".format(result))
