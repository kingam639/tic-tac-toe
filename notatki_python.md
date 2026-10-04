# Notatki z nauki Pythona — gra w kółko i krzyżyk

## Flagi i pętle — checklist pytań kontrolnych

Flaga to zwykła zmienna (najczęściej `True`/`False`), która "pamięta" coś, co wydarzyło
się w trakcie pętli, żeby można było to sprawdzić PO jej zakończeniu. Pętla sama w sobie
nic nie pamięta — gdy się skończy, wszystko co się w niej działo "znika", chyba że
zapisałaś to po drodze w jakiejś zmiennej.

Pytania kontrolne, które warto sobie zadawać za każdym razem:

- **Kiedy w ogóle potrzebna jest flaga?** Gdy chcę wiedzieć, co się działo w CAŁEJ pętli,
  dopiero PO jej zakończeniu — a nie w trakcie.
- **Jaka wartość startowa?** Zwykle najbardziej optymistyczne/neutralne założenie, od
  którego zaczynam, zanim cokolwiek sprawdzę. W `victory_for` to było "zakładam, że ta
  kombinacja jest zwycięska" → `True`.
- **Gdzie zmienić flagę?** Dokładnie w tym miejscu w pętli, gdzie łamie się założenie
  startowe. W `victory_for`: gdy pole NIE pasuje do szukanego znaku.
- **Gdzie reset flagi?** Na początku każdej nowej "porcji" danych, zanim zacznę ją
  sprawdzać od nowa — inaczej flaga "pamięta" wynik z poprzedniej porcji. W `victory_for`
  flaga resetowała się na początku każdej nowej kombinacji (każdego obrotu zewnętrznej
  pętli `for combination in winning_fields`).
- **Gdzie sprawdzić flagę?** ZAWSZE po pętli, która ją ustawia, czyli POZA jej wcięciem.
  Błąd, który popełniłaś na początku: `is_equal = True` na końcu `for combination`, w tym
  samym wcięciu co `if is_equal`, zamiast po całej pętli — przez to flaga resetowała się,
  zanim zdążyłaś ją sprawdzić.

## `for...else` — druga droga do tego samego celu

`else` przy pętli `for` wykonuje się TYLKO wtedy, gdy pętla zakończyła się BEZ `break`.
Jeśli `break` się wykonał (bo coś znaleziono / coś nie pasowało), `else` się pomija.

Typowy sygnał, że to pasuje: "szukam czegoś w pętli i jeśli NIE znajdę (albo nic jej nie
przerwało), zrobię coś innego po jej zakończeniu".

Przykład z `enter_move` (Twoja pierwsza wersja tego mechanizmu):
```python
for row in board:
    if user_move in row:
        ...
        break
else:
    print("To pole jest juz zajete. Sprobuj ponownie.")
```

Przykład z `victory_for` (finalna wersja, zamiast flagi):
```python
for field in combination:
    if field != sign:
        break
else:
    return "Wygrałeś!"
```
To robi dokładnie to samo, co wcześniejsza wersja z flagą `is_equal`, tylko krócej.
Różnica: wersja z `break` zatrzymuje się od razu, gdy znajdzie niepasujące pole (nie
sprawdza reszty), a wersja z flagą leci przez wszystkie trzy pola zawsze. Przy trzech
elementach ta różnica w wydajności jest nieistotna — to kwestia stylu i czytelności,
nie poprawności. Obie wersje są tak samo dobre.

## Zmienne globalne vs argumenty funkcji

Problem pojawił się przy `user_moves_examples(user_moves_board)`, gdzie funkcja
odwoływała się do `used_move` zdefiniowanej GDZIEŚ w pliku, poza funkcją — edytor
podkreślał to na czerwono, bo z punktu widzenia samej funkcji nie wiadomo skąd ta
zmienna się bierze.

Pytania kontrolne, czy coś powinno być argumentem (prawie zawsze TAK), czy zmienną
globalną:
- Czy funkcja to CZYTA lub ZMIENIA? → powinno być argumentem.
- Czy chcę móc łatwo testować tę funkcję z różnymi danymi wejściowymi? → argument
  (zmienna globalna "przykleja" funkcję na sztywno do jednego stanu, nie da się
  podstawić innego bez zmiany kodu globalnego).
- Czy ta wartość zmienia się w czasie działania programu? → argument. Zmienne globalne,
  które się zmieniają w trakcie działania programu, prowadzą do trudnych do namierzenia
  błędów, bo różne funkcje mogą je modyfikować "po cichu", bez śladu w swojej sygnaturze.

