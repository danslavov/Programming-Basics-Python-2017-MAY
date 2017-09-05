x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

xIsInside = x1 <= x <= x2
yIsInside = y1 <= y <= y2

if xIsInside and yIsInside:
    print("Inside")
else:
    print("Outside")
