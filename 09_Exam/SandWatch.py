n = int(input())
elapsed = int(input())

for i in range(n - 1):
    side = (" " if i % 2 == 0 else "?") * i
    symbol = "-" if i < elapsed else "*"
    print(side + (symbol + " ") * (n - 1 - i) + symbol + side)

center = (" " if n % 2 != 0 else "?") * (n - 1)
print(center + "o" + center)

for i in range(n - 2, -1, -1):
    side = (" " if i % 2 == 0 else "?") * i
    symbol = "-" if i >= elapsed else "*"
    print(side + (symbol + " ") * (n - 1 - i) + symbol + side)