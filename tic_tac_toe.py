from random import randrange


def user_moves_examples(user_moves_board, used_move):
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

def enter_move(board):
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
            user_move = int(input("Wprowadź swój ruch: "))
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


# Przebieg gry
# WAZNE do zrobienia:
# Czego jeszcze brakuje, żeby to było grywalną całością: nie widzę tu jeszcze głównej pętli gry,
# która na przemian wywołuje enter_move i draw_move, po każdym ruchu sprawdza victory_for (dla obu graczy)
# oraz sprawdza remis (czy make_list_of_free_fields zwraca pustą listę), i dopiero wtedy kończy grę.
# To jest ten brakujący "spoiwo" między funkcjami.
# user_moves_examples świetnie nadaje się do testów enter_move, ale zwróć uwagę, że sama w sobie nie
# zastępuje input() — musiałabyś ją jakoś "podłączyć" w miejsce input() w trakcie testu
# (to wracamy do tematu mock/nadpisywania input, o którym mówiłyśmy).

# tablica z poczatkowym ukladem pol, komputer zaczyna wiec jego pierwszy znak "X" jest juz na srodku
game_board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
# w slowniku players_move funkcje enter_move i draw_move sa tylko obiektami - a ich nazwa
# to zwykła etykieta wskazująca na obiekt funkcji w pamięci
# slownik pozwala na obsluge ....
players_moves = {"O": enter_move, "X": draw_move}

# glowna petla gry
# poczatkowy stan flagi, gdy gra trwa
end_of_game = False
# petla while dziala dopoki zmienna end_of_game nie zmieni sie na True, czyli jeden z graczy wygra lub bedzie remis
while not end_of_game:

    # petla for idzie po slowniku w kolejnosci w jakiej zostaly wpisane klucze,
    # dlatego po ruchu komputera na starcie pierwszy ruch wykonuje "O", czyli użytkownik
    for key, value in players_moves.items():

        # wyswietlanie tablicy gry
        display_board(game_board)
        # wywolanie funkcji ze slownika players_move: do zmiennej value zostaje przypisana funkcja enter_move -
        # gdy przypada kolej na ruch uzytkownika, draw_move - gdy przypada kolej na ruch komputera;
        # () oznaczaja, ze funkcje zostaja wywolane
        value(game_board)

        # sprawdzenie, czy gracz, ktory wykonal ruch wygral
        if victory_for(game_board, key):
            # wyswietlenie tablicy, gdy jeden z graczy wygral
            display_board(game_board)
            print("Zwyciezyl gracz", key)
            # break konczy petle for, end_of_game zmienia wartosc na True, zmienna while sprawdza jej wartosc
            # przy kolejnej iteracji i wtedy konczy swoje dzialenie
            end_of_game = True
            break

        # sprawdzenie, czy jest remis
        if make_list_of_free_fields(game_board) == []:
            # wyswietlenie tablicy, gdy jest remis
            display_board(game_board)
            print("Jest remis. Zaden z graczy nie wygral.")
            # break konczy petle for, end_of_game zmienia wartosc na True, zmienna while sprawdza jej wartosc
            # przy kolejnej iteracji i wtedy konczy swoje dzialenie
            end_of_game = True
            break


# TESTY

user_moves_board = [1, 3, "c", 12, -7, 4, 8]
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
# v_board_1 = [["X", "X", "X"], ["O", "X", "O"], ["O", 8, 9]]
# v_board_2 = [["X", "X", 3], ["O", "O", "O"], [7, 8, "X"]]
# v_board_3 = [["O", "X", "X"], ["O", "X", "O"], ["O", 8, 9]]
# v_board_4 = [["X", "X", "O"], ["O", "X", "O"], ["O", "O", 9]]
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