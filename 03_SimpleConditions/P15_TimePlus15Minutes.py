hours = int(input())
minutes = int(input())

minutes += 15

if minutes > 59:
    hours += 1
    minutes -= 60

if hours > 23:
    hours = 0

print("{}:{:02d}".format(hours, minutes))
