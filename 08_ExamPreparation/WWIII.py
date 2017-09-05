import math

bunkerX = float(input())
bunkerY = float(input())
volleyCount = int(input())
bunkerHealth = int(input())
NGVolleyMin = float(input())
NGVolleyMax = float(input())
CCVolleyMin = float(input())
CCVolleyMax = float(input())
NGHits = 0
CCHits = 0

for i in range(2 * volleyCount):
    volleyX = float(input())
    volleyY = float(input())

    sqDiffX = math.pow((bunkerX - volleyX), 2)
    sqDiffY = math.pow((bunkerY - volleyY), 2)
    bunkerIsOutsideInner = (sqDiffX + sqDiffY) >= math.pow((NGVolleyMin if (i % 2 == 0) else CCVolleyMin), 2)
    bunkerIsInsideOuter = (sqDiffX + sqDiffY) <= math.pow(NGVolleyMax if (i % 2 == 0) else CCVolleyMax, 2)
    hit = bunkerIsOutsideInner and bunkerIsInsideOuter

    if hit:
        bunkerHealth -= 1
        if i % 2 == 0:
            NGHits += 1
        else:
            CCHits += 1

    if bunkerHealth <= 0:
        print("NO")
        print("NG" if (i % 2 == 0) else "CC")
        exit()

print("YES\n{}\n{}".format(CCHits, NGHits))
