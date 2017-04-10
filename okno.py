for j in range(6):
    if j == 0 or j == 5:
        for i in range(6):
            print("X", end = " ")
    else:
        for neco in range(6):
            if neco == 0 or neco == 5:
                print("X", end=" ")
            else:
                print(" ", end=" ")
    print(" ")
