# Константы для курсов
RUB_TO_USD_RATE = 0.0102
USD_TO_RUB_RATE = 98


def convert_rubles_to_dollars(rubles):
    return rubles * RUB_TO_USD_RATE


def convert_dollars_to_rubles(dollars):
    return dollars * USD_TO_RUB_RATE


def main():
    print("1. Конвертировать рубли в доллары")
    print("2. Конвертировать доллары в рубли")

    choice = input("Ваш выбор: ")

    if choice == '1':
        try:
            rubles = float(input("Введите сумму в рублях: "))
            if rubles < 0:
                print("Сумма не может быть отрицательной!")
            else:
                dollars = convert_rubles_to_dollars(rubles)
                print(f"{rubles} рублей = {dollars:.2f} доллара(ов)")
        except ValueError:
            print("Введите корректное число!")
    elif choice == '2':
        try:
            dollars = float(input("Введите сумму в долларах: "))
            if dollars < 0:
                print("Сумма не может быть отрицательной!")
            else:
                rubles = convert_dollars_to_rubles(dollars)
                print(f"{dollars} долларов = {rubles:.2f} рублей")
        except ValueError:
            print("Ошибка: введите корректное число!")

    else:
        print("Некорректный выбор! Попробуйте снова.")


if __name__ == "__main__":
    main()
