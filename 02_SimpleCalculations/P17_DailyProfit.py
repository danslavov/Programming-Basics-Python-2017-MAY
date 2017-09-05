daysPerMonth = int(input())
dollarsPerDay = float(input())
exchangeRate = float(input())

salaryPerMonth = daysPerMonth * dollarsPerDay
salaryPerYear = (salaryPerMonth * (12 + 2.5)) * 0.75
levaPerDay = salaryPerYear / 365 * exchangeRate

print("{0:.2f}".format(levaPerDay))

