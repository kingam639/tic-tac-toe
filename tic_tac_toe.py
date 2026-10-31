from random import randrange


def display_board(board):
    """The function accepts one parameter containing the board's current status
    and prints it out to the console."""
    # tablica ma strukture [[1,2,3], [4,5,6], [7,8,9]]
    # ulozenie pol na planszy za pomoca petli for
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for field in row:
            print("|  ", field, "  ", end="")  # end - print nie przechodzi do nowej linii
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
    # wpisal symbol "O" na polu, ktore jest "puste"
    free_field = True
    while free_field:
        # blok try except sprawdza czy uzytkownik wpisal int
        try:
            # uzytkownik wpisuje pole na ktorym chce postawic znak "O"
            user_move = input("Wprowadź swój ruch: ")
            # konwersja ruchu uzytkownika na int, by sprawdzic, czy wytypowal odpowiednie pole na znak "O"
            user_move = int(user_move)

        # jesli uzytkownik nie wpisal int funkcja wyrzuci wyjatek,
        # a nastepnie wroci na poczatek funkcji i ponownie uruchomi petle while
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
                        # znak "O" (kolko) zostaje wpisany na pole wybrane przez uzytkownika
                        row[indeks] = "O"
                        # flaga zmienia wartosc na False i konczy wykonywanie petli while,
                        # bo uzytkownik wpisal dobry ruch
                        free_field = False
                        # break - konczy wykonywanie petli for, bo znaleziono indeks pola,
                        # ktore wybral uzytkownik na wpisanie "O" (kolka)
                        break
                # jesli nie znaleziono pola, w ktore wybral uzytkownik na wpisanie znaku "O" (kolka)
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
                      [board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]],
                      [board[0][2], board[1][2], board[2][2]],
                      [board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]

    # petla for przechodzi przez tablice z mozliwymi wygranymi kombinacjami na planszy
    for combination in winning_fields:
        # sprawdzam przejscie przez pojedyncza wygrywajaca kombinacje
        for field in combination:
            # jesli podczas przejscia przez kazde pole trafi na symbol inny niz ten ktory sprawdza,
            # nastepuje przerwanie petli
            if field != sign:
                break
        # else przy for wykonuje sie tylko wtedy, gdy petla nie zostala przerwana przez break,
        # czyli wszystkie 3 pola maja znak sign
        else:
            return True
    # jesli po przejsciu przez kazda kombinacje nie znaleziono trzech identycznych znakow, funkcja zwraca False
    # gracz z tym znakiem nie wygral (gra trwa, wygral przeciwnik albo jest remis)
    return False

# git commit -m "Sprzątanie tic_tac_toe.py: usunięto nieużywany kod i stare komentarze. victory_for: for...else zamiast flagi, uproszczenie warunku remisu"

def draw_move(board):
    """The function draws the computer's move and updates the board."""
    # losowanie symbolu "X" symulujacego ruch komputera moze odbywac sie tylko posrod nie zajetych pol
    # dlatego funkcja draw_move wykorzystuje funkcje make_list_of_free_fields zwracajaca tablice krotek rzad, kolumna
    free_fields = make_list_of_free_fields(board)
    list_length = len(free_fields)
    # randrange(n) losuje liczbe od 0 do n-1, wiec nadaje sie na indeks listy wolnych pol;
    # sposrod wszystkich wolnych pol, losowo wybierany jest indeks jednego z nich,
    # by postawic na nim znak 'X' symulujacy ruch komputera
    computer_move = randrange(list_length)
    # rozpakowywanie krotki (row, column) do zmiennych okreslajacych numer wiersza i kolumny na tablicy gry
    row, column = free_fields[computer_move]
    # umieszczenie znaku 'X' na wylosowanym polu - poprzez podanie rzedu i kolumny w ktorych ma byc
    board[row][column] = "X"


if __name__ == "__main__":
    # Przebieg gry

    # poczatkowa plansza: komputer zaczyna, wiec jego pierwszy znak "X" jest juz na srodku
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
            if not make_list_of_free_fields(game_board):
                # pokazanie zapelnionej planszy
                display_board(game_board)
                print("Jest remis. Zaden z graczy nie wygral.")
                # tak samo jak przy wygranej: break konczy for, flaga konczy while
                end_of_game = True
                break