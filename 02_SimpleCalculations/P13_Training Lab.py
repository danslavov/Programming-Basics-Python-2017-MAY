width = float(input())
height = float(input())

availableHeight = int((height - 1) // 0.7)
availableWidth = int(width // 1.2)

deskNumber = availableHeight * availableWidth - 3

print(deskNumber)

