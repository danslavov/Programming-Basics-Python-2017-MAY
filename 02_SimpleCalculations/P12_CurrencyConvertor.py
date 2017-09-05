amount = float(input())
fromCurrency = input()
toCurrency = input()

if fromCurrency == "USD":
    amount *= 1.79549
elif fromCurrency == "EUR":
    amount *= 1.95583
elif fromCurrency == "GBP":
    amount *= 2.53405

if toCurrency == "USD":
    amount /= 1.79549
elif toCurrency == "EUR":
    amount /= 1.95583
elif toCurrency == "GBP":
    amount /= 2.53405

print("{0:.2f} {1}".format(amount, toCurrency))
