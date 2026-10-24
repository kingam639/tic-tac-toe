"""Testy do gry w kółko i krzyżyk (tic_tac_toe.py).

Sprawdzają victory_for, enter_move i make_list_of_free_fields za pomocą assert.
Uruchomienie: python test_tic_tac_toe.py (plik leży obok tic_tac_toe.py).
Jeśli na końcu pojawi się komunikat o przejściu testów, żaden assert nie zawiódł.
"""


from tic_tac_toe import make_list_of_free_fields, victory_for, enter_move
from unittest.mock import patch


def test_victory_for(test_cases):
    """Sprawdza scenariusze testowe, gdy wygrywa jeden z graczy, jest remis lub gra jest niezakonczona."""
    for board, sign, result, message in test_cases:
        assert victory_for(board, sign) == result, f"{message}: dla {board} oczekiwano {result}"


def test_enter_move():
    """Sprawdza enter_move na każdym scenariuszu z enter_move_test_cases, bez czekania na klawiaturę."""
    for start_board, moves, expected_board in enter_move_test_cases:
        # patch podmienia input() na czas tego bloku: kolejne wywołania input()
        # zwracają kolejne elementy moves, zamiast czekać na wpisanie z klawiatury
        with patch('builtins.input', side_effect=moves) as mock_input:
            # enter_move niczego nie zwraca, tylko zmienia planszę w miejscu
            enter_move(start_board)
            # po wywołaniu start_board jest już zmieniona, więc porównuję ją z oczekiwaną;
            # przy błędzie komunikat wskazuje, który scenariusz zawiódł
            assert start_board == expected_board, f"Zawiodl test z lista ruchow: {moves}"
        # kazda wartosc z listy ruchow powinna zostac zuzyta, wiec input() wywolano tyle razy, ile jest ruchow
        assert mock_input.call_count == len(moves), (f"input() wywolano {mock_input.call_count} razy, "
                                                     f"a ruchow bylo {len(moves)}: {moves}")


def test_make_list_of_free_fields(test_cases):
    """Sprawdza, czy funkcja zwraca prawidlowa liste wolnych pol w postaci krotek (rzad, kolumna)."""
    for board, expected_free_fields in test_cases:
        result = make_list_of_free_fields(board)
        # przy bledzie komunikat pokazuje plansze, wynik funkcji i wynik oczekiwany
        assert result == expected_free_fields, (f"Funkcja nie zwrocila poprawnej listy krotek dla planszy {board}: "
                                                f"jest {result}, a powinno byc {expected_free_fields}")


# Testy funkcji victory_for(board,sign) z assert

# wygrana w każdej z 8 linii - Wygraną można zrobić na 8 sposobów: 3 wiersze, 3 kolumny i 2 przekątne.

# Każda plansza dostaje dwa assert: jeden dla gracza, który wygrał (oczekuję True),
# i jeden dla jego przeciwnika na tej samej planszy (oczekuję False).
# Oczekiwany wynik ustalam z zasad gry, zanim uruchomię kod, a komunikat
# po przecinku pokazuje się tylko wtedy, gdy test zawiedzie.

