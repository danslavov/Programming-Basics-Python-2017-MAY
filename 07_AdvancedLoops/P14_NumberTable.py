n = int(input())
for row in range(1, n + 1):
    for colAscend in range(row, n + 1):
        print(colAscend, end=" ")
    for colDescend in range(n - 1, n - row, -1):
        print(colDescend, end=" ")
    print()
