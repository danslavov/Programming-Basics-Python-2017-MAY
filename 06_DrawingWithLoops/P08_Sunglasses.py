n = int(input())
halfBorder = "*" * 2 * n
halfMiddle = "*" + "/" * (2 * n - 2) + "*"
border = halfBorder + " " * n + halfBorder
middle = halfMiddle + " " * n + halfMiddle
center = halfMiddle + "|" * n + halfMiddle

print(border)
for i in range(n - 2):
    if i == (n - 1) // 2 - 1:
        print(center)
    else:
        print(middle)
print(border)
