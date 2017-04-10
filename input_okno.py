cislo = int(input("Zadej celé číslo: "))
for j in range(cislo):
    if j == 0 or j == cislo - 1:
        for i in range(cislo):
            print("X", end = " ")
    else:
        for neco in range(cislo):
            if neco == 0 or neco == cislo - 1:
                print("X", end=" ")
            else:
                print(" ", end=" ")
    print(" ")
