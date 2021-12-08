def main():
    # Wyświetla wynik pierwszej lub drugiej części zadania / należy zamienić wywołanie funkcji
    print("Result: " + str(second_task()))


# Zad1
def first_task():
    # Należy zasymulować rozmnażanie świetlików/rybek
    # Na początek dostajemy dane dotyczące pewnej ławicy, każda z ryb ma przyporządkowaną liczbę dni za jaką sie rozmnazy
    # Następnie liczba dni ustawiana jest na 6 i odliczanie zaczyna się od nowa
    # Nowe ryby mają początkowo 8 dni do nowego rozmnożenia
    # Ustalić ile będzie ryb po 80 dniach
    # Sposób "na chłopski rozum"

    dataFile = open("data6.txt")
    numbers = list(int(number) for number in dataFile.readline().split(','))
    days = 80

    while days > 0:
        for i in range(len(numbers)):
            numbers[i] = round(numbers[i] - 1, 0)
            if numbers[i] == -1:
                numbers.append(8)
                numbers[i] = 6

        print("Days left " + str(days))
        days -= 1

    return len(numbers)


# Zad2
def second_task():
    # Należy zasymulować rozmnażanie świetlików/rybek
    # Na początek dostajemy dane dotyczące pewnej ławicy, każda z ryb ma przyporządkowaną liczbę dni za jaką sie rozmnazy
    # Następnie liczba dni ustawiana jest na 6 i odliczanie zaczyna się od nowa
    # Nowe ryby mają początkowo 8 dni do nowego rozmnożenia
    # Ustalić ile będzie ryb po 256 dniach
    # Szybszy sposób

    dataFile = open("data6.txt")
    numbers = list(int(number) for number in dataFile.readline().split(','))
    days = 256
    days_to_spawn = [0] * 9

    for number in numbers:
        days_to_spawn[number] += 1

    for i in range(days):
        giving_new_fishes = days_to_spawn[0]
        days_to_spawn = days_to_spawn[1:] + [giving_new_fishes]
        days_to_spawn[6] += giving_new_fishes

    return sum(days_to_spawn)


if __name__ == '__main__':
    main()

