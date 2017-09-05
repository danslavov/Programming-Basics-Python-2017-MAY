def price(x):
    return {"Premiere": 12.0,
            "Normal": 7.5,
            "Discount": 5.0
            }.get(x)

ticketPrice = price(input())
hallRows = int(input())
hallColumns = int(input())
hallArea = hallRows * hallColumns
print("{:.2f} leva".format(hallArea * ticketPrice))