Prosta reguła: zmienne globalne trzymać tylko dla rzeczy naprawdę STAŁYCH w całym
programie. Finalna wersja: `def user_moves_examples(user_moves_board, used_move):` —
obie listy jawnie jako argumenty.

## `assert` — testowanie

### Jak to działa
- `assert warunek` → jeśli warunek jest prawdziwy: nic się nie dzieje, cisza, program
  idzie dalej. Jeśli fałszywy: program zatrzymuje się z `AssertionError` i pokazuje
  numer linijki.
- `assert warunek, "komunikat"` → komunikat pokazuje się TYLKO przy błędzie, w tekście
  wyjątku. Pomaga od razu wiedzieć, który test zawiódł i dlaczego.
- To skrót od: `if not warunek: raise AssertionError("komunikat")`.

### Zasada testu
Po lewej stronie `==` jest to, co faktycznie zwróciła funkcja. Po prawej — to, czego się
spodziewam, ustalone PRZED uruchomieniem kodu, na podstawie znajomości zasad/logiki
(np. zasad gry w kółko i krzyżyk), a NIE na podstawie tego, co funkcja akurat zwróciła
przy pierwszym uruchomieniu. Przykład:
```python
vict_board_1 = [["X", "X", "X"], ["O", "X", "O"], ["O", 8, 9]]
assert victory_for(vict_board_1, "X") == True, "X ma górny rząd, powinno być True"
assert victory_for(vict_board_1, "O") == False, "O nie wygrał, powinno być False"
```

### Pułapki
- NIE: `assert (warunek, "komunikat")` — to para w nawiasie (krotka), a niepusta krotka
  jest w Pythonie zawsze uznawana za "prawdziwą", więc taki `assert` NIGDY się nie
  wywali, nawet gdy warunek jest fałszywy. Python nawet o tym ostrzega, ale łatwo to
  przeoczyć. Przecinek ma być POZA nawiasem.
- Sprawdzian, czy test w ogóle coś testuje: zmień na chwilę oczekiwany wynik na błędny.
  Test MUSI się wtedy wywalić. Jeśli nie, znaczy że niczego nie sprawdzał.
- `assert` zatrzymuje się na PIERWSZYM nieudanym teście — kolejne testy w tym samym
  pliku się wtedy nie wykonają. To ograniczenie, dlatego docelowo warto poznać
  `unittest` albo `pytest`, które uruchamiają wszystkie testy naraz i pokazują zbiorczo,
  które zawiodły.
- NIE używać `assert` do walidacji danych od prawdziwego użytkownika w działającym
  programie — uruchomienie z flagą `python -O` wyłącza WSZYSTKIE asserty w programie.
  Do walidacji danych służy `if`/`try-except`, tak jak w `enter_move`.

### Co właściwie testować w funkcji — pytanie kontrolne
*W jakich różnych sytuacjach ta funkcja może się znaleźć i co w każdej z nich powinna
zwrócić?*

Dla `victory_for` wyszły z tego konkretne scenariusze:
- wygrana osobno w każdej z 8 możliwych linii (3 rzędy, 3 kolumny, 2 przekątne) — bo
  `winning_fields` jest wpisane ręcznie, więc literówka w jednej linii (np.
  `board[1][2]` zamiast `board[1][1]`) wyjdzie TYLKO przy teście akurat tej linii;
- zwycięzca i jego przeciwnik sprawdzani na tej samej planszy (dwa asserty na planszę);
- "prawie wygrana" — linia, w której brakuje jednego znaku — pilnuje granicy
  porównania `!=` / `==` (czy funkcja nie uznaje przez pomyłkę niepełnej linii za
  wygraną);
- pełna plansza bez zwycięzcy (remis);
- plansza W TRAKCIE gry, z samymi liczbami zamiast samych `X`/`O` — pilnuje, czy
  funkcja przypadkiem nie myli pola z liczbą (np. `2`, `7`) ze znakiem gracza.

Ten sam sposób myślenia (wypisać sobie scenariusze, zanim napisze się choć jeden
`assert`) stosuje się do każdej kolejnej testowanej funkcji.

## `if __name__ == "__main__":`

- `__name__` to specjalna zmienna, którą Python SAM, automatycznie ustawia w KAŻDYM
  pliku `.py` — nie trzeba jej nigdzie definiować.
- Gdy plik jest uruchamiany BEZPOŚREDNIO (np. "Run" w PyCharmie na `tic_tac_toe.py`),
  Python ustawia w nim `__name__ = "__main__"`.
