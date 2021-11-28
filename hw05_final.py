# ################################## HW5 ################################## #
"""
Pokyny:
- Deadline odevzdani: 28. 11. 23:59
- Odevzdejte jediny soubor
- Za ulohu lze ziskat maximalne 40 bodu.
- Muzete si vytvaret pomocne funkce, pokud chcete.
    - V teto uloze to je doporuceno
- V pripade, ze chcete vytvaret vlastni testy, vkladete je na prislusne misto
    na konci souboru.
    - Pred odevzdanim vlastni modifikace smazte.
- Piste srozumitelny kod, pouzivejte vhodne nazvy promennych a funkci.
- Dodrzujte standard pep8.
- Nemente hlavicky pripravenych funkci.
- Pripadne nejasnosti muzete resit v diskuznim foru. Pokud by ale mela otazka
    obsahovat kusy kodu, nebo neco, co by mohli ostatni studenti opsat, tak
    napiste radeji email.
- Pokud nevite, jak nejaky priklad vyresit kompletne, napiste do komentare,
    co vasemu reseni chybi.
- Neopisujte. Nestoji to za to. Dostanete zaporne body a budete muset ulohu
    stejne vypracovat sami.

Zadani:
Vytvorte program hrajici hru "Padajici piskvorky" uzivatele proti pocitaci
(na planu zadane velikosti). Tato variace piskvorek se hraje na dvourozmernem
hracim planu. Hra je podobna klasickym piskvorkam s tim rozdilem, ze pokud
jste na tahu, nevolite konkretni ctverecek, do ktereho byste umistili svuj
symbol, ale sloupec. Symbol v danem sloupci spadne dolu (nejvice, co to jde).
Vyhrava ten, kdo posklada 4 sve symboly v rade, sloupci nebo diagonale.

Zadani:
Vasim ukolem je implementovat:
1) Funkci show_state(state), ktera vypise dany plan na standardni vystup.
Plan je reprezentovan seznamem seznamu stejne delky, ktere obsahuji znaky
X (krizek), O (kolecko) nebo mezera pro neobsazene pole.
>> state = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 'O'],
         [' ', ' ', ' ', ' ', 'X'], [' ', 'O', ' ', ' ', 'X']]
>> show_state(state)

        O
        X
  O     X
- - - - -
0 1 2 3 4

2) Funkci strategy(state, symbol), ktera pro dany plan a symbol vrati pozici
(sloupec) tahu pocitace. Neni nutne aby byla nejak sofistikovana, muze
vracet nahodny sloupec v danem rozsahu.

>> state = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'X', ' ']]
>> strategy(state, 'O')
2

3) Funkci tictactoe(rows, cols, human_starts=True), ktera umoznuje hrat hru
padajicich piskvorek na planu o danem poctu radku a sloupcu. Muzete
predpokladat, ze zadana velikost planu je rozumna (alespon 4 a mene nez 26
sloupcu a radku). Parametr human_starts urcuje, zda zacina hrac nebo pocitac.
Vypis prubehu hry by mel vypadat stejne, jako v nasledujicich prikladech.
Funkce kontroluje, zda jsou tahy zadane hracem a pocitacem platne a pokud
nejsou, vyzve ho k novemu zadani. Pro hru pocitace volejte vyse uvedene
funkce show_state(state) a strategy(state, symbol). Nezapomente, ze hra muze
skoncit i remizou

Priklad hry, v nemz zacina hrac:

Na tahu je hrac
Do jakeho sloupce chces hrat? (do 0 do 9)? 5

          X
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je pocitac
Pocitac hraje do sloupce cislo 9

          X       O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je hrac
Do jakeho sloupce chces hrat? (do 0 do 9)? 6

          X X     O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je pocitac
Pocitac hraje do sloupce cislo 5

          O
          X X     O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je hrac
Do jakeho sloupce chces hrat? (do 0 do 9)? 4

          O
        X X X     O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je pocitac
Pocitac hraje do sloupce cislo 7

          O
        X X X O   O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je hrac
Do jakeho sloupce chces hrat? (do 0 do 9)? 3

          O
      X X X X O   O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9
Vyhral jsi!

Bodovani:
- Maximum je 40 bodu.
- Funkce tictactoe(rows, cols, human_starts=True) musi korektne provadet hru
    hrace a pocitace, kontrolovat zadane tahy hrace a urcit vyhru. Vypis se
    musi shodovat s vyse uvedenymi ukazkami.
- Zakladni variantou strategy je funkce, ktera dodrzuje pravidla, ale jinak
    hraje nahodne. Pokud vas program bude hrat "inteligentne" (napriklad ukonci
    hru, pokud bude mit moznost), ziskate bonusove body. Cim inteligentneji,
    tim vice bodu. V kazdem pripade napiste do komentare strucne vysvetleni,
    jak moc inteligentne program hraje. Kvalita tohoto popisu je take dulezita.

Nekolik tipu:
- Nez zacnete psat kod, rozmyslete si (nejlepe si i nakreslete) dekompozici
    problemu na jednodussi funkce. Jinak se v tom ztratite. Problem lze
    rozlozit ruzne, priklady uzitecnych funkci: is_won(state) nebo
    valid_move(move, state), ale v prubehu reseni by vas pak mely napadnout
    jeste dalsi. Kdykoliv zjistite, ze mate v programu duplicitni kod,
    zbavte se ho (napr. prave pomoci nove pomocne funkce). A vsechny funkce
    by mely zustat dostatecne kratke a prehledne.
- Zacnete variantou s nahodnymi tahy, rozumne chovani pridejte az potom.
    Pri dobre dekompozici by rozsirovani nemel byt problem.
- Zkuste si tuto hru parkrat zahrat (s nekym nebo i sami se sebou), pomuze
    vam to lepe pochopit, jak by mel pocitac optimalne hrat.
"""
# Import knihoven:

