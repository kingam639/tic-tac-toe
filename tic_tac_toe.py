from random import randrange


def user_moves_examples(user_moves_board, used_move):
    # TODO: Jedna drobna uwaga: w pierwszym zdaniu masz "user_moves_board" opisane jako listę
    #  "do przetestowania", ale w tej chwili ta sama lista pełni już inną rolę w Twojej nowej
    #  pętli (źródło do konsumowania, a nie "dane testowe" w sensie assertów). To nie błąd,
    #  tylko do rozważenia, czy nazwa parametru i jej opis nadal dobrze pasują do tego, jak
    #  faktycznie jej teraz używasz — możesz to zostawić bez zmian, to nie jest konieczne.
    """The function chooses the user's move from the list of sample user moves and checks if the user
    hasn't used the move yet. If not, it returns the move to imitate the user's move."""
    # petla for przechodzi przez kazdy element na liscie z przykladowymi ruchami uzytkownika
    for move in user_moves_board:
        # jesli przykladowy ruch nie zostal jeszcze uzyty, dodaje go do listy uzytych ruchow
        # i zwraca ten ruch jako symulacje ruchu uzytkownika
        if move not in used_move:
            used_move.append(move)
            return move


def display_board(board):
    """The function accepts one parameter containing the board's current status
    and prints it out to the console."""
    # tablica ma strukture [[1,2,3], [4,5,6], [7,8,9]]
    # ulozenie pol na planszy za pomoca petli for
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for field in row:
            print("|  ", field, "  ", end="") # end - print nie przechodzi do nowej linii
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board, user_move=None):
    """The function accepts the board's current status, asks the user about their move,
    checks the input, and updates the board according to the user's decision."""
    # użytkownik wykonuje ruch wprowadzając numer pola, w którym chce postawić znak
    # - liczba musi być nie tylko prawidłowa, ale i legalna, tzn. musi to być liczba
    # całkowita, większa od 0 i mniejsza od 10, a także nie może to być liczba,
    # która odnosi się do wcześniej zaznaczonego, a więc zajętego już, pola;
    # flaga free_field jest ustawiona na True, jesli zmieni wartosc na False bedzie to znaczylo, ze uzytkownik
    # wspisal symbol "O" na polu, ktore jest "puste"
    free_field = True
    while free_field:
        # blok try except sprawdza czy uzytkownik wpisal int
        try:
            # instrukcja sprawdza, czy podczas wywolywania funkcji wprowadzono argument user_move "na sztywno"
            # jesli nie, pyta uzytkownika o ruch
            if user_move is None:
                user_move = input("Wprowadź swój ruch: ")
            # konwersja ruchu uzytkownika na int, by sprawdzic, czy wytypowal odpowiednie pole na znak "O"
            user_move = int(user_move)

        # jesli uzytkownik nie wpisal int funkcja wyrzuci wyjatek,
        # a nastepnie wroci na poczatek funkcji i ponownie uruchmi petle while
        except ValueError:
            print("Nie wpisales liczby. Sprobuj ponownie.")
        # blok else wykona sie, gdy przejdzie pomyslnie przez blok try (uzytkownik podal int)
        else:
            # sprawdza, czy uzytkownik wpisal liczbe z zakresu 1-9 i czy pole na tablicy jest wolne
            if 0 < user_move < 10:
                # petla for przechodzi przez kazdy rzad gry i sprawdza,
                for row in board:
                    if user_move in row:
                        # funkcja index zwraca indeks pierwszego znalezionego elementu -
                        # znajduje pod jakim indeksem znajduje sie ruch uzytkownika
                        indeks = row.index(user_move)
                        # print(indeks)
                        # znak "O" (kolko) zostaje wpisany na pole wybrane przez uzytkownika
                        row[indeks] = "O"
                        # flaga zmienia wartosc na False i konczy wykonywanie petli while,
                        # bo uzytkownik wpisal dobry ruch
                        free_field = False
                        # break - konczy wykonywanie petli for, bo znaleziono indeks pola,
                        # ktore wybral uzytkownik na wpisanie "O" (kolka)
                        break
                # jesli nie znaleziono pola, w ktore wyblak uzytkownik na wpisanie znaku "O" (kolka)
                # oznacza to, ze miejsce ktore wybral uzytkownik jest juz zajete
                else:
                    print("To pole jest juz zajete. Sprobuj ponownie.")
            # uzytkownik wpisal liczbe nie znajdujaca sie w zakresie 1-9
            else:
                print("Twój ruch nie miesci sie w zakresie 1-9. Sprobuj ponownie.")


