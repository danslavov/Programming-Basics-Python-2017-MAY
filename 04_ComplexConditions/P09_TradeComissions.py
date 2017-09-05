def volume0to500(x):
    return {"Sofia": 5.0,
            "Varna": 4.5,
            "Plovdiv": 5.5
            }.get(x, -1.0)


def volume500to1000(x):
    return {"Sofia": 7.0,
            "Varna": 7.5,
            "Plovdiv": 8.0
            }.get(x, -1.0)


def volume1000to10000(x):
    return {"Sofia": 8.0,
            "Varna": 10.0,
            "Plovdiv": 12.0
            }.get(x, -1.0)


def volume10000plus(x):
    return {"Sofia": 12.0,
            "Varna": 13.0,
            "Plovdiv": 14.5
            }.get(x, -1.0)


town = input()
salesVolume = float(input())
commission = -1.0

if 0 <= salesVolume <= 500:
    commission = volume0to500(town)
elif salesVolume <= 1000:
    commission = volume500to1000(town)
elif salesVolume <= 10000:
    commission = volume1000to10000(town)
elif salesVolume > 10000:
    commission = volume10000plus(town)

if commission >= 0:
    print("{:.2f}".format(salesVolume * commission / 100.0))
else:
    print("error")
