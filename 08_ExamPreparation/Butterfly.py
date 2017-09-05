n = int(input())
odd = "*" * (n - 2)
even = "-" * (n - 2)
for i in range(1, n - 1):
    if i % 2 == 1:
        print(odd + "\\ /" + odd)
    else:
        print(even + "\\ /" + even)
print(" " * (n - 1) + "@")
for i in range(1, n - 1):
    if i % 2 == 1:
        print(odd + "/ \\" + odd)
    else:
        print(even + "/ \\" + even)