win_board_1 = [["X", "X", "X"], ["O", "X", "O"], ["O", 8, 9]]
win_board_2 = [["X", "X", 3], ["O", "O", "O"], [7, 8, "X"]]
# przypadek testuje dodatkowo linie, w której brakuje tylko jednego znaku:
win_board_3 = [["O", 2, "O"], ["O", "X", "O"], ["X", "X", "X"]]
win_board_4 = [["O", "X", "X"], ["O", "X", "O"], ["O", 8, 9]]
win_board_5 = [["O", "X", 3], ["O", "X", 6], [7, "X", 9]]
win_board_6 = [["X", "X", "O"], ["X", "X", "O"], [7, 8, "O"]]
win_board_7 = [["X", 2, 3], [4, "X", 6], ["O", "O", "X"]]
win_board_8 = [["O", 2, "X"], ["O", "X", 6], ["X", 8, 9]]
# pełna plansza bez zwycięzcy
tie_board_1 = [["X", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]
tie_board_2 = [["O", "O", "X"], ["X", "X", "O"], ["O", "X", "X"]]
# plansza w trakcie gry, bez zwycięzcy
no_winner_board = [[1, "O", 3], [4, "X", "O"], [7, "X", 9]]

victory_for_test_cases = [(win_board_1, "X", True, "X ma górny rząd"),
                          (win_board_1, "O", False, "O nie wygrał"),
                          (win_board_2, "O", True, "O ma srodkowy rzad"),
                          (win_board_2, "X", False, "X nie wygral"),
                          (win_board_3, "X", True, "X ma dolny rzad"),
                          (win_board_3, "O", False, "O nie wygral"),
                          (win_board_4, "O", True, "O ma lewa kolumne"),
                          (win_board_4, "X", False, "X nie wygral"),
                          (win_board_5, "X", True, "X ma srodkowa kolumne"),
                          (win_board_5, "O", False, "O nie wygral"),
                          (win_board_6, "O", True, "O ma prawa kolumne"),
                          (win_board_6, "X", False, "X nie wygral"),
                          (win_board_7, "X", True, "X ma pierwsza przekatna"),
                          (win_board_7, "O", False, "O nie wygral"),
                          (win_board_8, "X", True, "X ma druga przekatna"),
                          (win_board_8, "O", False, "O nie wygral"),
                          (tie_board_1, "X", False, "X nie wygral"),
                          (tie_board_1, "O", False, "O nie wygral"),
                          (tie_board_2, "X", False, "X nie wygral"),
                          (tie_board_2, "O", False, "O nie wygral"),
                          (no_winner_board, "X", False, "X nie wygral"),
                          (no_winner_board, "O", False, "O nie wygral")]

# Test funkcji enter_move(board) z mock

# Plansze startowe przed rozpoczeciem testow
board_invalid_type = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_out_of_range = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_occupied_field = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_valid_move = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_boundary_low = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_boundary_high = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
# Plansze po zasymulowaniu ruchu uzytkownika
board_invalid_type_expected = [[1, 2, "O"], [4, "X", 6], [7, 8, 9]]
board_out_of_range_expected = [[1, 2, 3], [4, "X", 6], ["O", 8, 9]]
board_occupied_field_expected = [[1, 2, 3], [4, "X", "O"], [7, 8, 9]]
board_valid_move_expected = [[1, "O", 3], [4, "X", 6], [7, 8, 9]]
board_boundary_low_expected = [["O", 2, 3], [4, "X", 6], [7, 8, 9]]
board_boundary_high_expected = [[1, 2, 3], [4, "X", 6], [7, 8, "O"]]

# Scenariusze testowe dla enter_move. Każdy scenariusz sklada sie z krotki:
# (plansza startowa, ruchy "wpisywane" przez użytkownika, plansza oczekiwana po teście).
# Lista ruchów zawsze kończy się poprawnym ruchem, bo enter_move pyta w kółko,
# aż dostanie poprawny. Każdy scenariusz ma własną planszę startową, bo enter_move
# zmienia planszę w miejscu i wspólna plansza przenosiłaby zmiany między testami.
enter_move_test_cases = [
    # zły typ: "c" nie jest liczbą, potem pole 3 -> "O" w 1. rzędzie, 3. kolumnie
    (board_invalid_type, ["c", "3"], board_invalid_type_expected),
    # zły zakres: 0 i 10 są poza 1-9, potem pole 7 -> "O" w 3. rzędzie, 1. kolumnie
    (board_out_of_range, ["0", "10", "7"], board_out_of_range_expected),
    # zajęte pole: pole 5 zajmuje "X", potem wolne pole 6 -> "O" w 2. rzędzie, 3. kolumnie
    (board_occupied_field, ["5", "6"], board_occupied_field_expected),
    # poprawny ruch: pole 2 jest wolne, więc ruch przechodzi za pierwszym razem
    (board_valid_move, ["2"], board_valid_move_expected),
    # poprawny ruch: pole 1, to pole graniczne i jest wolne, więc ruch przechodzi za pierwszym razem
    (board_boundary_low, ["1"], board_boundary_low_expected),
    # poprawny ruch: pole 9, to pole graniczne i jest wolne, więc ruch przechodzi za pierwszym razem
    (board_boundary_high, ["9"], board_boundary_high_expected)
]


# Testy funkcji make_list_of_free_fields(board) z assert
# plansze opisujace rozne scenariusze gry - 1. poczatek gry - plansza jest niezapelniona,
# 2. srodek gry - plansza jest czesciowo zapelniona, 3. koniec gry - nie ma wolnych pol na planszy
# i 4. wartosc graniczna - na planszy zostalo dokladnie jedno wolne pole
board_game_start = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_mid_game = [["X", 2, "O"], [4, "X", 6], [7, "X", "O"]]
board_full = [["X", "O", "O"], ["O", "X", "X"], ["X", "X", "O"]]
# wartosc graniczna: na planszy zostalo dokladnie jedno wolne pole (pole 6)
board_one_free = [["X", "O", "X"], ["O", "X", 6], ["O", "X", "O"]]
# wolne pola jako indeksy (rzad, kolumna) liczone od 0, wiersz po wierszu, tak jak zwraca je funkcja;
# kolejnosc ma znaczenie, bo lista jest porownywana przez ==
free_fields_game_start = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
free_fields_mid_game = [(0, 1), (1, 0), (1, 2), (2, 0)]
# [] dla free_fields_full oznacza, ze wszystkie pola na planszy zostaly zapelnione
free_fields_full = []
free_fields_one = [(1, 2)]

# lista przypadkow testowych z parami: dane wejsciowe - plansza z postawionymi przez graczy znakami "X", "O",
# oczekiwany wynik - lista krotek z polami na ktorych nie ma jeszcze znaku "X", "O" o budowie (rzad, kolumna)
free_fields_test_cases = [(board_game_start, free_fields_game_start),
                          (board_mid_game, free_fields_mid_game),
                          (board_full, free_fields_full),
                          (board_one_free, free_fields_one)]

test_victory_for(victory_for_test_cases)
test_enter_move()
test_make_list_of_free_fields(free_fields_test_cases)

# komunikat o przejsciu testow wyswietli sie, jesli zaden assert nie wyswietli bledu
print("Wszystkie testy przeszly.")