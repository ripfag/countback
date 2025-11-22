def count_back():
    try:
        get_number = int(input("Введите число: "))
    except ValueError:
        print("Введено не число, введите число!")
        return count_back()
    if get_number < 0:
        print("Введите целое положительное число!")
        return count_back()
    else:
        while True:
            if get_number > -1:
                print("Счетчик: ", get_number)
                get_number -= 1
            if get_number == -1:
                break


count_back()

