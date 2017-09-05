n = int(input())
previous = 1
current = 1
next = 0

for i in range(1, n - 1):
    if i % 2 != 0:
        next = current + previous

    else:
        next = current * (i // 2 + 1)

    previous = current
    current = next

if n < 3:
    print(1)
else:
    print(int(next))