import numpy as np
from typing import List
from random import choice, randint

# Funkce vypise dany plan na standardni vystup. Plan je reprezentovan seznamem
#  seznamu stejne delky, ktere obsahuji znaky X (krizek), O (kolecko) nebo
#  mezera pro neobsazene pole.

# :param state:  Seznam seznamu obsahujici znaky X, 0, a mezera



def show_state(state: List[List[str]]) -> None:
    sublist_length = len(state[0])
    for element in state:
        if len(element) != sublist_length:
            return(print("ERROR: the length of sublists is not equal!"))
        for i in range(len(element)):
            if element[i] not in ["O", "X", " "]:
                return(print(f"ERROR: the value {element[i]} in a sublist is not acceptable, enter one of '0', ' ', 'X'!"))
    print()
    for i in range(len(state)):
        for j in range(len(state[i])):
            print(state[i][j], end=" ")
        print()
    for i in range(len(state[0])):
        print("_ ", end="")
    print()
    for i in range(len(state[0])):
        print(i, end=" ")

# show_state(state = np.full((3, 5), " "))

print()
print()

# Funkce pro dany plan state a symbol chr vrati pozici (sloupec) tahu
# pocitace.
# Pozn. Funkce neresi zadnou logiku hry ani vypisy, jen vraci sloupec, kam
# umistuje pocitac svuj symbol.

#    :param state:  Seznam seznamu obsahujici znaky X, 0, a mezera
#    :param chr:    Znak, ktery se ma vlozit
#    :return:       Sloupec, do ktereho se ma vlozit znak chr


def strategy(state: List[List[str]], chr: str) -> int:
# funkci jsem sice vytvoril, ale pak jsem ji nebyl schopny v hlavni casti pouzit tak, aby
    state_array_t = np.array(state).transpose()
    col_selection = []

    for i in range(len(state_array_t)):
        if " " in state_array_t[i]:
            col_selection.append(i)

    return [choice(col_selection), chr][0]

# print(strategy(state = np.full((3, 5), " "), chr = "X"))

print()
print()

# Funkce umoznuje hrat hru padajicich piskvorek na planu o danem poctu radku
# a sloupcu.

#   :param rows:    Pocet radku (4..25)
#   :param cols:    Pocet sloupcu (4..25)
#   :param human_starts: True, pokud zacina hrac, False jinak

def gameplan(rows, cols):
    gameplan_init = np.full((rows, cols), " ")
    return gameplan_init

# show_state(state = np.full((1, 5), " "))

def assign_chr(characters):
    #Tato funkce slouzi k rozdeleni, kdo z hracu hraje 'X' a kdo hraje 'O'
    chr_list = np.random.permutation(characters).tolist()
    return chr_list

def empty_row_index(col, arr):
    #Tato funkce nachazi index prazdneho radku, ktery pouzijeme k prirazovani do herniho pole
    for i in range(len(arr))[::-1]:
        if arr[i, col] == " ":
            return int(i)

def check_result(res_array):
    max_col = len(res_array[0])
    max_row = len(res_array)

    cols = [[]for c in range(max_col)]
    rows = [[]for r in range(max_row)]
    rdiag = [[] for r in range(max_row + max_col - 1)]
    ldiag = [[] for l in range(len(rdiag))]
    min_ldiag = -max_row + 1

    for i in range(max_col):
        for j in range(max_row):
            cols[x].append(test[y][x])
            rows[y].append(test[y][x])
            fdiag[x + y].append(test[y][x])
            bdiag[x - y - min_bdiag].append(test[y][x])
















def tictactoe(rows: int, cols: int, human_starts: bool = True):
    state_array = np.full((rows, cols), " ") #takto vytvorim array samych ' '
    undecided = True # Promenna pro pokracovani hry
    stepcount = int(human_starts) # Pocitadlo kroku, slouzi k prepinani mezi uzivatelem a pocitacem
    chr_division = assign_chr(["O", "X"])  #funkce
    cols_possible = []
    while undecided:
        show_state(state_array.tolist())
        print()
        if stepcount % 2 == 0:
            turn = [randint(0, cols - 1), chr_division[0]] #strategy(show_state(state_array), str(chr_division[0]))
            print("Na tahu je pocitac")
            print(f"Pocitac hraje do sloupce cislo {turn[0]}")
        else:
            print("Na tahu je hrac")
            turn = [int(input(f"Do jakeho sloupce chces hrat? (od {0} do {cols - 1}) \n")), str(chr_division[1])]


        stepcount += 1
        state_array[empty_row_index(int(turn[0]), state_array), int(turn[0])] = str(turn[1])


tictactoe(7, 7, False)



########################################################################
#               Nasleduje kod testu                                    #
########################################################################

# Zde muzete vkladat vlastni testy
# if __name__ == '__main__':
#     tictactoe(6, 6)
#     pass
