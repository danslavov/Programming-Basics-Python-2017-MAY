def vowels(x):
    return {"a": 1,
            "e": 2,
            "i": 3,
            "o": 4,
            "u": 5
            }.get(x, 0)

word = input().lower()
vowelSum = 0

for i in word:
    vowelSum += vowels(i)

print(vowelSum)