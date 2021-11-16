import re
from typing import Dict, List

# Napiste funkci, ktera vrati soucet vsech hodnot ulozenych ve slovniku.
# Napr. d1 = {'a': 100, 'b': 200, 'c':300} => 600


def dict_sum(dct: Dict[str, int]) -> int:
    return sum(dct.values())


# Napiste funkci, ktera vezme dva slovniky a vrati novy, ktery obsahuje jejich
# soucet. Tj. pokud oba slovniky obsahuji polozky se stejnym klicem, pak ve
# vyslednem slovniku bude u daneho klice soucet hodnot z obou slovniku
# (ostatni polozky jsou vlozeny beze zmeny).
# Napr. d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# => {'a': 400, 'b': 400, 'd': 400, 'c': 300}



def add_two_dictionaries(dct_1: Dict[str, int], dct_2: Dict[str, int]) -> Dict[str, int]:
    dct_added = dict(dct_2)

    for key in dct_1:
        if key in dct_2.keys():
            dct_added[key] = dct_1[key] + dct_2[key]
        else:
            dct_added[key] = dct_1[key]
    return dct_added



# Napiste funkci, ktera vrati seznam(!) vsech hodnot,ktere osahuje dany
# slovnik (bez duplicit).


def unique_values(dct: Dict[str, int]) -> List[int]:
    dct_vals = []
    for val in dct.values():
        if val not in dct_vals:
            dct_vals.append(val)
    return dct_vals



# Nactete text ze souboru maj.txt a vypiste ho na obrazovku


def show_file_text() -> None:
    with open("maj.txt", "r", encoding = "utf-8") as textfile:
        for line in textfile:
            print(line, end = " ")

show_file_text()

# Misto vypsani na obrazovku je zkopirujte do noveho souboru.


def copy_to_other_file() -> None:
    maj_textlist = []
    with open("maj.txt", "r", encoding = "utf-8") as textfile:
        for line in textfile:
            maj_textlist.append(line)

    with open("maj_copy.txt", "w", encoding = "utf-8") as textfile:
        for element in maj_textlist:
            textfile.write(element)


copy_to_other_file()

# Pote text ulozte do noveho souboru opacne (obratte poradi pismen – tj.
# posledni pismeno bude prvni v novem souboru, predposledni druhe, ...)


def reversed_copy() -> None:
    maj_textlist = []
    with open("maj.txt", "r", encoding="utf-8") as textfile:
        for line in textfile:
            maj_textlist.insert(0, line)

    with open("maj_reverse.txt", "w", encoding="utf-8") as textfile:
        for element in maj_textlist:
            textfile.write(element[::-1])


reversed_copy()

# Obratte pouze poradi slov (posledni slovo bude na prvnim miste, predposledni
#  na druhem, ...), ale neobracejte poradi pismen v jednotlivych slovech

print()
print()

def reversed_words_copy() -> None:
    maj_textlist = []
    word_reverse = ""
    with open("maj.txt", "r", encoding="utf-8") as textfile:
        for line in textfile:
            maj_textlist.append(line)

    for element in maj_textlist:
        line_split = element.split(" ")
        for words in line_split:
            # words = words[::-1]
            word_reverse = words + " " + word_reverse

    print("".join(word_reverse))



reversed_words_copy()


# Nactete data ze souboru do vhodne struktury

import re
def load_data():

    # Poznamka: sherlock-holmes.txt musi byt ve stejnem adresari jako skript
    with open('sherlock-holmes.txt', 'r', encoding="utf-8") as file:
        dct: Dict[str, int] = {}

        # nacitani dat do slovniku
        for line in file:
            clear_line = re.sub('\W+', ' ', line)  # nechat jen pismena

            for word in clear_line.split():
                if word:  # jen neprazdna slova
                    dct[word] = dct.get(word, 0) + 1

    return dct


holmes_data = load_data()

# Top 10 nejcastejsich slov

def top_ten(data: Dict[str, int]) -> None:
    print(sorted(data.items(), reverse=True, key=lambda x: x[1])[0:10])


# Prumerna delka slova v textu


def word_average(data: Dict[str, int]) -> None:
        wordcount = sum(data.values())
        average = sum(len(w) * c for w, c in data.items()) / wordcount
        print(f'The text comprises of {wordcount} words with average length of {round(average, 2)} characters')


########################################################################
#               Nasleduje kod testu                                    #
########################################################################

ib113_dict_sum_in = ([{'a': 100, 'b': 200, 'c': 300}, {'x': 1000}])
ib113_dict_sum_out = (600, 1000)


def ib113_test_dict_sum() -> None:
    print("Testovani funkce dict_sum: ", end="")
    failure = False

    for i in range(len(ib113_dict_sum_in)):
        res = dict_sum(ib113_dict_sum_in[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_dict_sum_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_dict_sum_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_dict_sum_out[i]))
            break

    if not failure:
        print("OK")


ib113_add_two_dictionaries_in = ([({'a': 100, 'b': 200, 'c': 300},
                                   {'a': 300, 'b': 200, 'd': 400})])
ib113_add_two_dictionaries_out = [{'a': 400, 'b': 400, 'd': 400, 'c': 300}]


def ib113_test_add_two_dictionaries() -> None:
    print("Testovani funkce add_two_dictionaries: ", end="")
    failure = False

    for i in range(len(ib113_add_two_dictionaries_in)):
        res = add_two_dictionaries(ib113_add_two_dictionaries_in[i][0],
                                   ib113_add_two_dictionaries_in[i][1])
        if not isinstance(res, dict):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu dict, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_add_two_dictionaries_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_add_two_dictionaries_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_add_two_dictionaries_out[i]))
            break

    if not failure:
        print("OK")


ib113_unique_values_in = ([{'a': 5, 'b': 5, 'c': 4},
                           {'a': 1, 'b': 5, 'c': 1, 'd': 5},
                           {'a': 1, 'b': 5, 'c': 1, 'd': 1}])
ib113_unique_values_out = ([4, 5], [1, 5], [1, 5])


def ib113_test_unique_values() -> None:
    print("Testovani funkce unique_values: ", end="")
    failure = False

    for i in range(len(ib113_unique_values_in)):
        res = unique_values(ib113_unique_values_in[i])
        if not isinstance(res, list):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu list, "
                  "ale typu {}".format(type(res)))
            break
        if sorted(res) != sorted(ib113_unique_values_out[i]):
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_unique_values_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_unique_values_out[i]))
            break

    if not failure:
        print("OK")


# Zde muzete vkladat vlastni testy
if __name__ == '__main__':
    ib113_test_dict_sum()
    print()
    ib113_test_add_two_dictionaries()
    print()
    ib113_test_unique_values()
    print()
    LOADED_DATA = load_data()
    top_ten(LOADED_DATA)
    print()
    word_average(LOADED_DATA)
