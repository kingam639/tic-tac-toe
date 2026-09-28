**Testy: co zrobić, po kolei**

1. **Wybierz, co testujesz.** Symulacji ruchów potrzebuje tylko `enter_move`, bo tylko ona używa `input()`. `victory_for` i `make_list_of_free_fields` możesz testować zwykłym `assert` na przygotowanych planszach, bez żadnej symulacji. Zacznij od nich, bo są najprostsze, a `enter_move` zostaw na koniec.
2. **Zanim napiszesz kod, wypisz scenariusze na kartce.** Do każdego dopisz, jak ma wyglądać plansza (albo co ma zostać wypisane) po jego zakończeniu. Dla `enter_move` zastanów się, jakie rodzaje złych danych możesz dostać i czy Twoja lista `[1, 3, "c", 12, -7, 4, 8]` pokrywa je wszystkie. Sprawdź też, czy jest w niej scenariusz „pole jest już zajęte". Na starcie zajęte jest tylko środkowe pole.
3. **Zastanów się, jak `enter_move` ma dostawać wartości z Twojej funkcji zamiast z klawiatury.** Wróć do naszej rozmowy o nadpisywaniu `input`. Zastanów się też, co się stanie, gdy `user_moves_examples` wyczerpie listę i nie zwróci niczego.
4. **Zastanów się, co się stanie, gdy plik z testami zaimportuje plik z grą.** W pliku z grą masz teraz główną pętlę na najwyższym poziomie. Sprawdź, co Python robi przy `import` z takim kodem, i poszukaj, do czego służy `if __name__ == "__main__":`.
5. **Pisz po jednym teście naraz.** Napisz jeden, uruchom go i upewnij się, że przechodzi, a dopiero potem dodawaj następne. Żeby zobaczyć, że test naprawdę coś sprawdza, zepsuj na chwilę oczekiwany wynik i zobacz, czy test to wykryje.
6. **Po każdym teście wywołaj `assert` na stanie planszy**, a nie tylko sprawdzaj, czy funkcja się nie wysypała.

Zacznij od punktów 1 i 2 i pokaż mi swoją listę scenariuszy. Chętnie powiem, czy czegoś w niej brakuje.