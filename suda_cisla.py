x = int(input("Zadej číslo: "))


if x % 2 == 0:
    print("Číslo je sudé.")
else:
    print("Číslo je liché.")

from math import factorial
print("Faktoriál čísla je: ", factorial(x))

if float((2**x - 2)/x) == int((2**x - 2)/x):
    print("Číslo je prvočíslo.")
else:
    print("Číslo není prvočíslo.")