# Dane trzymasz w jednej liście krotek (wejście, oczekiwany wynik), a sama asercja jest napisana raz i wykonuje się
# dla każdego przypadku z listy.
# Co do Twojego pytania „czy enter_move też testować assertami" — tak, tylko tutaj assert sprawdza nie to,
# co funkcja zwraca (bo enter_move nic nie zwraca), tylko stan planszy po jej wywołaniu. Pomyśl:
# skoro enter_move modyfikuje board w miejscu, to po jej wywołaniu możesz sprawdzić assert board == oczekiwana_plansza.
# Zanim przełożysz to na pętlę z wieloma scenariuszami na raz, mam dla Ciebie pytanie do przemyślenia,
# bo to jest tu nieco trudniejsze niż przy victory_for: każdy scenariusz dla enter_move potrzebuje własnej,
# świeżej planszy startowej (bo funkcja ją modyfikuje), a nie jednej wspólnej planszy używanej przez wszystkie
# przypadki po kolei. Zastanów się, czy w swojej liście przypadki obok user_move i oczekiwanego wyniku, nie powinnaś
# trzymać też osobnej planszy dla każdego scenariusza.
# Zanim napiszesz pętlę, rozpisz najpierw te 3-4 scenariusze, o których już mówiłyśmy
# (zły typ, poza zakresem, zajęte pole, poprawny ruch), każdy z: jaka plansza startowa, jaka lista
# ruchów do enter_move (pamiętaj: zły ruch + poprawny na końcu, bo funkcja kończy się po pierwszym sukcesie),
# jaka plansza oczekiwana na końcu. Pokaż mi tę listę, zanim przejdziemy do kodu.
test_move = ["c", "0", "10", "5", "2"]
game_board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
# Plansze startowe przed rozpoczeciem testow
board_zly_typ = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_zly_zakres = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_zajete_pole = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_poprawny_ruch = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
board_zly_typ_po_tescie = [[1, 2, "O"], [4, "X", 6], [7, 8, 9]]
board_zly_zakres_po_tescie = [[1, 2, 3], [4, "X", 6], ["O", 8, 9]]
board_zajete_pole_po_tescie = [[1, 2, 3], [4, "X", "O"], [7, 8, 9]]
board_poprawny_ruch_po_tescie = [[1, "O", 3], [4, "X", 6], [7, 8, 9]]

# TODO: Spróbuj teraz dopisać do każdej z 4 scenariuszy (zły typ, zły zakres, zajęte pole, poprawny ruch od razu)
#  trzy rzeczy razem: nazwę planszy startowej, listę wartości kończącą się sukcesem, i nazwę/zawartość oczekiwanej
#  planszy końcowej. Dla "zły zakres" możesz zostawić jeden scenariusz z listą zawierającą obie złe wartości po kolei,
#  np. ["0", "10", "5"], zamiast dwóch osobnych plansz — to dobry moment, żeby to uprościć.

# Przypadki testowe do testowania ruchow uzytkownika.
# Scenariusze obejmuja: zly typ - testuje styp str, zly zakres - testuje zakresy graniczne 0 i 10, zajete pole
# - testuje pole 5 zajete przez znak "X", poprawny ruch - testuje pole 2, ktore znajduje sie na planszy i jest puste
test_cases = [
    (board_zly_typ, ["c", "3"], board_zly_typ_po_tescie),
    (board_zly_zakres, ["0", "10", "7"], board_zly_zakres_po_tescie),
    (board_zajete_pole, ["5", "6"], board_zajete_pole_po_tescie),
    (board_poprawny_ruch, ["2"], board_poprawny_ruch_po_tescie)
]


from unittest.mock import patch

