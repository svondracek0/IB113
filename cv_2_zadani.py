from math import pi, pow

# Vytvorte program pocitajici objem kvadru a objem koule
def volume (side_a, side_b, side_c):
    objem_kvadru = side_a * side_b * side_c
    objem_koule = (4/3) * (pi * side_a ** 3)
    print("Objem kvadru je", objem_kvadru, "cm^3.", "Objem koule je", objem_koule, "cm^3.")


# TODO


# Vypiste prvnich 10 mocnin cisla 2.
# Oddelte je carkou a mezerou (za posledni cislici neni carka)

def powers(count):
    for i in range(count)[0:count-1]:
        print(2 ** i, end = ", ")

    pass  # TODO



powers(10)
print()


# Vypiste prvnich 15 prvku Fibonnaciho posloupnosti.


def print_fibonnaci(count: int) -> None:
    a = 0
    b = 1
    c = a + b
    for i in range(count):
        if i == 0:
            print(a)
        elif i == 1:
            print(b)
        else:
            b = c
            c = a + b
            a = b
            print(c)
print_fibonnaci(10)

print_fibonnaci(15)



# Napiste funkci, ktera vypise prvnich 10 prvku posloupnosti, jejichz prvni
# prvky vypadaji nasledovne:
#   a) 1 -1 2 -2 3 -3 4 -4 5 -5 ...

def print_alternating(length: int) -> None:
    for i in range(1,length + 1):
        print(i, -i, end = "")
    pass  # TODO


print_alternating(10)



#   b) 1 1 2 1 2 3 1 2 3 4 …


def print_subsequence(length: int) -> None:
    for i in range(length):
        for j in range(1, i):
            print(j, end = " ")
    pass  # TODO

print_subsequence(10)


print_subsequence(10)
print()
print()


# Naleznete a vypiste vsechny delitele daneho cisla.
# Cislo zadejte pomoci promenne


def divisors(num: int):
    if num <= 0:
        print("CHYBA PYCO")
    else:
        for i in range(1, num + 1):
            if num % i == 0:
                print(i, end = ",")



# Rozsireni v pripade dostatku casu
# a) Cisla vypiste na jeden radek oddelena carkou
# b) Pro 0 a zaporna cisla vypiste chybovou hlasku


def divisors_extended(num: int) -> None:
    pass  # TODO


TESTED_NUMBER = 1586  # je to konstanta, proto UPPER_CASE
# tested_number = int(input("Zadej cislo: "))
print("Zakladni verze:")
divisors(TESTED_NUMBER)
print()
print("Rozsirena verze:")
divisors_extended(TESTED_NUMBER)
