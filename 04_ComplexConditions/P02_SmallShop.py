product = input().lower()
town = input().lower()
quantity = float(input())
price = .0

if town == "sofia":
    if product == "coffee":
        price = .5
    elif product == "water":
        price = .8
    elif product == "beer":
        price = 1.2
    elif product == "sweets":
        price = 1.45
    else:
        price = 1.6

elif town == "plovdiv":
    if product == "coffee":
        price = .4
    elif product == "water":
        price = .7
    elif product == "beer":
        price = 1.15
    elif product == "sweets":
        price = 1.3
    else:
        price = 1.5

else:
    if product == "coffee":
        price = .45
    elif product == "water":
        price = .7
    elif product == "beer":
        price = 1.1
    elif product == "sweets":
        price = 1.35
    else:
        price = 1.55

print("{:.2f}".format(quantity * price))
