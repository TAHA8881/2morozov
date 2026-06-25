from trips import AvtoObservation,  AvtoAnalyzer

def input_observation() ->  AvtoObservation:
    """Функция ввода данных с проверкой корректности."""
    while True:
        date = float(input("Введите дату (например, 06.24): "))
        if date:
            break
        print("Дата не может быть пустой.")

    while True:
        try:
            km = float(input("Введите расстояние в километрах (в км): "))
            break
        except ValueError:
            print("Ошибка: введите число.")
    while True:
        try:
            name = input("Введите имя маршрута: ")
            if name != "":
                break
            print("имя маршрута не может быть пустым")
        except ValueError:
            print("Ошибка: введите число.")

    while True:
        try:
            rashod = float(input("Введите расход топлива в числах: "))
            if 0 <= rashod:
                break
            print("Средний расход топлива на 100 километров должен быть от 0")
        except ValueError:
            print("Ошибка: введите число.")

    while True:
        try:
            price = float(input("Введите cтоимость одного литра топлива (руб., неотрицательное): "))
            if price >= 0:
                break
            print("Скорость может быть отрицательной.")
        except ValueError:
            print("Ошибка: введите число.")

    return  AvtoObservation(date, km, name, rashod, price)
#date:float, km:float, name, rashod:float, price:float):

def main():
    analyzer =  AvtoAnalyzer()

    # Добавление демонстрационных данных за 5 дней (по условию)
    demo_data = [
        (20.02, 22.5, "ggg1", 65.0, 3.2),
        (26.05, 18.0, "ggg2", 80.0, 5.1),
        (2.09, 25.3, "ggg3", 55.0, 2.0),
        (23.07, 14.8, "ggg4", 90.0, 4.5),
        (24.06, 20.0, "ggg5", 70.0, 3.0),
    ]
    for date, km, name, rashod, price in demo_data:
        analyzer.add_observation( AvtoObservation(date, km, name, rashod, price))

    while True:
        print("\n=== Система анализа поездок ===")
        print("1. Добавить наблюдение")
        print("2. Просмотреть все наблюдения")
        print("3. Рассчитать топливо")
        print("4. Определить цену")
        print("5. Определить самый дорогой маршрут")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "0":
            print("До свидания!")
            break
        elif choice == "1":
            obs = input_observation()
            analyzer.add_observation(obs)
            print("Наблюдение добавлено.")
        elif choice == "2":
            obs_list = analyzer.get_all()
            if not obs_list:
                print("Нет наблюдений.")
            else:
                for i, obs in enumerate(obs_list, 1):
                    print(f"{i}. {obs}")
        elif choice == "3":
            avg = analyzer.average_toplivo()
            if avg is None:
                print("Нет данных.")
            else:
                print(f"Сколько топлива: {analyzer.average_toplivo()}")
     
        elif choice == "4":
            avg = analyzer.toplivo_price()
            if avg is None:
                print("Нет данных.")
            else:
                print(f"Сколько цена топлива: {analyzer.toplivo_price()}")
 
        elif choice == "5":
            coldest = analyzer.priciest_day()
            if coldest is None:
                print("Нет данных.")
            else:
                print(f"Самый дорогой маршрут: {analyzer.priciest_day()}")
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()