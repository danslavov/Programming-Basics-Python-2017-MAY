x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

sideA = abs(x1 - x2)
sideB = abs(y1 - y2)

perimeter = 2 * (sideA + sideB)
area = sideA * sideB

print(area)
print(perimeter)
