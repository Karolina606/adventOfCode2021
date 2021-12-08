
def main():
    # Wyświetla wynik pierwszej lub drugiej części zadania / należy zamienić wywołanie funkcji
    print("Result: " + str(second_task()))


# Zad1
def first_task():
    # Należy ustalić, na podstawie współrzędnych początków i końców linii, ile z będzie punktów na mapie,
    # w których nakłądać sie będą na siebie dwie linie bądź więcej.
    # Bierzemy pod uwagę tylko linie pionowe lub poziome

    dataFile = open("data5.txt")
    numbers = 1000
    # Mapa na której zapisywane będą linie
    map = [[0 for x in range(numbers)] for y in range(numbers)]
    ends = []
    first_end_of_line = []
    second_end_of_line = []
    # Licznik nakłądania się linii
    count = 0

    for line in dataFile:
        # Rozdzielneie współrzędnych końców linii
        ends = line.split('->')
        first_end_of_line = ends[0].split(',')
        second_end_of_line = ends[1].split(',')
        first_end_of_line = [int(i) for i in first_end_of_line]
        second_end_of_line = [int(i) for i in second_end_of_line]

        # Sprawdza czy dane współrzędne tworzą linie horyzontalne lub wertykalne
        if first_end_of_line[0] == second_end_of_line[0] or first_end_of_line[1] == second_end_of_line[1]:
            # Jeśli tak to ustal początku zakresów x i y, dla punktów na linii
            first_start = min(first_end_of_line[0], second_end_of_line[0])
            second_start = max(first_end_of_line[0], second_end_of_line[0])
            first_end = min(first_end_of_line[1], second_end_of_line[1])
            second_end = max(first_end_of_line[1], second_end_of_line[1])

            # Przejdz przez zakres wyznaczonych składowych x i y dla współrzędnych linii
            for j in range(first_start, second_start + 1):
                for i in range(first_end, second_end + 1):
                    # Zaznacz na mapie o jeden punkt więcej w tym miejscu
                    map[i][j] += 1
                    # Jeśli są już dwa punkty w tym miejscu, wlicz je do licznika
                    if map[i][j] == 2:
                        count += 1

            print()
            print("First: " + str(first_end_of_line))
            print("Second: " + str(second_end_of_line))
    for row in map:
        print(row)

    # Zwracamy ilość punktów z nakładającymi się liniami
    return count


# Zad2
def second_task():
    # Należy ustalić, na podstawie współrzędnych początków i końców linii, ile z będzie punktów na mapie,
    # w których nakłądać sie będą na siebie dwie linie bądź więcej.
    # Bierzemy pod uwagę linie pionowe, poziome oraz diagonalne

    dataFile = open("data5.txt")
    numbers = 1000
    # Mapa na której zapisywane będą linie
    map = [[0 for x in range(numbers)] for y in range(numbers)]
    ends = []
    first_end_of_line = []
    second_end_of_line = []
    count = 0

    for line in dataFile:
        # Rozdzielneie współrzędnych końców linii
        ends = line.split('->')
        first_end_of_line = ends[0].split(',')
        second_end_of_line = ends[1].split(',')
        first_end_of_line = [int(i) for i in first_end_of_line]
        second_end_of_line = [int(i) for i in second_end_of_line]

        # Jeśli współrzędne wskazują na linie położoną pod kątem 45 stopni
        if abs(first_end_of_line[0]-second_end_of_line[0]) == abs(first_end_of_line[1]-second_end_of_line[1]):
            range_x = [0]
            range_y = [0]

            # Ustalamy zakres x i y dla punktów leżących na tej linii.
            # W zależńości od tego, od którego x i y zaczniemy należy wygenerować zakres odwrotny.
            if first_end_of_line[0] < second_end_of_line[0] and first_end_of_line[1] < second_end_of_line[1]:
                range_y = list(range(first_end_of_line[0], second_end_of_line[0]+1))
                range_x = list(range(first_end_of_line[1], second_end_of_line[1]+1))
            elif first_end_of_line[0] > second_end_of_line[0] and first_end_of_line[1] < second_end_of_line[1]:
                range_y = list(range(second_end_of_line[0], first_end_of_line[0]+1))
                range_x = list(range(first_end_of_line[1], second_end_of_line[1]+1))
                range_y.reverse()
            elif first_end_of_line[0] > second_end_of_line[0] and first_end_of_line[1] > second_end_of_line[1]:
                range_y = list(range(second_end_of_line[0], first_end_of_line[0]+1))
                range_x = list(range(second_end_of_line[1], first_end_of_line[1]+1))
                range_x.reverse()
                range_y.reverse()
            elif first_end_of_line[0] < second_end_of_line[0] and first_end_of_line[1] > second_end_of_line[1]:
                range_y = list(range(first_end_of_line[0], second_end_of_line[0] + 1))
                range_x = list(range(second_end_of_line[1], first_end_of_line[1]+1))
                range_x.reverse()

            print()
            for i in range(len(range_x)):
                map[range_x[i]][range_y[i]] += 1
                if map[range_x[i]][range_y[i]] == 2:
                    count += 1

        # Jeśli linia nie leży pod kątem 45 stopni
        else:
            # Sprawdzamy czy linia jest pionowa lub pozioma
            # Reszra analogicznie jak dla zadania pierwszego
            if first_end_of_line[0] == second_end_of_line[0] or first_end_of_line[1] == second_end_of_line[1]:
                first_start = min(first_end_of_line[0], second_end_of_line[0])
                second_start = max(first_end_of_line[0], second_end_of_line[0])
                first_end = min(first_end_of_line[1], second_end_of_line[1])
                second_end = max(first_end_of_line[1], second_end_of_line[1])

                for j in range(first_start, second_start + 1):
                    for i in range(first_end, second_end + 1):
                        map[i][j] += 1
                        if map[i][j] == 2:
                            count += 1

    for row in map:
        print(row)

    # Zwracamy ilość punktów z nakładającymi się liniami
    return count


if __name__ == '__main__':
    main()

