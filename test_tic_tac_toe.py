from tic_tac_toe import make_list_of_free_fields, victory_for, enter_move
from unittest.mock import patch


# TESTY z assert
# Testy funkcji victory_for
# 1. wygrana w każdej z 8 linii - Wygraną można zrobić na 8 sposobów: 3 wiersze, 3 kolumny i 2 przekątne.

# Każda plansza dostaje dwa assert: jeden dla gracza, który wygrał (oczekuję True),
# i jeden dla jego przeciwnika na tej samej planszy (oczekuję False).
# Oczekiwany wynik ustalam z zasad gry, zanim uruchomię kod, a komunikat
# po przecinku pokazuje się tylko wtedy, gdy test zawiedzie.

vict_board_1 = [["X", "X", "X"],
                ["O", "X", "O"],
                ["O", 8, 9]]

assert victory_for(vict_board_1, "X") == True, "X ma górny rząd, powinno być True"
assert victory_for(vict_board_1, "O") == False, "O nie wygrał, powinno być False"

vict_board_2 = [["X", "X", 3],
                ["O", "O", "O"],
                [7, 8, "X"]]
assert victory_for(vict_board_2, "O") == True, "O ma srodkowy rzad, powinno byc True"
assert victory_for(vict_board_2, "X") == False, "X nie wygral, powinno byc False"

# dodatkowo linia, w której brakuje jednego znaku:
vict_board_3 = [["O", 2, "O"],
                ["O", "X", "O"],
                ["X", "X", "X"]]
assert victory_for(vict_board_3, "X") == True, "X ma dolny rzad, powinno byc True"
assert victory_for(vict_board_3, "O") == False, "O nie wygral, powinno byc False"

vict_board_4 = [["O", "X", "X"],
                ["O", "X", "O"],
                ["O", 8, 9]]
assert victory_for(vict_board_4, "O") == True, "O ma lewa kolumne, powinno byc True"
assert victory_for(vict_board_4, "X") == False, "X nie wygral, powinno byc False"

vict_board_5 = [["O", "X", 3],
                ["O", "X", 6],
                [7, "X", 9]]
assert victory_for(vict_board_5, "X") == True, "X ma srodkowa kolumne, powinno byc True"
assert victory_for(vict_board_5, "O") == False, "O nie wygral, powinno byc False"

vict_board_6 = [["X", "X", "O"],
                ["X", "X", "O"],
                [7, 8, "O"]]
assert victory_for(vict_board_6, "O") == True, "O ma prawa kolumne, powinno byc True"
assert victory_for(vict_board_6, "X") == False, "X nie wygral, powinno byc False"

vict_board_7 = [["X", 2, 3],
                [4, "X", 6],
                ["O", "O", "X"]]
assert victory_for(vict_board_7, "X") == True, "X ma pierwsza przekatna, powinno byc True"
assert victory_for(vict_board_7, "O") == False, "O nie wygral, powinno byc False"

vict_board_8 = [["O", 2, "X"],
                ["O", "X", 6],
                ["X", 8, 9]]
assert victory_for(vict_board_8, "X") == True, "X ma druga przekatna, powinno byc True"
assert victory_for(vict_board_8, "O") == False, "O nie wygral, powinno byc False"

# pełna plansza bez zwycięzcy
draw_board_1 = [["X", "O", "X"],
                ["X", "X", "O"],
                ["O", "X", "O"]]
assert victory_for(draw_board_1, "X") == False, "X nie wygral, powinno byc False"
assert victory_for(draw_board_1, "O") == False, "O nie wygral, powinno byc False"

draw_board_2 = [["O", "O", "X"],
                ["X", "X", "O"],
                ["O", "X", "X"]]
assert victory_for(draw_board_2, "X") == False, "X nie wygral, powinno byc False"
assert victory_for(draw_board_2, "O") == False, "O nie wygral, powinno byc False"

# plansza w trakcie gry, bez zwycięzcy
no_winner_board = [[1, "O", 3],
                [4, "X", "O"],
                [7, "X", 9]]
assert victory_for(no_winner_board, "X") == False, "X nie wygral, powinno byc False"
assert victory_for(no_winner_board, "O") == False, "O nie wygral, powinno byc False"


# Plansze startowe przed rozpoczeciem testow
board_zly_typ = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_zly_zakres = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_zajete_pole = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_poprawny_ruch = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_zly_typ_po_tescie = [[1, 2, "O"], [4, "X", 6], [7, 8, 9]]
board_zly_zakres_po_tescie = [[1, 2, 3], [4, "X", 6], ["O", 8, 9]]
board_zajete_pole_po_tescie = [[1, 2, 3], [4, "X", "O"], [7, 8, 9]]
board_poprawny_ruch_po_tescie = [[1, "O", 3], [4, "X", 6], [7, 8, 9]]

# Scenariusze testowe dla enter_move. Każdy to trójka:
# (plansza startowa, ruchy "wpisywane" przez użytkownika, plansza oczekiwana po teście).
# Lista ruchów zawsze kończy się poprawnym ruchem, bo enter_move pyta w kółko,
# aż dostanie poprawny. Każdy scenariusz ma własną planszę startową, bo enter_move
# zmienia planszę w miejscu i wspólna plansza przenosiłaby zmiany między testami.
test_cases = [
    # zły typ: "c" nie jest liczbą, potem pole 3 -> "O" w 1. rzędzie, 3. kolumnie
    (board_zly_typ, ["c", "3"], board_zly_typ_po_tescie),
    # zły zakres: 0 i 10 są poza 1-9, potem pole 7 -> "O" w 3. rzędzie, 1. kolumnie
    (board_zly_zakres, ["0", "10", "7"], board_zly_zakres_po_tescie),
    # zajęte pole: pole 5 zajmuje "X", potem wolne pole 6 -> "O" w 2. rzędzie, 3. kolumnie
    (board_zajete_pole, ["5", "6"], board_zajete_pole_po_tescie),
    # poprawny ruch: pole 2 jest wolne, więc ruch przechodzi za pierwszym razem
    (board_poprawny_ruch, ["2"], board_poprawny_ruch_po_tescie)
]


def test_enter_move():
    """Sprawdza enter_move na każdym scenariuszu z test_cases, bez czekania na klawiaturę."""
    for plansza_startowa, lista_ruchow, plansza_oczekiwana in test_cases:
        # patch podmienia input() na czas tego bloku: kolejne wywołania input()
        # zwracają kolejne elementy lista_ruchow, zamiast czekać na wpisanie z klawiatury
        with patch('builtins.input', side_effect=lista_ruchow):
            # enter_move niczego nie zwraca, tylko zmienia planszę w miejscu
            enter_move(plansza_startowa)
            # po wywołaniu plansza_startowa jest już zmieniona, więc porównuję ją z oczekiwaną;
            # przy błędzie komunikat wskazuje, który scenariusz zawiódł
            assert plansza_startowa == plansza_oczekiwana, f"Zawiodl test z lista ruchow: {lista_ruchow}"


test_enter_move()


