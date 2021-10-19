from typing import List, Tuple, Optional

# Napiste funkce nad seznamem cisel, ktere zjisti:
# Soucet vsech cisel v seznamu


def my_sum(numbers: List[int]) -> int:
    sum_rt = 0
    for nm in numbers:
        sum_rt += nm
    return sum_rt


print(my_sum([6, 5, 11, 8]))    # 30

# Nejvyssi cislo v seznamu


def my_max(numbers: List[int]) -> Optional[int]:
    if len(numbers) == 0:
        return numbers

    max_num = numbers[0]
    for nm in numbers:
        if nm > max_num:
            max_num = nm
    return max_num



print(my_max([6, 5, 11, 8]))    # 11
print(my_max([-10, -3, -5]))    # -3

# Zda se urcita hodnota vyskytuje v seznamu


def my_in(num: int, numbers: List[int]) -> bool:
    for element in numbers:
        if num == element:
            return True
    else:
        return False


print(my_in(5, [6, 5, 11, 8]))  # True
print(my_in(4, [6, 5, 11, 8]))  # False

# Vypiste, zda je v seznamu vice sudych nebo lichych cisel


def odd_or_even(numbers: List[int]) -> None:
    odd_count = 0
    for elem in numbers:
        if elem % 2 != 0:
            odd_count += 1
    if odd_count / (len(numbers) / 2) == 1:
        print("Tie")
    elif odd_count / (len(numbers) / 2) > 1:
        print("Odd")
    else:
        print("Even")
    

odd_or_even([6, 5, 10, 8])  # Even
odd_or_even([6, 5, 11, 7])  # Odd
odd_or_even([6, 5, 10, 7])  # Tie
print()


# Napiste funkci, ktera vypocita soucin cisel v seznamu, ale ignoruje pritom
# pripadne nuly.




def nonzero_product(numbers: List[int]) -> int:
    product = 1
    for i in range(1, len(numbers)):
        if numbers[i] != 0:
            product *= numbers[i]
    return product








# Napiste funkci double_all, ktera dostane na vstupu seznam cisel a kazdy jeho
# prvek vynasobi dvema.


def double_all(numbers: List[int]) -> None:
    for i in range(len(numbers)):
        numbers[i] = 2 * numbers[i]
    return numbers


# Napiste funkci create_doubled, ktera dostane na vstupu seznam cisel a vrati
# novy seznam ziskany ze vstupniho tak, ze kazdy prvek vynasobi dvema. Na
# rozdil od predchozi funkce vsak nemeni predany seznam.


def create_doubled(numbers: List[int]) -> List[int]:
    num_rtrn = []
    for elem in numbers:
        num_rtrn.append(2 * elem)
    return num_rtrn


# Napiste funkci, jejimz vstupem je seznam seznamu a vystupem je seznam, ktery
# obsahuje prvky vsech jednotlivych seznamu.

# [[1, 2, 3], [4], [5]] -> [1, 2, 3, 4, 5]

def flatten(lists: List[List[int]]) -> List[int]:
    list_flt = []
    for lst in lists:
        list_flt += lst
    return list_flt


# Napiste funkci, ktera zasifruje text podle predem daneho klice. Pro posun
# pismen zdrojoveho textu se postupne pouzivaji pismena z klice: 'a' posouva
#  o 0, 'b' o 1, … 'z' o 25. Pokud je klic kratsi nez zdrojovy text,
# jsou pouzita pismena z klice opet od zacatku. Muzete se inspirovat popisem
# Vigenerovy sifry.
# Pozn. mala pismena zmente velka; vysledny text obsahuje pouze velka pismena


# text = "ahojdeti"
# key  = "keykeykeykeykey"
# --------------
#        kl..

from math import ceil
def vigenere(text: str, key: str) -> str:
    text = text.upper()
    key = key.upper()
    text_returnable = ""
    key_iterated = ceil(len(text) / len(key)) * key
    for i in range(len(text)):
        text_returnable += chr(ord(text[i]) + ord(key_iterated[i]) - ord("A"))
    return text_returnable




# abcdefgh, 3
# cbafedhg


# Vytvorte funkci, ktera bude na vstupu brat text a cislo. Funkce vrati text,
# kde jednotlive n-tice budou vzdy pozpatku.

