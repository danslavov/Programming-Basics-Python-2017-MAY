volume = int(input())
firstPipeFlow = int(input())
secondPipeFlow = int(input())
time = float(input())

currentVolume = (firstPipeFlow + secondPipeFlow) * time
diff = volume - currentVolume

if diff >= 0:
    firstPipeShare = int(firstPipeFlow * time / currentVolume * 100)
    secondPipeShare = int(secondPipeFlow * time / currentVolume * 100)
    print("The pool is {}% full. Pipe 1: {}%. Pipe 2: {}%."
          .format(int(currentVolume / volume * 100), firstPipeShare, secondPipeShare))
else:
    print("For {} hours the pool overflows with {} liters."
          .format(time, abs(diff)))
