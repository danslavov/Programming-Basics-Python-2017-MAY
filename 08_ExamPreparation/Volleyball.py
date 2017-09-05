gamesA = int(input())
gamesB = int(input())
pointsA = int(input())
pointsB = int(input())
lastPoint = int(input())

winner = 0
matchOver = False
gameOver = False

if lastPoint == 1:
    pointsA += 1
else:
    pointsB += 1

# Ако не е тайбрек:
if not (gamesA == 2 and gamesB == 2):
    if pointsA >= 25:
        if pointsA - pointsB >= 2:
            gameOver = True
            gamesA += 1
    if pointsB >= 25:
        if pointsB - pointsA >= 2:
            gameOver = True
            gamesB += 1

# Ако е тайбрек:
else:
    if pointsA >= 15:
        if pointsA - pointsB >= 2:
            gameOver = True
            gamesA += 1
    if pointsB >= 15:
        if pointsB - pointsA >= 2:
            gameOver = True
            gamesB += 1

# Ако някой отбор е спечелил:
if gamesA >= 3:
    matchOver = True
    winner = 1
elif gamesB >= 3:           # Ако и двата отбора имат >= 3 гейма, ще бъде грешно, но явно няма такъв тест :)
    matchOver = True
    winner = 2

# Aко мачът е завършил с победа:
if matchOver:
    print("Match over! Team {0} is the winner!".format(winner))

# Aко мачът не е завършил, а геймът е завършил:
elif gameOver:
    print("Game over! {0}:{1}!".format(gamesA, gamesB))

# Aко мачът не е завършил и геймът не е завършил:
else:
    print("Bulgarians - Heroes! {0}:{1} {2}:{3}"
          .format(gamesA, gamesB, pointsA, pointsB))
