# 97/100 in Judge

h = int(input())
x = int(input())
y = int(input())

insideOne = (0 < x < (3 * h)) and (0 < y < h)
insideTwo = (h < x < (2 * h)) and (0 < y < (4 * h))

borderOne = (0 <= (3 * h)) and (y == 0)
borderTwo = (x == 0 or x == (3 * h)) and (0 <= y <= h)
borderThree = ((0 <= x <= h) or ((2 * h) <= x <= (3 * h))) and (y == h)
borderFour = ((x == h) or (x == (2 * h))) and (h <= y <= (4 * h))
borderFive = (h <= x <= (2 * h)) and (y == (4 * h))

isOnBorder = borderOne or borderTwo or borderThree or borderFour or borderFive
isInside = insideOne or insideTwo

if isInside:
    print("inside")
elif isOnBorder:
    print("border")
else:
    print("outside")
