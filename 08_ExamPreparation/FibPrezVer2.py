n = int(input())
previous = 1
current = 0
next = 0
while next < n:
    next = previous + current
    previous = current
    current = next
sum = 0
while n - sum > 0:
    if next <= (n - sum):
        print(next)
        sum += next
    next = current
    current = previous
    previous = next - current