@patch('builtins.input', side_effect=["c", "3"])
def test_cos(mock_input):
    # w środku tej funkcji, każde wywołanie input() w testowanym kodzie
    # zwraca kolejno elemnty listy side_effect
    enter_move(board_zly_typ)
    assert board_zly_typ == board_zly_typ_po_tescie, "Znak 'O' nie zostal postawiony w zadnym polu."
# test_cases = [(test_move[0], game_board), (test_move[1], game_board),(test_move[2], game_board),
#              (test_move[3], game_board), (test_move[4], game_board_poprawny_ruch)]
test_cos()
user_moves_board = ["0", "10", "1", "9", "5", "1", "-2", "3.5", "c"]
used_move = []
# poczatkowa plansza: komputer zaczyna, wiec jego pierwszy znak "X" jest juz na srodku
# game_board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

# flaga free_moves ustawiona na True, jesli zmieni wartosc na False oznacza to, ze
# wszystkie przykladowe ruchy uzytkownika zostaly przetestowane
# free_moves = True
# while free_moves:
#     # funkcja user_moves_examples porownuje liste ruchow do zasymulowania, z tymi ktore
#     # juz zostaly przetestowane i jesli trafi na ruch ktory nie zostal jeszcze przetestowany zwraca go
#     move = user_moves_examples(user_moves_board, used_move)
#     # zwrocony ruch zostaje uzyty jako argument do funkcji enter_move by zasymulowac ruch uzytkownika
#     enter_move(board=game_board, user_move=move)
#     # jesli listy user_moves_board i used_move sa takie same, tzn ze wszytskie
#     # ruchy uzytkownika zostaly przetestowane i to koniec testow
#     print(move)
#     if user_moves_board == used_move:
#         free_moves = False
#         print("Wszystkie ruchy uzytkownika zostaly przetestowane.")
    # print(used_move)


def make_list_of_free_fields(board):
    """The function browses the board and builds a list of all the free squares;
    the list consists of tuples, while each tuple is a pair of row and column numbers."""
    # tablica do przechowywania krotek rzad, kolumna na ktorych mozna jeszcze postawic znaki "X", "O"
    free_fields_board = []
    for i in range(len(board)):
        # len(board) = 3, bo lista jest zagniezdzona i jako 1 element liczona jest
        # 1 wewnetrzna lista [[1,2,3](1 element), [4,5,6], [7,8,9]]
        # do zmiennej rzad przypisujemy 1 zagniezdzona liste z tablicy board
        row = board[i]
        # petla for przechodzi przez kazdy element z rzedu, przez ktory iteruje
        for j in range(len(row)):
            # warunek sprawdza, czy wartosc w polu jest rozna od 'O' i 'X'
            if row[j] != "O" and row[j] != "X":
                # jesli jest rozna, czyli na polu wciaz nie ma znaku "X" lub "O",
                # zostaje appendowana do listy pustych pol jako krotka o strukturze rzad, kolumna
                free_fields_board.append((i, j))
    # WAZNE ta lista musi byc zwrocona, bo przeciez nie ma jej nigdzie poza funkcja
    return free_fields_board


