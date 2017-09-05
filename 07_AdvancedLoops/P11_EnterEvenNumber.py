while True:
    print("Enter even number: ", end="")
    try:
        n = int(input())
        if n % 2 == 1:
            print("The number is not even.")
        else:
            print("Even number entered: {}".format(n))
            break
    except:
        print("Invalid number!")
