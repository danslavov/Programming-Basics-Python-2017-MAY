n = int(input())

print(("." * (n + 1)) + ("_" * (2 * n + 1)) + ("." * (n + 1)))

for i in range(n):
    print(("." * (n - i)) + "//" + ("_" * ((2 * n - 1) + (2 * i))) + "\\\\" + ("." * (n - i)))

print("//" + ("_" * ((n * 4 - 6) // 2)) + "STOP!" + ("_" * ((n * 4 - 6) // 2)) + "\\\\")

for j in range(n, 0, -1):
    print(("." * (n - j)) + "\\\\" + ("_" * ((2 * n - 1) + (2 * j))) + "//" + ("." * (n - j)))
