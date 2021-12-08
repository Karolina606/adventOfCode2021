def main():
    # Wyświetla wynik pierwszej lub drugiej części zadania / należy zamienić wywołanie funkcji
    print("Result: " + str(second_task
    ()))


class bingo_board:
    # Klasa reprezentująca planszę do gry w bingo 5 x 5

    def __init__(self):
        self.board = []
        self.markup_board = []
        self.won = False
        for i in range(5):
            self.markup_board.append([0] * 5)

    def symbol_to_remove(self, symbol):
        for line in self.board:
            if symbol in line:
                line.remove(symbol)

    def mark_number(self, number_to_mark):
        # Oznacza na planszy oznaczeń czy trafiono odpowiednie pole
        for line in range(5):
            for column in range(5):
                if self.board[line][column] == number_to_mark:
                    self.markup_board[line][column] = 1

    def check_if_winning(self):
        # Sprawdza czy jakaś linia bądź wiersz jest trafiona
        for line in range(5):
            # sprawdź czy jest cały wiersz
            if 0 not in self.markup_board[line]:
                return True
        for column in range(5):
            if self.markup_board[0][column] == 1 and self.markup_board[1][column] == 1 and self.markup_board[2][column] == 1\
                    and self.markup_board[3][column] == 1 and self.markup_board[4][column] == 1:
                return True

        return False

    def calculate_points(self, last_bingo_number):
        # Liczy punkty wygranej planszy (nieoznaczone pola) razy (ostatnia trafiona liczba)
        self.print()
        unmarked_sum = 0
        for line in range(5):
            for column in range(5):
                if self.markup_board[line][column] == 0:
                    unmarked_sum += int(self.board[line][column])
        print("unmarked: " + str(unmarked_sum))
        return unmarked_sum * last_bingo_number

    def print(self):
        # Wyświetla planszę bingo
        print("Board")
        for line in self.board:
            print(line)

        print("Marked")
        for line in self.markup_board:
            print(line)


# Zad1
def first_task():
    # Ma za zadanie zwrócić wynik punktowy pierwszej zwycięskiej planszy bingo
    # Plansza wygrywa gdy ma wykreślony cały jeden wiersz lub kolumnę
    # Punkty liczone są jako (suma niewykreślonych pól) razy (ostatni trafiony numer)

    dataFile = open("data4.txt")
    bingo_numbers = dataFile.readline().split(',')
    print(bingo_numbers)

    # Odczytanie wszystkich pozostałych linii
    lines = []
    for line in dataFile:
        if line != '\n':
            lines.append(line)

    bingo_boards_number = int(len(lines) / 5)
    bingo_boards = []

    # Odczytanie i stworzenie instancji plansz
    for i in range(bingo_boards_number):
        new_board = bingo_board()
        new_board.board.append(lines[5 * i].replace('\n', '').replace('  ', ' ').split(' '))
        new_board.board.append(lines[5 * i + 1].replace('\n', '').replace('  ', ' ').split(' '))
        new_board.board.append(lines[5 * i + 2].replace('\n', '').replace('  ', ' ').split(' '))
        new_board.board.append(lines[5 * i + 3].replace('\n', '').replace('  ', ' ').split(' '))
        new_board.board.append(lines[5 * i + 4].replace('\n', '').replace('  ', ' ').split(' '))

        new_board.symbol_to_remove('')

        bingo_boards.append(new_board)
        print(new_board.board)

    # Przejście przez wyszystkie numery do wykreślenia
    for number in bingo_numbers:
        # Przejście przez wszystkie plansze
        for board in bingo_boards:
            # oznacz trafienie
            board.mark_number(number)
            # sprawdz czy trafiono linie bądź kolumnę
            if_winning = board.check_if_winning()

            if if_winning:
                print("Number: " + number)
                print("if_winning: " + str(if_winning))

                points = board.calculate_points(int(number))
                print("points: " + str(points))
                return points


# Zad2
def second_task():
    # Ma za zadanie zwrócić wynik punktowy ostatniej zwycięskiej planszy bingo
    # Plansza wygrywa gdy ma wykreślony cały jeden wiersz lub kolumnę
    # Punkty liczone są jako (suma niewykreślonych pól) razy (ostatni trafiony numer)

    dataFile = open("data4.txt")
    bingo_numbers = dataFile.readline().split(',')
    #bingo_numbers[-1] = '13'

    bingo_numbers = [int(bingo_numbers[i]) for i in range(len(bingo_numbers))]
    print(bingo_numbers)

    # Odczytanie wszystkich pozostałych linii
    lines = []
    for line in dataFile:
        if line != '\n':
            # Sprawdzenie czy linia zaczyna się od spacji
            if line.startswith(' '):
                line = line.lstrip()

            lines.append(line)

    bingo_boards_number = int(len(lines) / 5)
    bingo_boards = []

    # Odczytanie i stworzenie instancji plansz
    for i in range(bingo_boards_number):
        new_board = bingo_board()
        new_board.board.append(list(int(each) for each in lines[5 * i].replace('\n', '').replace('  ', ' ').split(' ')))
        new_board.board.append(list(int(each) for each in lines[5 * i + 1].replace('\n', '').replace('  ', ' ').split(' ')))
        new_board.board.append(list(int(each) for each in lines[5 * i + 2].replace('\n', '').replace('  ', ' ').split(' ')))
        new_board.board.append(list(int(each) for each in lines[5 * i + 3].replace('\n', '').replace('  ', ' ').split(' ')))
        new_board.board.append(list(int(each) for each in lines[5 * i + 4].replace('\n', '').replace('  ', ' ').split(' ')))

        bingo_boards.append(new_board)

    points_list = []
    for number in bingo_numbers:
        for board in bingo_boards:
            # jeśli ta plansza jeszcze nie wygrała
            if board.won is False:
                # oznacz trafienie
                board.mark_number(number)
                # sprawdz czy trafiono linie bądź kolumne
                if_winning = board.check_if_winning()

                if if_winning:
                    board.won = True
                    print()
                    print("Number: " + str(number))
                    print("if_winning: " + str(if_winning))
                    points = board.calculate_points(int(number))
                    points_list.append(points)
                    print("points: " + str(points))
                    print("Boards left: " + str(len(bingo_boards)))
                    print("how many numbers gen: " + str(len(bingo_numbers)))
                    print("order of number: " + str(bingo_numbers.index(number)))

    return points_list[-1]


if __name__ == '__main__':
    main()
