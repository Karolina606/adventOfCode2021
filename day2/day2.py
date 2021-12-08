def main():
    # Wyświetla wynik pierwszej lub drugiej części zadania / należy zamienić wywołanie funkcji
    print("Result: " + str(second_task()))


# Zad1
def first_task():
    # Należy policzyć horyzontalną i głębokościową pozycję okrętu oraz pomnożyć je przez siebie
    # Obliczamy to według podanej reguły

    # Pobiera z pliku z danymi kolejne linie
    dataFile = open("data2.txt")
    # Kooordynat horyzontalny
    horizontal = 0
    # Kooordynat głębokościowy
    depth = 0
    for line in dataFile:
        line_tab = line.split(" ")
        print(line_tab)
        # Jeśli okręt płynie do przodu, to dodaj przesunięcie do koordynatu horyzontalnego
        if line_tab[0] == "forward":
            horizontal += int(line_tab[1])
        # Jeśli okręt płynie w dół, to dodaj przesunięcie do koordynatu głębokości
        elif line_tab[0] == "down":
            depth += int(line_tab[1])
        # Jeśli okręt płynie do góry, to odejmij przesunięcie od koordynatu głębokości
        elif line_tab[0] == "up":
            depth -= int(line_tab[1])

    return horizontal, depth, horizontal * depth


# Zad2
def second_task():
    # Należy policzyć horyzontalną i głębokościową pozycję okrętu oraz pomnożyć je przez siebie
    # Obliczamy to według podanej reguły

    dataFile = open("data2.txt")
    # Kooordynat horyzontalny
    horizontal = 0
    # Kooordynat głębokościowy
    depth = 0
    # Cel
    aim = 0
    for line in dataFile:
        line_tab = line.split(" ")
        print(line_tab)
        # Jeśli okręt płynie do przodu, to dodaj przesunięcie do koordynatu horyzontalnego
        # Oraz jego iloczyn z aim do koordynatu głębokości
        if line_tab[0] == "forward":
            horizontal += int(line_tab[1])
            depth += int(line_tab[1]) * aim
        # Jeśli okręt płynie w dół, to dodaj przesunięcie do aim
        elif line_tab[0] == "down":
            aim += int(line_tab[1])
        # Jeśli okręt płynie do góry, to odejmij przesunięcie od aim
        elif line_tab[0] == "up":
            aim -= int(line_tab[1])

    return horizontal, depth, horizontal * depth


if __name__ == '__main__':
    main()
