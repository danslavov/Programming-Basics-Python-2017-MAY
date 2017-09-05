num = int(input())

wordsSmall = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
              6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
              11: "eleven", 12: "twelve", 13: "thirteen", 15: "fifteen", 18: "eighteen"}
wordsBig = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
            6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

if 0 <= num < 100:
    if num < 14 or num == 15 or num == 18:
        print(wordsSmall.get(num))
    elif num < 20:
        print("{}teen".format(wordsSmall.get(num % 10)))
    elif num % 10 == 0:
        print(wordsBig.get(num // 10))
    else:
        print("{} {}".format(wordsBig.get(num // 10), wordsSmall.get(num % 10)))
elif num == 100:
    print("one hundred")
else:
    print("invalid number")
