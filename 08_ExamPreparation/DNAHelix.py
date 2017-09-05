# not tested in Judge

n = int(input())
base1 = ""
base2 = ""
sequence = "ATCGTTAGGG"
rowNumber = 0
shiftCount = 0

while True:
    print("**{}{}**".format(sequence[shiftCount % len(sequence)],
                            sequence[(shiftCount + 1) % len(sequence)]))
    rowNumber += 1
    shiftCount += 2
    if rowNumber == n:
        exit()
    print("*{}--{}*".format(sequence[shiftCount % len(sequence)],
                            sequence[(shiftCount + 1) % len(sequence)]))
    shiftCount += 2
    rowNumber += 1
    if rowNumber == n:
        exit()
    print("{}----{}".format(sequence[shiftCount % len(sequence)],
                            sequence[(shiftCount + 1) % len(sequence)]))
    shiftCount += 2
    rowNumber += 1
    if rowNumber == n:
        exit()
    print("*{}--{}*".format(sequence[shiftCount % len(sequence)],
                            sequence[(shiftCount + 1) % len(sequence)]))
    shiftCount += 2
    rowNumber += 1
    if rowNumber == n:
        exit()
