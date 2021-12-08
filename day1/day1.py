def main():
    # Wyświetla wynik pierwszej lub drugiej części zadania / należy zamienić wywołanie funkcji
    print("Result: " + str(second_task()))


# Zad1
def first_task():
    # Ma zliczyć powiększenie głębokości okrętu

    # Pobiera z pliku z danymi kolejne linie
    dataFile = open("data.txt")
    # Zapamientuje liczbę z poprzedniej linii oraz nowy bit
    previous_number = 0
    number = 0
    counter = 0
    for line in dataFile:
        number = int(line)
        print(number)
        # Jeśli poprzednia liczba jest zerem, nie robi nic
        if previous_number == 0:
            ...
        # Jeśli poprzednia liczba jest mniejsza od tej z aktualnej linii to zwiększ licznik o jeden
        elif previous_number < number:
            counter += 1
        # Zapisz aktualną liczbę jako poprzednią
        previous_number = number

    # Zwróć licznik
    return counter


# Zad2
def second_task():
    # Ma zliczyć powiększenie głębokości okrętu, licząc po trzy odczyty jako grupa

    # Pobiera z pliku z danymi kolejne linie
    dataFile = open("data.txt")
    # Licznik, który będzie zliczał
    counter = 0

    # Lista odczytów
    numbers = []
    for line in dataFile:
        numbers.append(int(line))

    for i in range(len(numbers)):
        # Stwórz pierwszą 3-elementową grupę odczytów
        first_group = numbers[i: i+3]
        # Stwórz drugą 3-elementową grupę odczytów
        second_group = numbers[i+1: i+4]
        print(first_group)
        print(second_group)

        # Jeśli Grupy odczytów przestaną być 3-elementowe
        if len(first_group) == 3 and len(first_group) == 3:
            # Jeśli druga suma grupy odczytów jest większa (głębokość rosła) zwiększ licznik
            if sum(first_group) < sum(second_group):
                counter += 1
                print("counted")
        else:
            break

        print()

    # Zwróć licznik
    return counter

if __name__ == '__main__':
    main()
