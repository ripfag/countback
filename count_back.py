get_number = None
while True:
    try:
        get_number = float(input("Введите положительное число: "))
        if get_number < 0:
            print("Введите целое положительное число!")


        while get_number > -1:
            print("Счетчик: ",get_number)
            get_number -= 1
            if get_number == -1:
                break


    except ValueError:
        print("Введено не число, введите число!")
    except TypeError:
        print("Введите целое положительное число!")

