# ################################## HW3 ################################## #
"""
Pokyny:
- Deadline odevzdani: 31. 10. 2021 23:59
- Odevzdejte jediny soubor
- Muzete si vytvaret pomocne funkce, pokud chcete.
- V pripade, ze chcete vytvaret vlastni testy, vkladete je na prislusne misto
    na konci souboru.
    - Pred odevzdanim vlastni modifikace testu smazte.
- Piste srozumitelny kod, pouzivejte vhodne nazvy promennych a funkci.
- Dodrzujte prosim standard pep8.
- Nemente hlavicky pripravenych funkci.
- Pripadne nejasnosti muzete resit v diskuznim foru. Pokud by ale mela otazka
    obsahovat kusy kodu, nebo neco, co by mohli ostatni studenti opsat, tak
    napiste radeji email.
- Pokud nevite, jak nejaky priklad vyresit kompletne, napiste do komentare,
    co vasemu reseni chybi.
- Neopisujte. Nestoji to za to. Dostanete zaporne body a budete muset ulohu
    stejne vypracovat sami.

Zadani:
Clovece nezlob se:

- Ukol 1: Vytvorte simulator zjednodusene a upravene hry "Clovece nezlob se".
    (20 bodu)
- Ukol 2: Vytvorte funkci, ktery analyzuje jaka je prumerna delka
    (vrati typ float) hry pro zadany pocet poli a pocet her.
    (5 bodu)
- Ukol 3: Pomoci funkce z ukolu 2 zjistete a vypiste prumerne delky her pro
    plany o velikostech 2-50.
    (5 bodu)

Pravidla:
- Hraje se na hracim planu o n polich.
- Figurka zacina na jedne strane hraciho planu na pozici 1.
- Haze se kostkou (1-6)
    - Kdyz padne 6, hazi se znovu (i opakovane)
    - Pokud na kostce padne 5, ruší se všechny naházené hodnoty a hráč se toto
      kolo neposouvá.
    - Figurka se posunuje o soucet hodnot z kostek, zustava stat ocitla-li
        by se za cilem.
    - Hra konci kdyz figurka dorazi na posledni pole.
    - Napr. 6 6 1 => Posun o 13 (pokud neprekroci cil, jinak se neposouva)
    - 6 6 6 5 => Neposouva se
    - 4 => Posun o 4 vpred (pokud neprekroci cil, jinak se neposouva)
    - 5 => Neposouva se

Poznamky:
- Pri delce hraciho planu < 2 skoncete funkci a vypiste nejakou
    smysluplnou hlasku.
- Figurka se posunuje bud o celkovy soucet hodu na kostkach, nebo vubec
    (v situaci, kdy by presla domecek).
"""

from random import randint

# Vytvorte simulator zjednodusene hry "Clovece nezlob se" dle pravidel
# uvedenych na zacatku souboru.

#   :param length:  Velikost hraciho planu
#   :param output:  True, pokud se maji vypisovat informace o probihajici hre
#                   na standardni vystup. False, pokud funkce nic nevypisuje
#   :return: (int)  Cele cislo urcujici, ve kterem kole byla hra dohrana v
#                   pripade, ze delka planu je alespon 2; jinak vraci None

# Ukazkovy vystup po zavolani game(35) muze vypadat napriklad takto:
# 1. round: 3 -> New position: 4
# 2. round: 4 -> New position: 8
# 3. round: 6 6 1 -> New position: 21
# 4. round: 5 -> New position: 21
# 5. round: 6 5 -> New position: 21
# 6. round: 6 4 -> New position: 31
# 7. round: 4 -> New position: 35
# Game ended in 7. round.


# Pozn. Parametr output=True nastavuje implicitni hodnotu parametru. Pokud
#   byste volali funkci game(15), pak se parametr output nastavi na True.
#   Pokud chcete mit parametr nastaven na False, volejte funkci napriklad
#   takto: game(15, False)
import random
def game(length: int, output: bool = True) -> int:
    if length < 2:
        print("Your gameplan is too short!")
        return None
    position = 0
    throw_count = 1
    over_6_sum = ""
    while position < length:
        throw = random.randint(a=1, b=6)
        if throw == 5:
            position = position + 0
        elif throw == 6:
            throw_6_sum = 6
            over_6_sum += "6 "
            throw = random.randint(a=1, b=6)
            while throw == 6:
                over_6_sum += "6 "
                throw_6_sum += 6
                throw = random.randint(a=1, b=6)
            if throw == 5:
                throw_6_sum = 0
            else:
                throw_6_sum += throw
            over_6_sum += str(throw)

            if (position + throw_6_sum) <= length:
                position += throw_6_sum
        else:
            if (position + throw) <= length:
                position += throw
        throw_count += 1
        if over_6_sum != "":
            throw = over_6_sum
        if output == True:
            print(f"{throw_count}. round: {throw} -> New position : {position}")
        over_6_sum = ""
    if output == True:
        print((f"Game ended in {throw_count}. round"))
    else:
        return (throw_count)



# Funkce, ktera analyzuje, jaka je prumerna delka (vrati typ float) hry pro
# zadany pocet poli a pocet her. Samotna funkce nic nevypisuje.

#   :param length:  Velikost hraciho planu
#   :param count:   Kolikrat se ma dana hra hrat pro urceni prumerne delky
#   :return: (float)    Prumerna delka hry clovece na danem planu
def game_analysis(length: int, count: int) -> float:
    sum_duration = 0.0
    for i in range(count):
        sum_duration = sum_duration + game(length, False)
    return sum_duration / count


# Vypisuje na standardni vystup prumerne delky her pro plany o velikostech
# 2-50. Pocet simovanych her nad kazdym planem je urcen paramtrem count.
# (Pokud je count nastaven na hodnotu 10, tak hra nad planem velokosti 2
# probehne 10krat, nad planem velikosti 3 take 10krat, atd.

#   :param count: pocet her, ktere se maji simulovat nad danymi plany.

# Ukazkovy vystup po zavolani game_average_length(20):
# Plan with length: 2  ->  6.35
# Plan with length: 3  ->  3.3
# Plan with length: 4  ->  7.45
# Plan with length: 5  ->  6.05
# Plan with length: 6  ->  8.3
# Plan with length: 7  ->  7.95
# Plan with length: 8  ->  6.15
# Plan with length: 9  ->  6.95
# Plan with length: 10  ->  6.1
# Plan with length: 11  ->  5.95
# Plan with length: 12  ->  8.7
# Plan with length: 13  ->  8.3
# ...
def game_average_length(count: int):
    for i in range(2, 51):
        print(f"Plan with length: {i} -> {game_analysis(i, count)}")

########################################################################
#               Nasleduje spusteni hry                                 #
########################################################################

# Zde muzete vkladat vlastni testy
# Pro otestovani funkcnosti kodu muzete odkomentovat pripravena volani funkci
if __name__ == '__main__':
    game(170)
    print(game_analysis(40, 20))
    game_average_length(20)
    pass
