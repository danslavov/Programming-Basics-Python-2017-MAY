def workday(x):
    return {"banana": 2.5,
            "apple": 1.2,
            "orange": .85,
            "grapefruit": 1.45,
            "kiwi": 2.7,
            "pineapple": 5.5,
            "grapes": 3.85
            }.get(x, -1.0)


def weekend(x):
    return {"banana": 2.7,
            "apple": 1.25,
            "orange": .9,
            "grapefruit": 1.6,
            "kiwi": 3.0,
            "pineapple": 5.6,
            "grapes": 4.2
            }.get(x, -1.0)


fruit = input().lower()
dayOfWeek = input().lower()
quantity = float(input())
price = -1.0

isWeekend = (dayOfWeek == "saturday" or dayOfWeek == "sunday")
isWorkDay = (dayOfWeek == "monday" or dayOfWeek == "tuesday" or
             dayOfWeek == "wednesday" or dayOfWeek == "thursday" or
             dayOfWeek == "friday")

if isWeekend:
        price = quantity * weekend(fruit)
elif isWorkDay:
        price = quantity * workday(fruit)

if price >= 0:
        print("{:.2f}".format(price))
else:
        print("Error")
