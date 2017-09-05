n = int(input())

print(n, end="")

while n > 0:
    print(n % 10, end="")
    n //= 10
print()