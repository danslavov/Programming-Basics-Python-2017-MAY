q = int(input())
y = int(input())
x = int(input())

insideUpperLower = (-3 * q < x < 3 * q) and ((-2 * q < y < -1 * q) or (1 * q < y < 2 * q))
insideMiddle = (-2 * q < x < 2 * q) and (-2 * q < y < 2 * q)
isInside = insideUpperLower or insideMiddle

lowerUpperBorder = (-3 * q <= x <= 3 * q) and ((y == - 2 * q) or (y == 2 * q))
sideOuterBorder = ((x == -3 * q) or (x == 3 * q)) and ((-2 * q <= y <= -1 * q) or (1 * q <= y <= 2 * q))
sideInnerBorder = ((x == -2 * q) or (x == 2 * q)) and (-1 * q <= y <= 1 * q)
otherBorder = (((-3 * q <= x <= -2 * q) or (2 * q <= x <= 3 * q)) and ((y == 1 * q) or (y == -1 * q)))
isOnBorder = lowerUpperBorder or sideOuterBorder or sideInnerBorder or otherBorder

if isInside:
    print("INSIDE")
elif isOnBorder:
    print("BORDER")
else:
    print("OUTSIDE")