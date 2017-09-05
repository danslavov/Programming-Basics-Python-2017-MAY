bitcoin = int(input())
juan = float(input())
commission = float(input())

bitcoinToLev = bitcoin * 1168
juanToDollar = juan * 0.15
dollarToLev = juanToDollar * 1.76
euro = (bitcoinToLev + dollarToLev) / 1.95
euro -= euro * commission / 100

print("{0:.2f}".format(euro))
