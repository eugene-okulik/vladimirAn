class Flower:
    def __init__(
        self,
        name: str,
        price: int,
        fresh_days: int,
        color: str,
        stem_length: int,
        lifespan: int,
    ):
        self.name = name
        self.price = price
        self.fresh_days = fresh_days
        self.color = color
        self.stem_length = stem_length
        self.lifespan = lifespan


class Roza(Flower):
    def __init__(
        self,
        name: str,
        price: int,
        fresh_days: int,
        color: str,
        stem_length: int,
        lifespan: int,
        peculiarity,
    ):
        super().__init__(name, price, fresh_days, color, stem_length, lifespan)
        self.peculiarity = peculiarity


class Romashka(Flower):
    def __init__(
        self,
        name: str,
        price: int,
        fresh_days: int,
        color: str,
        stem_length: int,
        lifespan: int,
        peculiarity,
    ):
        super().__init__(name, price, fresh_days, color, stem_length, lifespan)
        self.peculiarity = peculiarity


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flowers(self, *flower: Flower):
        for f in flower:
            self.flowers.append(f)

    def total_cost(self):
        return sum(flower.price for flower in self.flowers)

    def avg_lifespan(self):
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_by_freshness(self, reverse: bool = False):
        self.flowers.sort(key=lambda x: x.fresh_days, reverse=reverse)

    def sort_by_color(self, reverse: bool = False):
        self.flowers.sort(key=lambda x: x.color, reverse=reverse)

    def sort_by_stem_length(self, reverse: bool = False):
        self.flowers.sort(key=lambda x: x.stem_length, reverse=reverse)

    def sort_by_price(self, reverse: bool = False):
        self.flowers.sort(key=lambda x: x.price, reverse=reverse)

    def get_info(self):
        result = ""
        for flower in self.flowers:
            result += f"- {flower.name}: {flower.price} руб.\n"
        return result

    def find_by_lifespan(self, target_lifespan: int):
        found = []
        for flower in self.flowers:
            if flower.lifespan == target_lifespan:
                found.append(flower)
        return found


roza_red = Roza("Роза красная", 200, 2, "Красный", 60, 10, "колючая")
roza_white = Roza("Роза белая", 250, 1, "Белый", 70, 12, "пахучая")
romashka = Romashka("Ромашка полевая", 50, 3, "Белый", 40, 7, "6 белых лепестков")

bouquet = Bouquet()
bouquet.add_flowers(roza_red, roza_white, romashka)

coast = bouquet.total_cost()
avg = bouquet.avg_lifespan()
print("Общая стоимость:", coast)
print("Среднее время жизни букета:", avg)

print("Сортировка цены по возрастанию")
bouquet.sort_by_price()
print(bouquet.get_info())
print("Сортировка цены по убыванию")
bouquet.sort_by_price(reverse=True)
print(bouquet.get_info())
print("Сортировка цены по убыванию")
bouquet.sort_by_price(reverse=True)
print(bouquet.get_info())
print("Поиск цветов по временем жизни")
found_flowers = bouquet.find_by_lifespan(10)
for f in found_flowers:
    print(f"- Найдено: {f.name} (Время жизни: {f.lifespan} дней)")

print("Сортировка цветов по алфавиту (по цвету):")
bouquet.sort_by_color()
for flower in bouquet.flowers:
    print(f"- {flower.name} (Цвет: {flower.color})")

print("Сортировка по длине стебля (от коротких к длинным):")
bouquet.sort_by_stem_length()
for flower in bouquet.flowers:
    print(f"- {flower.name} (Длина стебля: {flower.stem_length} см)")
