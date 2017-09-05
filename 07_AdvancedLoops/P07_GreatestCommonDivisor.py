a = int(input())
b = int(input())
if b > a:
    temp = a
    a = b
    b = temp
while b > 0:
    temp = b
    b = a % b
    a = temp
print(a)