def victory_for(board, sign):
    """The function analyzes the board's status in order to check if
    the player using 'O's or 'X's has won the game and returns True if won or False if didn't win."""

    # tablica z kombinacjami pol, ktore daja zwyciestwo
    winning_fields = [[board[0][0], board[0][1], board[0][2]], [board[1][0], board[1][1], board[1][2]],
                      [board[2][0], board[2][1], board[2][2]],
                      [board[0][0], board[1][0], board[2][0]],[board[0][1], board[1][1], board[2][1]],
                      [board[0][2], board[1][2], board[2][2]],
                      [board[0][0], board[1][1], board[2][2]],[board[0][2], board[1][1], board[2][0]]]

    # petla for przechodzi przez tablice z mozliwymi wygranymi kombinacjami na planszy
    for combination in winning_fields:
        # flaga is_equal sluzy do sprawdzenia, czy w mozliwych zwycieskich kombinacjach pol sa tylko
        # znaki jednego typu, jesli nie flaga zmieni wartosc na False
        # ustawiam flage is_equal na True na początku każdej nowej porcji,
        # zanim zaczne ją sprawdzać od nowa — bo inaczej flaga "pamięta" wynik z poprzedniej porcji
        is_equal = True
        # sprawdzam przejscie przez pojedyncza wygrywajaca kombinacje
        for field in combination:
            # jesli podczas przejscia przez kazde pole trafi na symbol inny niz ten ktory sprawdza,
            # nastepuje zmiana flagi na False
            if field != sign:
                is_equal = False
        # po przejsciu przez kombinacje trzech pol sprawdzam, czy flaga jest caly czas True,
        # co oznacza ze uzytkownik wygral i zwracam True
        if is_equal:
            return True
    # jesli po przejsciu przez kazda kombinacje nie znaleziono trzech znakow, funkcja zwraca False
    return False

    # WAZNE to byla moja druga wersja petli for i chcialabym jeszcze do niej wrocic i poprawic ja... w tym tygodniu
    # petla for przechodzi przez tablice z mozliwymi wygranymi kombinacjami na planszy
    # for combination in winning_fields:
    #     print(combination)
    #     # zakladamy ze sign rowna sie pojedynczym polom w kombinacji wygranych pol
    #     while True:
    #         # sorawdzam przejscie przez pojedyncza kombinacje
    #         for field in combination:
    #             # jesli w polu jest znak inny niz sign, przerywamy wewnetrzna petle for,
    #             # poniewaz natrafilismy na pole w ktorym jest znak drugiego gracza lub nie ma w nim zadnego znaku
    #             if field != sign:
    #                 break
    #         return "Wygrałeś!"
    # return "Jest remis!"


def draw_move(board):
    """The function draws the computer's move and updates the board."""
    # randrange generuje 1 losowa liczbe z przedzialu - to przedzial otwarty
    # losowanie symbolu "X" symulujacego ruch komputera moze odbywac sie tylko posrod nie zajetych pol
    # dlatego funkcja draw_move wykorzystuje funkcje make_list_of_free_fields zwracajaca tablice krotek rzad, kolumna
    free_fields = make_list_of_free_fields(board)
    list_length = len(free_fields)
    # sposrod wszystkich wolnych pol, losowo wybierany jest indeks jednego z nich,
    # by postawic na nim znak 'X' symulujacy ruch komputera
    computer_move = randrange(list_length)
    print(free_fields[computer_move])
    # rozpakowywanie krotki (row, column) do zmiennych okreslajacych numer wiersza i kolumny na tablicy gry
    row, column = free_fields[computer_move]
    # umieszczenie znaku 'X' na wylosowanym polu - poprzez podanie rzedu i kolumny w ktorych ma byc
    board[row][column] = "X"

    # to bylo moje rozwiazanie, ale claude zasugerowal, ze nalezy uzyc wczesniejszej funkcji
    # make_list_of_free_fields
    # return comuter_move[1]
    # computer_move = randrange(1,10)
    # computer_move = 5
    # print(computer_move)
    # free_field = True
    # while free_field:
    #     # sprawdza, czy komputer wylosowal wolne pole na znak "X"
    #     for row in board:
    #         if computer_move in row:
    #             # funkcja index zwraca indeks pierwszego znalezionego elementu
    #             # znajduje pod jakim indeksem znajduje sie ruch komputera
    #             indeks = row.index(computer_move)
    #             # aktualizacja tablicy o ruch komputera
    #             row[indeks] = "X"
    #             free_field = False
    #             break
    #     else:
    #         computer_move = randrange(1,10)


# user_moves_board = [1, 3, "c", 12, -7, 4, 8]
#
# used_move = []
# free_moves = True
# while free_moves:
#     user_moves_examples(user_moves_board)
#     if user_moves_board[-1] == used_move[-1]:
#         free_moves = False
#     print(used_move)

# display_board(board)
# enter_move(board)
# free_fields_board = make_list_of_free_fields(board)
# print(free_fields_board)
# draw_move(board)
# display_board(board)
# TESTY victory_for

