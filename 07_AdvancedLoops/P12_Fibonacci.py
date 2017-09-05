n = int(input())
previous = 0
current = 1
next = 1
for i in range(n):
    next = previous + current
    previous = current
    current = next
if n < 2:
    print(1)
else:
    print(next)