- Gdy ten sam plik jest IMPORTOWANY z innego pliku (np. `import tic_tac_toe` albo
  `from tic_tac_toe import victory_for` w pliku testowym), Python ustawia w nim
  `__name__` na nazwę tego pliku (czyli `"tic_tac_toe"`), a NIE `"__main__"`.

Dzięki temu w pliku z grą (`tic_tac_toe.py`) główną pętlę gry (tworzenie planszy,
słownik graczy, `while not end_of_game`) owija się w:
```python
if __name__ == "__main__":
    # tu wszystko, co ma się wykonać TYLKO przy bezpośrednim uruchomieniu tego pliku
```
Dzięki temu gra NIE uruchamia się przypadkiem, gdy plik testowy robi
`from tic_tac_toe import victory_for` — Python wtedy wczytuje definicje funkcji, ale
pomija to, co jest wewnątrz `if __name__ == "__main__":`.

Import konkretnych funkcji wygląda tak:
```python
from tic_tac_toe import victory_for, make_list_of_free_fields, enter_move
```
Dzięki temu w pliku testowym wywołuje się je bezpośrednio (`victory_for(...)`), bez
przedrostka `tic_tac_toe.` z przodu.

Plik testowy (`test_tic_tac_toe.py`) nie musi mieć własnego `if __name__`, JEŻELI nikt
go nie importuje — to zabezpieczenie jest tylko dobrą praktyką na przyszłość, nie
koniecznością.

## Dependency injection — alternatywa dla `mock` w testach

Problem: `enter_move` normalnie czeka na `input()`, czyli na kogoś piszącego na
klawiaturze. Żeby to przetestować bez siedzenia i wklepywania wartości ręcznie, są
dwie drogi:
1. `unittest.mock` z dekoratorem `@patch` — "podmienia" `input` z zewnątrz (bardziej
   zaawansowane, zostawione na później).
2. **Dependency injection** (dosłownie: "wstrzykiwanie zależności") — dodanie do
   funkcji dodatkowego parametru z wartością domyślną `None`, który pozwala podać
   wartość "z góry", zamiast czekać na input:

```python
def enter_move(board, user_move=None):
    free_field = True
    while free_field:
        try:
            if user_move is None:
                user_move = input("Wprowadź swój ruch: ")
            user_move = int(user_move)
        except ValueError:
            print("Nie wpisales liczby. Sprobuj ponownie.")
        else:
            # reszta logiki (zakres, zajętość pola) bez zmian
            ...
```

Dzięki `user_move=None` jako wartości domyślnej funkcja działa normalnie w grze
(nikt nic nie podaje → pyta o input), a w testach podaje się wartość wprost:
`enter_move(board, "5")` — bez czekania na klawiaturę, bez `mock`, bez dekoratorów.

**Ważna pułapka, na którą wpadłyśmy:** `input()` ZAWSZE zwraca `string`, nawet jeśli
użytkownik wpisze liczbę. Dlatego w testach trzeba podawać wartości jako string
(`"3.5"`, `"5"`, `"c"`), a NIE jako gotowe typy Pythona (`3.5`, `5`). Różnica:
- `int(3.5)` (prawdziwy float) → po cichu OBCINA do `3`, nie wywala błędu.
- `int("3.5")` (string) → rzuca `ValueError`, tak samo jak błędny input z klawiatury.

Gdyby testować funkcję floatem zamiast stringiem `"3.5"`, dostałoby się fałszywie
pozytywny wynik — w prawdziwej grze taka sytuacja (float jako argument) nigdy się nie
zdarzy, bo `input()` nic innego niż string nie zwraca.

**Etapy dojścia do tej wersji (żeby pamiętać, co nie zadziałało i dlaczego):**
1. Pierwsza próba: `if isinstance(user_move, int): return user_move` — błąd:
   `return` urywa całą resztę funkcji (sprawdzenie zakresu, zajętości pola), więc
   funkcja nic nie robiła, tylko oddawała tę samą wartość z powrotem.
2. Druga próba: osobne `int(user_move)` w gałęzi `else`, ale bez przypisania wyniku
   z powrotem do `user_move` — wynik się liczył i "ginął", zmienna `user_move`
   zostawała niezmieniona (nadal string albo cokolwiek, co przyszło).
3. Finalna wersja: jedna wspólna linijka `user_move = int(user_move)` dla OBU ścieżek
   (i tej z `input()`, i tej z argumentu) — prostsze, bez duplikacji, i obie ścieżki
   przechodzą przez tę samą walidację w `try/except`.

