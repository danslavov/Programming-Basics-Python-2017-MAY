import sys

distance = int(input())
dayOrNight = input()
bus = sys.maxsize
train = sys.maxsize

if dayOrNight == "day":
    taxi = 70 + distance * 79
else:
    taxi = 70 + distance * 90

if distance >= 20:
    bus = distance * 9

if distance >= 100:
    train = distance * 6

print(min(taxi, bus, train) * 0.01)
