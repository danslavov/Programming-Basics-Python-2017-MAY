n = int(input())
previous = 1
current = 0
next = 0
fib = []

while next < n:
    next = previous + current
    previous = current
    current = next
    fib.append(next)

fib.reverse()
sum = 0

for num in fib:
    if num <= (n - sum):
        sum += num
        print(num)
        if (n - sum) == 0:
            exit()
