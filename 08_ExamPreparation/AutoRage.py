width = int(input())
height = int(input())
passengers = int(input())

border = ("|" + ("-" * (width * 2 + 1)) + "|")
print(border)

for row in range(height):
    print("|", end="")
    for col in range(width):
        print(".X" if passengers > 0 else ".O", end="")
        passengers -= 1
    print(".|")
print(border)
print("v" + (" " * (width * 2 + 1)) + "v")
