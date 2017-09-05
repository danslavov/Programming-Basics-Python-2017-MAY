number = int(input())
bonus = 0.0

if number <= 100:
    bonus = 5
elif number <= 1000:
    bonus = number * 2 / 100
else:
    bonus = number * 1 / 100

if number % 2 == 0:
    bonus += 1

if number % 10 == 5:    # elif number % 5 == 0:
    bonus += 2

print("{}\n{}".format(bonus, (number + bonus)))
