inputNumber = float(input())
fromMetric = input()
toMetric = input()

fromMetricList = {"mm": 1/1000, "cm": 1/100, "mi": 1/0.000621371192,
                  "in": 1/39.3700787, "km": 1/0.001,
                  "ft": 1/3.2808399, "yd": 1/1.0936133}

toMetricList = {"mm": 1000, "cm": 100, "mi": 0.000621371192,
                "in": 39.3700787, "km": 0.001,
                "ft": 3.2808399, "yd": 1.0936133}

outputNumber = inputNumber * fromMetricList.get(fromMetric, 1.0) * toMetricList.get(toMetric, 1.0)

print(outputNumber)
