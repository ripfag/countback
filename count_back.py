while True:
    try:
        number = int(input("Введите число: "))
        if number > 0:
            break
        else:
            print("Введите целое положительное число!")
    except ValueError:
        print("Введите целое положительное число!")


while number >= 0:
    print(number)
    number -= 1