## `user_moves_examples` — jak działa i dwie wersje tej samej idei

Finalna funkcja:
```python
def user_moves_examples(user_moves_board, used_move):
    for move in user_moves_board:
        if move not in used_move:
            used_move.append(move)
            return move
```
Działa jak "kolejka": dostaje listę przykładowych ruchów (`user_moves_board`) i listę
ruchów już wykorzystanych (`used_move`). Za każdym wywołaniem szuka pierwszego ruchu,
którego jeszcze nie było w `used_move`, dopisuje go tam i go zwraca. Lista
`user_moves_board` zostaje NIETKNIĘTA, zmienia się tylko `used_move`. Jeśli WSZYSTKIE
ruchy z `user_moves_board` są już w `used_move`, pętla `for` przechodzi od początku do
końca bez trafienia w `if`, funkcja kończy się bez jawnego `return` → zwraca `None`
(ogólna zasada Pythona: brak `return` na końcu = `None`).

**Alternatywne podejście, które rozważałyśmy:** `move = user_moves_board.pop(0)` —
krócej, bez osobnej listy `used_move`, ale z dwiema różnicami:
- `.pop()` modyfikuje listę IN PLACE — `user_moves_board` skurczyłaby się z każdym
  wywołaniem, więc nie dałoby się jej użyć ponownie w innym teście bez odtworzenia.
- `.pop(0)` nie radzi sobie z duplikatami tak samo — przy liście `[1, 3, 1, 4]`
  zwróciłoby `1` dwa razy, podczas gdy wersja z `used_move` pominęłaby powtórzoną
  jedynkę.
Obie wersje są poprawnym kodem, różnią się zachowaniem na brzegach.

**Błąd, który się pojawił przy testowaniu zakończenia pętli:** warunek
`if user_moves_board == used_move: free_moves = False` nie działa, bo te listy
praktycznie NIGDY nie staną się sobie równe (np. `"c"` i `-7` nigdy nie trafią do
`used_move`, bo... no właśnie, to już osobna sprawa od samej `user_moves_examples` —
`used_move` rośnie o KAŻDY nieużyty jeszcze ruch, niezależnie od tego, czy jest on
"poprawny" w sensie zasad gry). Właściwy sposób sprawdzenia końca: sprawdzić, czy
`user_moves_examples` zwróciła `None`.

## Docstring — co powinien zawierać

Trzy pytania, na które docstring ma odpowiadać:
1. Co funkcja robi (ogólnie, jednym-dwoma zdaniami)?
2. Co dostaje jako parametry i co one oznaczają?
3. Co zwraca — WE WSZYSTKICH przypadkach, łącznie z przypadkami "pustymi"/brzegowymi
   (np. że zwraca `None`, gdy nic nie zostało znalezione / lista się wyczerpała).

Sprawdzian na dobry docstring: przeczytać go, UDAJĄC że nigdy się nie widziało kodu tej
funkcji, i sprawdzić, czy dałoby się na jego podstawie poprawnie tę funkcję wywołać.

Przykład dobrego docstringa (finalna wersja dla `user_moves_examples`):
> "Funkcja przyjmuje jako argumenty listę z przykładowymi ruchami użytkownika do
> przetestowania (user_moves_board) i listę z ruchami użytkownika, które już zostały
> przetestowane (used_move). Sprawdza czy ruch z listy user_moves_board jest już na
> liście used_move, co oznacza że został już przetestowany; jeśli nie jest, zwraca ten
> ruch do zasymulowania kolejnego ruchu użytkownika i dodaje go do listy ruchów już
> przetestowanych (used_move). Funkcja zwraca None, gdy wszystkie ruchy zostały już
> przetestowane."

Pamiętać: funkcja BEZ jawnego `return` na końcu zwraca `None` — to ogólna, wbudowana
zasada Pythona, nie coś specyficznego dla jednej funkcji.

## Komentarze — jak pisać dobre

1. **Kod mówi CO, komentarz mówi DLACZEGO.** Sprawdzian: skreśl komentarz w myślach —
   jeśli nic nie ginie (bo kod sam się tłumaczy), komentarz był zbędny.
2. **Pisz dla kogoś, kto zna Pythona, ale nie zna Twojego projektu** — czyli dla siebie
   za 3 tygodnie. Nie tłumacz mechanizmów samego Pythona (czym jest `for`, co robi
   `.index()`) — chyba że to jeszcze etap utrwalania wiedzy, wtedy to ma sens, ale
   docelowo tłumacz DECYZJE (dlaczego ta flaga, dlaczego ten słownik, dlaczego ta
   kolejność).
