t1 = int(input()) * 60 + int(input())
t2 = int(input()) * 60 + int(input())
t3 = int(input()) * 60 + int(input())
h1 = int(input())
h2 = int(input())
h3 = int(input())

hMax = 0
hMid = 0
hMin = 0
tMax = 0
tMid = 0
tMin = 0

# order happiness amounts with their times
if h1 > h2:
    if h1 > h3:
        hMax = h1
        tMax = t1
        if h2 > h3:
            hMid = h2
            tMid = t2
            hMin = h3
            tMin = t3
        else:
            hMid = h3
            tMid = t3
            hMin = h2
            tMin = t2
    else:
        hMax = h3
        tMax = t3
        if h1 > h2:
            hMid = h1
            tMid = t1
            hMin = h2
            tMin = t2
        else:
            hMid = h2
            tMid = t2
            hMin = h1
            tMin = t1
elif h2 > h3:
    hMax = h2
    tMax = t2
    if h3 > h1:
        hMid = h3
        tMid = t3
        hMin = h1
        tMin = t1
    else:
        hMid = h1
        tMid = t1
        hMin = h3
        tMin = t3
else:
    hMax = h3
    tMax = t3
    if h1 > h2:
        hMid = h1
        tMid = t1
        hMin = h2
        tMin = t2
    else:
        hMid = h2
        tMid = t2
        hMin = h1
        tMin = t1

hTotal = hMax

# try to add second-best happiness
if (tMax > tMid + 89) or (tMax + 89 < tMid):
    hTotal += hMid
elif (tMax > tMin + 89) or (tMax + 89 < tMin):
    hTotal += hMin
# if the sum of mid & min is bigger than max and can be combined,
# use them instead
elif (hMid + hMin > hMax) and ((tMid > tMin + 89) or (tMid + 89 < tMin)):
    hTotal = hMid + hMin

print(hTotal)

