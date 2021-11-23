import re
from typing import List, Dict

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

# Vypiste k nejcastejsich slov delky alespon length

def top_k(data: Dict[str, int], k: int, length: int) -> None:
    data_subset = dict()
    for (key, value) in data.items():
        if len(str(key)) >= length:
            data_subset[key] = value

    data_subset = sorted(data_subset.items(), reverse=True, key=lambda x: x[1])[0:k]
    print(data_subset)


top_k(load_data(), 5, 8)


# Vypiste, kolikrat se v textu vyskytuji jednotliva pismena.
# https://is.muni.cz/auth/el/fi/podzim2021/IB113/um/skupiny_01_02_a_03/cviceni_11/devatero_pohadek.txt
# Tip: pro overeni, ze je dany znak pismeno, muzete pouzit funkci isalpha.


def freq_analysis(file_name: str) -> None:
    res_dict = {}
    with open(file_name, "r") as file:
        text = file.read().lower()

    for letter in text:
        if letter not in res_dict.keys() and letter.isalpha():
            count = text.count(letter)
            res_dict[letter] = count

    return res_dict

freq_analysis("devatero_pohadek.txt")


def find_regexp(regexp, file_name="slovnik.txt"):
    with open(file_name, "r", encoding="utf-8") as my_file:
        for line in my_file:
            if re.search(regexp, line):
                strip_line = line.rstrip()
                print(strip_line, end=", ")
    print("\n")

# Vypsat vsechny retezce, ktere obsahuji podretezec "oo"
# find_regexp(r"")
# Vypsat vsechny retezce, ktere zacinaji na "e" a konci na "le"
# Vypise pouze erteple, elle, emile,
# find_regexp(r"")
# Vypsat vsechny retezce, ktere obsahuji "a", "e", "i", "o", "u" v tomto
# poradi (ale ne nutne za sebou, napr. akademickou)
# find_regexp(r"")
# Vypsat vsechny retezce, ktere obsahuji podretezec delky 4
# tvoreny z pismen "rst" (napr. bratrstvi)
# find_regexp(r"")
# Vypsat vsechny retezce, dve "u" vzdalena od sebe 8 pozic (napr. "uhlovodiku")
# find_regexp(r"")
# Obsahuji pismeno "u" na druhe i predposledni pozici (napr. "luxus")
# find_regexp(r"")
# Krome prvniho a posledniho pismene, kde muze byt libovolne pismeno, obsahuji
# pouze samohlasky a maji presne 5 pismen (napr. "foyer")
# find_regexp(r"")


# Pro kazde pismeno v textu vypiste 5 pismen, ktere za nim nasleduji nejcasteji
# Doporucena struktura dat je Dict[str, Dict[str, int]], napriklad:
# "abcaaab" -> { "a": { "b": 2, "a": 2 }, "b": {"c" : 1}, ... }


def cond_freq_analysis(file_name: str):
    pass  # TODO


cond_freq_analysis("devatero_pohadek.txt")


# Napiste funkci text_imitation(filename, length), ktera analyzuje text
# v souboru filename. Funkce pak vygeneruje pseudo-nahodny text o length
# slovech. Text se generuje po slovech. Dalsi generovane slovo se nahodne
# vybira z tech, ktere v puvodnim textu po naposledy vygenerovanem slove
# nasledovaly.


def text_imitation(file_name: str, length: int) -> None:
    import random as rnm
    with open(file_name, "r") as file:
        text = file.read().lower()
    text = re.sub('[^a-ž\ \']+', " ", text)
    text_lst = list(text.split())

    text_random = ""
    last_pos = 0
    word_pos = 0
    for i in range(length):
        word_pos = rnm.randint(last_pos, len(text_lst) - 1)
        text_random += str(text_lst[word_pos] + " ")
        last_pos = word_pos

    print(text_random, end=" ")

text_imitation('devatero_pohadek.txt', 10)
print()
