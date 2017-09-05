import math

k = int(input())
q = int(input())
c = int(input())
b = int(input())
o = int(input())

kgPerHour = q - c - b
diff = k - o * kgPerHour
if diff < 0:
    print("YES")
else:
    print("NO - {}".format(math.ceil(abs(diff / kgPerHour))))
