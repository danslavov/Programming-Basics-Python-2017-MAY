platformSide = int(input())
tileWidth = float(input())
tileLength = float(input())
benchWidth = int(input())
benchLength = int(input())

platformArea = platformSide * platformSide
tileArea = tileLength * tileWidth
benchArea = benchLength * benchWidth
area = platformArea - benchArea
tileNumber = area / tileArea
time = tileNumber * 0.2

print("{0:.2f}".format(tileNumber))
print("{0:.2f}".format(time))