3. **Komentuj bloki i niejasne miejsca, nie każdą linijkę.** Jeden komentarz nad kilkoma
   liniami, które razem robią jedną rzecz, lepszy niż pięć komentarzy jednolinijkowych.
4. **Dobre nazwy zmiennych zastępują część komentarzy** (np. `is_equal`, `free_fields`
   tłumaczą się same).
5. **Docstring ≠ komentarze w środku.** Docstring to umowa funkcji z zewnątrz (co robi,
   co dostaje, co zwraca). Komentarze w środku tłumaczą JAK i DLACZEGO TAK, a nie
   inaczej.
6. **Nie trzymać w komentarzach swoich rozmyślań ani starych wersji kodu** — od tego
   jest teraz Git (historia commitów). Niedokończone rzeczy oznaczać `# TODO: ...`.
7. **Krótko** — jedna myśl na jedną linijkę komentarza.

## Git — podstawowy przepływ

**Pierwsze połączenie repo lokalnego ze zdalnym (tylko raz, na początku projektu):**
```
git init
git add plik.py
git commit -m "opis"
git remote add origin <adres-repo-z-githuba>
git branch -M main
git push -u origin main
```

**Każda kolejna zmiana:**
```
git add plik.py
git commit -m "krótki opis DLACZEGO, nie tylko CO"
git push
```
(bez `-u origin main` — to trzeba było tylko raz, na starcie)

`git status` — pokazuje, co się zmieniło / jakie pliki są nowe, niewrzucone.

**Logowanie:** GitHub od pewnego czasu NIE przyjmuje zwykłego hasła przy `git push` —
trzeba Personal Access Token: GitHub.com → awatar → Settings → Developer settings →
Personal access tokens → Generate new token (classic), z uprawnieniem `repo`. Token
pokazuje się TYLKO RAZ przy tworzeniu — trzeba go od razu skopiować i zapisać. Przy
pytaniu o hasło w terminalu wkleja się TEN token, nie zwykłe hasło do konta.

`git config --global credential.helper osxkeychain` (macOS) zapamiętuje token w
Keychain, żeby nie wklejać go przy każdym kolejnym `push`.

**Zasada bezpieczeństwa:** token to jak hasło — nigdy nie wklejać go w czacie ani
nigdzie indziej poza terminalem/Keychain.

## Status projektu (gra w kółko i krzyżyk) — checklist

**Gotowe i działające:**
- `display_board` — wypisuje planszę.
- `enter_move` — pobiera i waliduje ruch użytkownika; ma teraz parametr
  `user_move=None` do testowania bez `input()`.
- `make_list_of_free_fields` — zwraca listę wolnych pól jako krotki `(wiersz, kolumna)`.
- `victory_for` — sprawdza wygraną, finalna wersja na `for...else`, zwraca `True`/`False`.
  W pełni przetestowana asercjami w `test_tic_tac_toe.py` (8 linii wygranej + remisy +
  plansza w trakcie gry).
- `draw_move` — losuje ruch komputera spośród wolnych pól (przez `make_list_of_free_fields`
  + `randrange` na indeksie listy, bez ryzyka nieskończonej pętli).
- Główna pętla gry — w `tic_tac_toe.py`, owinięta w `if __name__ == "__main__":`,
  używa słownika `players_moves = {"O": enter_move, "X": draw_move}` i pętli
  `for key, value in players_moves.items()` do naprzemiennej obsługi obu graczy.
- `user_moves_examples` — generator przykładowych ruchów użytkownika do testów.

**W trakcie:**
- Dokończenie testów `enter_move` z wykorzystaniem `user_move=None` i
  `user_moves_examples` — trzeba rozpisać osobne, KRÓTKIE listy ruchów na scenariusz
  (zły typ, poza zakresem, zajęte pole, poprawny ruch na końcu listy), bo
  `enter_move` kończy się po PIERWSZYM poprawnym ruchu i nie zobaczy reszty listy.

**Do zrobienia:**
- Testy `make_list_of_free_fields` (pusta plansza / w połowie zapełniona / pełna).
- Rozważyć przejście z `assert` na `unittest` albo `pytest` (uruchamiają wszystkie
  testy naraz, nie zatrzymują się na pierwszym błędzie).
- Uporządkować plik `tic_tac_toe.py` pod kątem końcowych komentarzy i ewentualnych
  pozostałości po starych wersjach kodu (można je bezpiecznie usuwać, bo historia
  i tak zostaje w Git).