def tuple_reverse(text: str, n_tuple: int) -> str:
    ind_first = 0
    ind_last = n_tuple
    rev_txt = ""
    for i in range(len(text) // n_tuple + 1):
    rev_txt += text[ind_last:ind_first:-1]
    return rev_txt


########################################################################
#               Nasleduje kod testu                                    #
########################################################################

ib113_nonzero_product_in: List[List[int]] = [
    [0, 2, 3, 0, 0, 3], [0, 0, 0, 0], [0, -1, 0], []]
ib113_nonzero_product_out = [18, 1, -1, 1]


def ib113_test_nonzero_product() -> None:
    print("Testovani funkce nonzero_product: ", end="")
    failure = False

    for i in range(len(ib113_nonzero_product_in)):
        res = nonzero_product(ib113_nonzero_product_in[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_nonzero_product_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup {} nebyl vracen spravny vysledek"
                  .format(ib113_nonzero_product_in[i]))
            print("Byl vracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}"
                  .format(ib113_nonzero_product_out[i]))
            break

    if not failure:
        print("OK")


ib113_double_all_in: List[List[int]] = [[1, 4, 2, 5], [0], []]
ib113_double_all_in_backup = [[1, 4, 2, 5], [0], []]
ib113_double_all_out = [[2, 8, 4, 10], [0], []]


def ib113_test_double_all() -> None:
    print("Testovani funkce double_all: ", end="")
    failure = False

    for i in range(len(ib113_double_all_in)):
        double_all(ib113_double_all_in[i])
        if ib113_double_all_in[i] != ib113_double_all_out[i]:
            failure = True
            print("NOK")
            print("Seznam nebyl {} zmenen koretne."
                  .format(ib113_double_all_in_backup[i]))
            print("Byl vracen vysledek: {}".format(ib113_double_all_in[i]))
            print("Byl ocekavan vysledek: {}".format(ib113_double_all_out[i]))
            break

    if not failure:
        print("OK")


ib113_create_doubled_in: List[List[int]] = [[1, 4, 2, 5], [0], []]
ib113_create_doubled_in_backup: List[List[int]] = [[1, 4, 2, 5], [0], []]
ib113_create_doubled_out: List[List[int]] = [[2, 8, 4, 10], [0], []]


def ib113_test_create_doubled() -> None:
    print("Testovani funkce create_doubled: ", end="")
    failure = False

    for i in range(len(ib113_create_doubled_in)):
        res = create_doubled(ib113_create_doubled_in[i])
        if not isinstance(res, list):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu list, ale typu {}"
                  .format(type(res)))
            break
        if res != ib113_create_doubled_out[i]:
            failure = True
            print("NOK")
            print("Seznam nebyl {} zmenen koretne."
                  .format(ib113_create_doubled_in_backup[i]))
            print("Byl vracen vysledek: {}"
                  .format(ib113_create_doubled_in[i]))
            print("Byl ocekavan vysledek: {}"
                  .format(ib113_create_doubled_out[i]))
            break
        if ib113_create_doubled_in[i] != ib113_create_doubled_in_backup[i]:
            failure = True
            print("NOK")
            print("Puvodni seznam byl {} zmenen na {}."
                  .format(ib113_create_doubled_in_backup[i],
                          ib113_create_doubled_in[i]))

    if not failure:
        print("OK")


ib113_flatten_in: List[List[List[int]]] = [[[0, 2, 3], [1, 2, 3], [9, 10]],
                                           [[], [0], []], [[], []]]
ib113_flatten_out: List[List[int]] = [[0, 2, 3, 1, 2, 3, 9, 10], [0], []]


def ib113_test_flatten() -> None:
    print("Testovani funkce flatten: ", end="")
    failure = False

    for i in range(len(ib113_flatten_in)):
        res = flatten(ib113_flatten_in[i])
        if not isinstance(res, list):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu list, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_flatten_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup {} nebyl vracen spravny vysledek"
                  .format(ib113_flatten_in[i]))
            print("Byl vracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".format(ib113_flatten_out[i]))
            break

    if not failure:
        print("OK")


ib113_vigenere_in = (("pampeliska", "klic"), ("abcdef", "abc"))
ib113_vigenere_out = ("ZLUROWQUUL", "ACEDFH")


def ib113_test_vigenere() -> None:
    print("Testovani funkce vigenere: ", end="")
    failure = False

    for i in range(len(ib113_vigenere_in)):
        res = vigenere(ib113_vigenere_in[i][0], ib113_vigenere_in[i][1])
        if not isinstance(res, str):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu str, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_vigenere_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" a klic \"{}\" nebyl vracen spravny vystup"
                  .format(ib113_vigenere_in[i][0], ib113_vigenere_in[i][1]))
            print("Byl vracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".format(ib113_vigenere_out[i]))
            break

    if not failure:
        print("OK")


ib113_tuple_reverse_in = (("ABC", 2), ("HESLOJETAJEMNO", 3),
                          ("SEHJOLATEMEJON", 3))
ib113_tuple_reverse_out = ("BAC", "SEHJOLATEMEJON", "HESLOJETAJEMNO")


def ib113_test_tuple_reverse() -> None:
    print("Testovani funkce tuple_reverse: ", end="")
    failure = False

    for i in range(len(ib113_tuple_reverse_in)):
        res = tuple_reverse(ib113_tuple_reverse_in[i][0],
                            ib113_tuple_reverse_in[i][1])
        if not isinstance(res, str):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu str, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_tuple_reverse_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" a n = {} nebyl vracen spravny vystup"
                  .format(ib113_tuple_reverse_in[i][0],
                          ib113_tuple_reverse_in[i][1]))
            print("Byl vracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}"
                  .format(ib113_tuple_reverse_out[i]))
            break

    if not failure:
        print("OK")


# Zde muzete vkladat vlastni testy
if __name__ == '__main__':
    ib113_test_nonzero_product()
    print()
    ib113_test_double_all()
    print()
    ib113_test_create_doubled()
    print()
    ib113_test_flatten()
    print()
    ib113_test_vigenere()
    print()
    ib113_test_tuple_reverse()
