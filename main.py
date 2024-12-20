import requests

API_URL = "https://v6.exchangerate-api.com/v6/263fb40fe97546c380bc3537/latest/USD"

def get_current_exchange_rate():
    try:
        response = requests.get(API_URL)
        data = response.json()

        if response.status_code == 200:
            rub_to_usd = data["conversion_rates"]["RUB"]
            return rub_to_usd
        else:
            print("Ошибка при получении курса.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")
        return None

def convert_rubles_to_dollars(rubles, rate):
    return rubles / rate

def convert_dollars_to_rubles(dollars, rate):
    return dollars * rate

def main():
    exchange_rate = get_current_exchange_rate()

    if exchange_rate is None:
        print("Не удалось получить курс валют. Программа завершена.")
        return

    print(f"Текущий курс доллара к рублю: 1 USD = {exchange_rate} руб.\n")

    print("1. Конвертировать рубли в доллары")
    print("2. Конвертировать доллары в рубли")

    choice = input("Ваш выбор: ")

    if choice == '1':
        try:
            rubles = float(input("Введите сумму в рублях: "))
            if rubles < 0:
                print("Сумма не может быть отрицательной")
            else:
                dollars = convert_rubles_to_dollars(rubles, exchange_rate)
                print(f"{rubles} рублей = {dollars:.2f} доллара(ов)")
        except ValueError:
            print("Введите корректное число!")
    elif choice == '2':
        try:
            dollars = float(input("Введите сумму в долларах: "))
            if dollars < 0:
                print("Сумма не может быть отрицательной")
            else:
                rubles = convert_dollars_to_rubles(dollars, exchange_rate)
                print(f"{dollars} долларов = {rubles:.2f} рублей")
        except ValueError:
            print("Введите корректное число!")
    else:
        print("Некорректный выбор.")

if __name__ == "__main__":
    main()
