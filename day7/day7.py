def main():
    # Wyświetla wynik pierwszej lub drugiej części zadania / należy zamienić wywołanie funkcji
    print("Result: " + str(second_task()))


# Zad1
def first_task():
    # Karby płyną własnymi łódkami podwodnymi na pomoc
    # Przemieszczają się tylko horyzontalnie, aby wykonać pomocniczy strzał, musza być w tym samym miejscu
    # Każdy ruch do współrzędnej o 1 większej wynosi 1 jednostkę paliwa
    # Do jakiej pozycji powinny udać się kraby, aby zużyć jak najmniej paliwa

    dataFile = open("data7.txt")
    # Pobranie początkowych krabich pozycji
    crabs_positions = list(int(number) for number in dataFile.readline().split(','))
    # Największa pozycja
    max_position = max(crabs_positions)
    # Najniższa pozycja
    min_position = min(crabs_positions)

    # Najlepsze aktualne parametry
    min_fuel_usage = 10000000
    wanted_position = 0

    # Przechodzimy po możliwych pozycjach
    for i in range(min_position, max_position + 1):
        # Tablica zużycia paliwa dala każdego kraba, aby dostać się na ta pozycję
        # zużyte paliwo to różnica pomiędzy pozycją startową, a tą aktualnie rozważaną
        current_fuel_usage_tab = [abs(x - i) for x in crabs_positions]

        # Jeśli ta pozycja jest lepsza od aktualnej to ją zapisz
        if sum(current_fuel_usage_tab) < min_fuel_usage:
            min_fuel_usage = sum(current_fuel_usage_tab)
            wanted_position = i

    return min_fuel_usage


# Zad2
def second_task():
    # Karby płyną własnymi łódkami podwodnymi na pomoc
    # Przemieszczają się tylko horyzontalnie, aby wykonać pomocniczy strzał, musza być w tym samym miejscu
    # Pierwszy ruch do współrzędnej o 1 większej wynosi 1 jednostkę paliwa, każdy koleny o jeden więcej
    # Do jakiej pozycji powinny udać się kraby, aby zużyć jak najmniej paliwa

    dataFile = open("data7.txt")
    # Pobranie początkowych krabich pozycji
    crabs_positions = list(int(number) for number in dataFile.readline().split(','))
    # Największa pozycja
    max_position = max(crabs_positions)
    # Najniższa pozycja
    min_position = min(crabs_positions)

    # Najlepsze aktualne parametry
    min_fuel_usage = 1000000000000000
    wanted_position = 0

    # Przechodzimy po możliwych pozycjach
    for i in range(min_position, max_position + 1):
        # Tablica zużycia paliwa dala każdego kraba, aby dostać się na ta pozycję
        # zużyte paliwo to różnica suma wartości wykonanych kroktów na każdym etapie
        # zrobił 3 kroki: [1, 2, 3] -> zużyte paliwo 1 + 2 + 3 = 6
        current_fuel_usage_tab = [sum(list(range(abs(x - i)+1))) for x in crabs_positions]

        # Jeśli ta pozycja jest lepsza od aktualnej to ją zapisz
        if sum(current_fuel_usage_tab) < min_fuel_usage:
            min_fuel_usage = sum(current_fuel_usage_tab)
            wanted_position = i

    return min_fuel_usage


if __name__ == '__main__':
    main()

