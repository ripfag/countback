while True:
    try:
        number = int(input("Введите число: "))
    except ValueError:
        print("Введите целое положительное число!")
        continue

    if number < 0:
        print("Введите целое положительное число!")
    else:
        while number >= 0:
            print(number)
            number -= 1


