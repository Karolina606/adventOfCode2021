# Pomocne zmienne globalne
line_counter = 0
count_ones = [0] * 12
count_zero = [0] * 12


def main():
    # Wyświetla wynik pierwszej lub drugiej części zadania / należy zamienić wywołanie funkcji
    print("Result: " + str(second_task()))


# Funkcja przeliczająca tablicę bitów na wartość dziesiętną
def binatodeci(binary):
    return sum(val * (2 ** idx) for idx, val in enumerate(reversed(binary)))


# Zad1
def first_task():
    # Należy policzyć iloraz gamma oraz epsilon
    # Współczynnik gamma to otrzymujemy poprzez wybranie z danych z raportu
    # najbardziej popularnego bitu na każdej pozycji (wsp. gamma ma tyle samo bitów co pojedynczy odczyt)
    # Dla współczynnika epsillon postępujemy analogiczne, lecz wybieramy najmnej popularny bit na każdej pozycji

    global line_counter
    global count_ones
    dataFile = open("data3.txt")
    gamma = [0] * 12
    epsilon = [0] * 12

    for line in dataFile:
        # Zlicz ile lini w raporcie
        line_counter += 1
        for i in range(12):
            # Jeśli na pozycji jest bit 1, to dodaj to tablicy liczącej jedynki
            if int(line[i]) == 1:
                count_ones[i] += 1
            # Jeśli na pozycji jest bit 0, to dodaj to tablicy liczącej zera
            elif int(line[i]) == 0:
                count_zero[i] += 1

    print(count_ones)
    for i in range(12):
        # Jeśli na danej pozycji jest więcej jedynek przypisz gammie na tej pozycji 1 a epsilonowi 0
        if count_ones[i] > line_counter / 2:
            gamma[i] = 1
            epsilon[i] = 0
        # W odwrotnym przypadku przypisz bity odwrotnie
        else:
            gamma[i] = 0
            epsilon[i] = 1

    print(gamma, epsilon)
    # Zwróć dziesiętne mnożenie obu współczynników
    return binatodeci(gamma) * binatodeci(epsilon)


# Zad2
def second_task():
    # Należy ustalić parametry tlenu i co2
    # Dla tlenu, sprawdzamy w raporcie każdą "kolumnę"/pozycję binarną i
    # jaki bit jest na niej najpopularnijeszy, następnie zostawiamy jedynie te odczyty,
    # które mają ten najpop. bit na tej pozycji (jeśli po równo, to wybieramy bit 1)
    # powtarzamy dopóki nie odrzucimy wszystkich odczytów poza jednym (to będzie parametr tlenu)

    # Dla co2, postępujemy analogicznie, wybieramy jednak za każdym razem niej popularny bit
    # w danej kolumnie, jeśli jest ich po równo to wybieramy 0

    dataFile = open("data3.txt")
    tab = []
    # Czytamy linie raportu do listy
    for line in dataFile:
        tab.append(line)

    # Wywołujemy funkcje znajdujące parametr tlenu i co2
    tab_oxy = find_oxygen(tab)[0].replace("\n", '')
    tab_co2 = find_co2(tab)[0].replace("\n", '')
    # print("hello " + tab_oxy + " hello " + tab_co2)

    # Zamieniamy otrzymane wartości na listę bitów
    oxy = [0] * 12
    co2 = [0] * 12
    for i in range(12):
        oxy[i] = int(tab_oxy[i])
        co2[i] = int(tab_co2[i])

    print(line_counter)
    print(str(binatodeci(oxy)) + ", " + str(binatodeci(co2)))
    # Zwracamy iloraz obu parametrów
    return binatodeci(oxy) * binatodeci(co2)


# Pomocnicza funkcja, licząca zera i jedynki w danym zbiorze odczytów
def count_one_and_zero(tab):
    global line_counter
    global count_ones
    global count_zero
    count_ones = [0] * 12
    count_zero = [0] * 12

    line_counter = 0
    for line in tab:
        line_counter += 1
        for i in range(12):
            if int(line[i]) == 1:
                count_ones[i] += 1
            elif int(line[i]) == 0:
                count_zero[i] += 1


def find_oxygen(tab):
    global line_counter
    global count_ones
    global count_zero
    new_tab = []

    # Przechodzimy przez wszystkie kolumny
    for i in range(12):
        # if count_ones[i] >= line_counter / 2:
        #     current_common_bit = 1
        # else:
        #     current_common_bit = 0

        # Liczymy ile zer i jedynek w obecnej liście
        count_one_and_zero(tab)

        # Jeśli na danej pozycji więcej jedynek lub po równo, to uznaj 1 za najpopularniejszy
        if count_ones[i] >= count_zero[i]:
            current_common_bit = 1
        # Jeśli odwrotnie to uznaj 0
        else:
            current_common_bit = 0

        # Przejdz przez całą listę odczytów, jeśli dany odczyt ma na danej pozycji, popularniejszy bit
        # zapisz go w nowej liście
        for line in tab:
            if int(line[i]) == current_common_bit:
                new_tab.append(line)

        print()
        print("Kolumna: " + str(i))
        print("Jedynek: " + str(count_ones[i]))
        print("Zer: " + str(count_zero[i]))
        print("Popularniejszy: " + str(current_common_bit))
        print("new_tab: " + str(new_tab))
        print("tab len: " + str(len(tab)))

        # Przypisz nową listę do starej
        tab = new_tab
        # wyczyść nową listę
        new_tab = []
        # Jeśli pozostał tylko jeden odczyt zakończ i zwróć listę
        if len(tab) == 1 and tab[0] is not None:
            return tab


def find_co2(tab):
    global line_counter
    global count_ones
    global count_zero
    new_tab = []

    for i in range(12):
        # if count_ones[i] < line_counter / 2:
        #     current_least_common_bit = 1
        # else:
        #     current_least_common_bit = 0

        # Liczymy ile zer i jedynek w obecnej liście
        count_one_and_zero(tab)

        # Jeśli na danej pozycji mniej jedynek, to uznaj 1 za mniej popularny
        if count_ones[i] < count_zero[i]:
            current_least_common_bit = 1
        # Jeśli odwrotnie to uznaj 0
        else:
            current_least_common_bit = 0

        # Przejdz przez całą listę odczytów, jeśli dany odczyt ma na danej pozycji, mniej popularniejszy bit
        # zapisz go w nowej liście
        for line in tab:
            if int(line[i]) == current_least_common_bit:
                new_tab.append(line)

        print()
        print("Kolumna: " + str(i))
        print("Jedynek: " + str(count_ones[i]))
        print("Zer: " + str(count_zero[i]))
        print("MniejPopularniejszy: " + str(current_least_common_bit))
        print("new_tab: " + str(new_tab))

        # Przypisz nową listę do starej
        tab = new_tab
        # wyczyść nową listę
        new_tab = []
        # Jeśli pozostał tylko jeden odczyt zakończ i zwróć listę
        print("tab len: " + str(len(tab)))
        if len(tab) == 1 and tab[0] is not None:
            return tab


if __name__ == '__main__':
    main()
