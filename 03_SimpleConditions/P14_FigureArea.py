import math

figure = input()

if figure == "square":
    side = float(input())
    result = side * side
elif figure == "rectangle":
    sideA = float(input())
    sideB = float(input())
    result = sideA * sideB
elif figure == "circle":
    r = float(input())
    result = math.pi * r * r
else:
    side = float(input())
    height = float(input())
    result = side * height / 2

print("{:.3f}".format(result))
