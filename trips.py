class AvtoObservation:
    """Класс для представления одного погодного наблюдения."""
    def __init__(self, date:float, km:float, name, rashod:float, price:float):
        self.date = date
        self.km = km
        self.name = name
        self.rashod = rashod
        self.price = price

    def __str__(self) -> str:
        return (f"Дата: {self.date}, Название маршрута: {self.name}, "
                f"Расстояние в километрах: {self.km} km, Cредний расход топлива на 100 километров: {self.rashod} топливо/100км, "
                f"Стоимость одного литра топлива: {self.price} руб")


class AvtoAnalyzer:
    """Класс для хранения и анализа набора погодных наблюдений."""
    def __init__(self):
        self.observations = []

    def add_observation(self, observation: AvtoObservation) -> None:
        self.observations.append(observation)

    def get_all(self) -> list:
        return self.observations
# Топливо (л) = (Расстояние (км) × Расход (л/100 км)) / 100
    def average_toplivo(self) -> AvtoObservation | None:
        if not self.observations:
            return None
        average_toplivo= self.km * self.rashod/100
        return (f"{average_toplivo}")

    def toplivo_price(self) -> AvtoObservation | None:
        if not self.observations:
            return None
        toplivo_price= self.km * self.rashod/100*self.price
        return (f"{toplivo_price}")

    def priciest_day(self) -> AvtoObservation | None:
        if not self.observations:
            return None
        return max(self.observations)
