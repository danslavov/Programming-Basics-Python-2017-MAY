x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

isOnBorderX = (x == x1 or x == x2) and (y1 <= y <= y2)
isOnBorderY = (y == y1 or y == y2) and (x1 <= x <= x2)
isOnBorder = isOnBorderX or isOnBorderY

if isOnBorder:
    print("Border")
else:
    print("Inside / Outside")
