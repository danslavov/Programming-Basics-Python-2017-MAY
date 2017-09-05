import math

leapOrNormal = input()
holidays = int(input())
hometownWeekends = int(input())

sofiaWeekends = 48 - hometownWeekends
gameCount = (sofiaWeekends * 3 / 4) + hometownWeekends + (holidays * 2 / 3)

if leapOrNormal == "leap":
    gameCount += gameCount * 15 / 100

print("{}".format(math.floor(gameCount)))
