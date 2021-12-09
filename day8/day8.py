def main():
    # Wyświetla wynik pierwszej lub drugiej części zadania / należy zamienić wywołanie funkcji
    print("Result: " + str(second_task()))


# Zad1
def first_task():
    # Karby płyną własnymi łódkami podwodnymi na pomoc
    # Przemieszczają się tylko horyzontalnie, aby wykonać pomocniczy strzał, musza być w tym samym miejscu
    # Każdy ruch do współrzędnej o 1 większej wynosi 1 jednostkę paliwa
    # Do jakiej pozycji powinny udać się kraby, aby zużyć jak najmniej paliwa
    count = {1: 0,
             4: 0,
             7: 0,
             8: 0}

    dataFile = open("data8.txt")
    for line in dataFile:
        splited_line = line.split('|')
        pattern = splited_line[0].replace('\n', '').rstrip().split(" ")
        digit_output = splited_line[1].replace('\n', '').lstrip().split(" ")
        print("Pattern len: " + str(len(pattern)))
        print("Digi out len: " + str(len(digit_output)))

        for dig_out in digit_output:
            if len(dig_out) == 2:
                print(dig_out)
                count[1] += 1
            elif len(dig_out) == 4:
                count[4] += 1
                print(dig_out)
            elif len(dig_out) == 3:
                count[7] += 1
                print(dig_out)
            elif len(dig_out) == 7:
                count[8] += 1
                print(dig_out)

    count_sum = sum(count.values())

    return count_sum


# Zad2
def second_task():
    # Karby płyną własnymi łódkami podwodnymi na pomoc
    # Przemieszczają się tylko horyzontalnie, aby wykonać pomocniczy strzał, musza być w tym samym miejscu
    # Pierwszy ruch do współrzędnej o 1 większej wynosi 1 jednostkę paliwa, każdy koleny o jeden więcej
    # Do jakiej pozycji powinny udać się kraby, aby zużyć jak najmniej paliwa

    known_digits = {1: "", 4: "", 7: "", 8: ""}
    unknown_digits = {0: "", 2: "", 3: "", 5: "", 6: ""}
    sum_of_out_numbers = 0
    out_number = ""

    dataFile = open("data8.txt")
    for line in dataFile:
        splited_line = line.split('|')
        pattern = splited_line[0].replace('\n', '').rstrip().split(" ")
        digit_output = splited_line[1].replace('\n', '').lstrip().split(" ")
        print("Pattern len: " + str(len(pattern)))
        print("Digi out len: " + str(len(digit_output)))

        for one in pattern:
            if len(one) == 2:
                known_digits[1] = one
            elif len(one) == 4:
                known_digits[4] = one
            elif len(one) == 3:
                known_digits[7] = one
            elif len(one) == 7:
                known_digits[8] = one

        unknown_digits[5] = known_digits[8][1] + known_digits[8][3] + known_digits[8][5] + known_digits[8][6] + known_digits[8][2]
        print("\n 5:")
        print(unknown_digits[5])

        unknown_digits[2] = known_digits[8][4] + known_digits[8][1] + known_digits[8][3] + known_digits[8][5] + known_digits[8][0]
        print("\n 2:")
        print(unknown_digits[2])

        unknown_digits[3] = known_digits[8][5] + known_digits[8][6] + known_digits[8][1] + known_digits[8][0] + known_digits[8][3]
        print("\n 3:")
        print(unknown_digits[3])

        unknown_digits[9] = known_digits[8][1] + known_digits[8][2] + known_digits[8][5] + known_digits[8][0] + known_digits[8][6] + known_digits[8][3]
        print("\n 9:")
        print(unknown_digits[9])

        unknown_digits[6] = known_digits[8][1] + known_digits[8][3] + known_digits[8][5] + known_digits[8][4] + known_digits[8][2] + known_digits[8][6]
        print("\n 6:")
        print(unknown_digits[6])

        unknown_digits[0] = known_digits[8][1] + known_digits[8][0] + known_digits[8][4] + known_digits[8][2] + known_digits[8][3] + known_digits[8][6]
        print("\n 0:")
        print(unknown_digits[0])


        print("#################################################################")
        print(known_digits)
        print(unknown_digits)

        print("#################################################################")



        out_number = ""
        for one in digit_output:
            dig_value = -1
            for key in known_digits.keys():
                print("\nsorted one: ")
                print(sorted(one))
                print("key:")
                print(key)
                print("sorted known: ")
                print(sorted(known_digits.get(key)))
                if sorted(one) == sorted(known_digits.get(key)):
                    dig_value = key
            if dig_value == -1:
                for key in unknown_digits.keys():
                    print("\nsorted one: ")
                    print(sorted(one))
                    print("key:")
                    print(key)
                    print("sorted unknown: ")
                    print(sorted(unknown_digits.get(key)))
                    if sorted(one) == sorted(unknown_digits.get(key)):
                        dig_value = key

            out_number += str(dig_value)
            print(out_number)

    sum_of_out_numbers += int(out_number)


if __name__ == '__main__':
    main()

