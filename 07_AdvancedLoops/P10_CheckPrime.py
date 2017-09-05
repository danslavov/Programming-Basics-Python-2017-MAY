import math

n = int(input())
if n < 2:
    print("Not Prime")
    exit()
for i in range(math.trunc(math.sqrt(n)), 1, -1):
    if n % i == 0:
        print("Not Prime")
        exit()
print("Prime")
