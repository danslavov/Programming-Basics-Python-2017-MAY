firstFriend = input().lower()
secondFriend = input().lower()

if (firstFriend == "out") ^ (secondFriend == "out"):
    print("Go out!")
else:
    print("Stay at home!")
