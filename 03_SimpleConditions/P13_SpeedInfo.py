speed = float(input())

speedRange = {(speed <= 10.0): "slow",
              (10.0 < speed <= 50.0): "average",
              (50.0 < speed <= 150.0): "fast",
              (150.0 < speed <= 1000.0): "ultra fast",
              (speed > 1000.0): "extremely fast"}

print(speedRange.get(True))
