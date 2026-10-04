from tic_tac_toe import user_moves_examples, display_board, make_list_of_free_fields, victory_for, draw_move

# TESTY z assert
# Testy funkcji victory_for
# 1. wygrana w każdej z 8 linii - Wygraną można zrobić na 8 sposobów: 3 wiersze, 3 kolumny i 2 przekątne.
vict_board_1 = [["X", "X", "X"],
                ["O", "X", "O"],
                ["O", 8, 9]]

# Co tu się dzieje:
# Pierwszy assert pyta: „gdy sprawdzę, czy X wygrał na tej planszy, czy wyjdzie True?"
# Tak ma być, bo X ma trzy znaki w pierwszym rzędzie.
# Drugi pyta o O na tej samej planszy. O nie ma żadnej pełnej linii, więc oczekiwane jest False.
# Wartość po == ustalasz sama, patrząc na planszę i znając zasady gry, jeszcze zanim uruchomisz kod.
# Tekst po przecinku pojawia się tylko wtedy, gdy test zawiedzie.

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


