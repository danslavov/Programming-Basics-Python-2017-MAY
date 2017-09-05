print("Еnter a number in the range [1...100]: ", end="")
n = int(input())
while n < 1 or n > 100:
    print("Invalid number!\n"
          "Еnter a number in the range [1...100]: ", end="")
    n = int(input())
print("The number is: {}".format(n))