# Testy
# # lista zawierajaca wartosci do przetestowania
# boards_for_tests = [v_board_1, v_board_2, v_board_3, v_board_4]
# # przykladowe pola, gdzie uzytkownik moze wpisac znak 'O'
# user_moves = [1, 2, 7, 9]
# # Test gry
# # poczatkowy uklad na tablicy
# board = [[1, 2, 3],[4, "X", 6], [7, 8, 9]]
# for test_board in boards_for_tests:
#     # wyswietlanie aktualnego
#     print(test_board)
#     result_1 = victory_for(test_board, "X")
#     counter_1 += 1
#     print(counter_1, "Znak 'X'", result_1)
#
#     print(test_board)
#     result_2 = victory_for(test_board, "O")
#     counter_2 += 1
#     print(counter_2, "Znak 'O'", result_2)

# v_board_4 = [["X", "X", "O"], ["O", "X", "O"], ["O", "O", 9]]
# board = [[1, 2, 3],[4, "X", 6], [7, 8, 9]]
# result= victory_for(v_board_4, "X")
# print("Znak 'X'", result)
# result= victory_for(board, "X")
# print("Znak 'X'", result)
# result_2 = victory_for(board = [["X", "X", "X"], [4, 5, 6], [7, 8, 9]], sign = "X")
# print(result_2)

# result= victory_for(v_board_4, "X")
#
# print("Znak 'X'", result)

if __name__ == "__main__":
    # Przebieg gry
    # WAZNE do zrobienia:
    # Czego jeszcze brakuje, żeby to było grywalną całością: nie widzę tu jeszcze głównej pętli gry,
    # która na przemian wywołuje enter_move i draw_move, po każdym ruchu sprawdza victory_for (dla obu graczy)
    # oraz sprawdza remis (czy make_list_of_free_fields zwraca pustą listę), i dopiero wtedy kończy grę.
    # To jest ten brakujący "spoiwo" między funkcjami.
    # user_moves_examples świetnie nadaje się do testów enter_move, ale zwróć uwagę, że sama w sobie nie
    # zastępuje input() — musiałabyś ją jakoś "podłączyć" w miejsce input() w trakcie testu
    # (to wracamy do tematu mock/nadpisywania input, o którym mówiłyśmy).

    #poczatkowa plansza: komputer zaczyna, wiec jego pierwszy znak "X" jest juz na srodku
    game_board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

    # slownik laczy znak gracza z funkcja, ktora wykonuje jego ruch:
    # "O" (uzytkownik) -> enter_move, "X" (komputer) -> draw_move.
    # Nazwy funkcji sa tu tylko odwolaniami do nich (bez nawiasow), wiec nic sie jeszcze nie wykonuje.
    # Dzieki temu jeden kod w petli obsluguje obu graczy.
    players_moves = {"O": enter_move, "X": draw_move}

    # flaga informuje, czy gra sie zakonczyla; False oznacza, ze gra trwa
    end_of_game = False

    # glowna petla gry: kazdy jej obrot to jedna runda, czyli ruch uzytkownika i ruch komputera.
    # Konczy sie, gdy flaga zmieni wartosc na True (wygrana lub remis)
    while not end_of_game:

        # petla for bierze gracza po kolei ze slownika, w kolejnosci wpisania kluczy.
        # key to znak gracza, a value to funkcja, ktora wykonuje jego ruch.
        # Komputer zrobil juz pierwszy ruch, wiec w pierwszej rundzie zaczyna "O"
        for key, value in players_moves.items():

            # pokazanie planszy przed ruchem gracza
            display_board(game_board)
            # value to funkcja przypisana graczowi, a nawiasy ja wywoluja:
            # dla "O" wykona sie enter_move, dla "X" draw_move
            value(game_board)

            # sprawdzenie, czy gracz, ktory przed chwila zagral, wygral
            if victory_for(game_board, key):
                # pokazanie planszy z ostatnim, wygrywajacym ruchem
                display_board(game_board)
                print("Zwyciezyl gracz", key)
                # break przerywa petle for, a flaga zatrzymuje petle while
                # przy sprawdzaniu warunku na poczatku kolejnego obrotu
                end_of_game = True
                break

            # sprawdzenie remisu: brak wolnych pol, a nikt nie wygral
            if make_list_of_free_fields(game_board) == []:
                # pokazanie zapelnionej planszy
                display_board(game_board)
                print("Jest remis. Zaden z graczy nie wygral.")
                # tak samo jak przy wygranej: break konczy for, flaga konczy while
                end_of_game = True
                break

