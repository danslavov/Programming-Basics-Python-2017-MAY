firstTime = int(input())
secondTime = int(input())
thirdTime = int(input())

totalTime = firstTime + secondTime + thirdTime
minutes = int(totalTime / 60)
seconds = totalTime % 60

print("{}:{:02d}".format(minutes, seconds))