class Flower:
    def __init__(
            self,
            name: str,
            color: str,
            stem_length: int,
            life_cycle: int,
            price: int
    ):
        self.__name = name
        self.__color = color
        self.__stem_length = stem_length
        self.__life_cycle = life_cycle
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def stem_length(self):
        return self.__stem_length

    @stem_length.setter
    def stem_length(self, value):
        self.__stem_length = value

    @property
    def life_cycle(self):
        return self.__life_cycle

    @life_cycle.setter
    def life_cycle(self, value):
        self.__life_cycle = value

    @property
    def price(self):
        return self.__life_cycle

    @price.setter
    def price(self, value):
        self.__price = value

    def __repr__(self):
        return (f"{self.__stem_length}cm {self.__color} {self.__name} "
                f"(Life cycle: {self.__life_cycle}, Price: ${self.__price})")

    def __str__(self):
        return (f"{self.__stem_length}cm {self.__color} {self.__name} "
                f"(Life cycle: {self.__life_cycle}, Price: ${self.__price})")


class Rose(Flower):
    def __init__(
            self,
            color: str,
            stem_length: int,
            life_cycle: int,
            price: int
    ):
        super().__init__("Rose", color, stem_length, life_cycle, price)
        self.__spikes = True

    @property
    def spikes(self):
        return self.__spikes

    @spikes.setter
    def spikes(self, value):
        self.__spikes = value

    def __repr__(self):
        if self.__spikes:
            return (f"{self.stem_length}cm {self.color} {self.name} with "
                    f"spikes (Life cycle: {self.life_cycle}, "
                    f"Price: ${self.price})")
        return (f"{self.stem_length}cm {self.color} {self.name} without spikes"
                f" (Life cycle: {self.life_cycle}, Price: ${self.price})")

    def __str__(self):
        if self.__spikes:
            return (f"{self.stem_length}cm {self.color} {self.name} with "
                    f"spikes (Life cycle: {self.life_cycle}, "
                    f"Price: ${self.price})")
        return (f"{self.stem_length}cm {self.color} {self.name} without spikes"
                f" (Life cycle: {self.life_cycle}, Price: ${self.price})")


class Tulip(Flower):
    def __init__(
            self,
            color: str,
            stem_length: int,
            life_cycle: int,
            price: int
    ):
        super().__init__("Tulip", color, stem_length, life_cycle, price)


class Lily(Flower):
    def __init__(
            self,
            color: str,
            stem_length: int,
            life_cycle: int,
            price: int
    ):
        super().__init__("Lily", color, stem_length, life_cycle, price)


class Bouquet:
    def __init__(self):
        self.__flowers = []  # flowers objects list

    def add_flower(self, flower):
        self.__flowers.append(flower)

    @property
    def calculate_total_price(self):
        return sum(flower.price for flower in self.__flowers)

    @property
    def calculate_total_flower_count(self):
        return len(self.__flowers)

    @property
    def calculate_average_life_cycle(self):
        if not self.__flowers:
            return "No flowers in the bouquet"
        return sum(
            flower.life_cycle for flower in self.__flowers
        ) / len(self.__flowers)

    def sort_by_color(self):
        self.__flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        self.__flowers.sort(key=lambda flower: flower.stem_length)

    def sort_by_life_cycle(self):
        self.__flowers.sort(key=lambda flower: flower.life_cycle)

    def sort_by_price(self):
        self.__flowers.sort(key=lambda flower: flower.price)

    def find_flowers_by_param(self, key, value):
        """
        Finds flowers in a bouquet by the given parameter and value.
        :param key: a string representing an attribute
                    (e.g. "color", "size", "life_cycle", "price").
        :param value: value to search for.
        :return: list of suitable colors.
        """
        if not self.__flowers:
            return "No flowers in the bouquet"

        flowers_list = []
        for flower in self.__flowers:
            if getattr(flower, key) == value:
                flowers_list.append(flower)
        return flowers_list

    def __str__(self):
        flowers_str = "\n ".join([repr(flower) for flower in self.__flowers])
        return (f"Bouquet:\n {flowers_str}\n"
                f"Total count: {self.calculate_total_flower_count} flowers.\n"
                f"Total price: ${self.calculate_total_price}.\n"
                f"Average life cycle: {self.calculate_average_life_cycle:.1f}"
                f" days.")


if __name__ == "__main__":
    # Flowers creation
    rose1 = Rose("Red", 20, 5, 9)
    rose2 = Rose("White", 21, 4, 9)
    rose2.spikes = False
    rose3 = Rose("White", 21, 4, 9)
    tulip1 = Tulip("Yellow", 18, 3, 3)
    tulip2 = Tulip("Red", 18, 3, 3)
    tulip3 = Tulip("Red", 18, 3, 3)
    lily1 = Lily("White", 27, 5, 5)
    lily2 = Lily("Blue", 24, 5, 5)
    lily3 = Lily("White", 25, 5, 5)

    # print info about flowers
    print("rose1 ->", rose1)
    print("rose2 ->", rose2)
    print("rose3 ->", rose3)
    print("tulip1 ->", tulip1)
    print("tulip2 ->", tulip2)
    print("tulip3 ->", tulip3)
    print("lily1 ->", lily1)
    print("lily2 ->", lily2)
    print("lily3 ->", lily3)

    # Bouquet creation
    bouquet = Bouquet()
    print(
        "calculate_average_life_cycle ->",
        bouquet.calculate_average_life_cycle
    )

    # Addition flowers to the bouquet
    bouquet.add_flower(rose1)
    bouquet.add_flower(rose2)
    bouquet.add_flower(rose3)
    bouquet.add_flower(tulip1)
    bouquet.add_flower(tulip2)
    bouquet.add_flower(tulip3)
    bouquet.add_flower(lily1)
    bouquet.add_flower(lily2)
    bouquet.add_flower(lily3)

    # print info about bouquet
    print(bouquet)

    # Sort bouquet
    bouquet.sort_by_color()
    print("sorted by color ->", bouquet)
    bouquet.sort_by_stem_length()
    print("sorted by stem length ->", bouquet)
    bouquet.sort_by_life_cycle()
    print("sorted by life cycle ->", bouquet)
    bouquet.sort_by_price()
    print("sorted by price ->", bouquet)

    # find flowers by param
    print(
        "find flowers by color ->",
        bouquet.find_flowers_by_param("color", "White")
    )

    print(
        "find flowers by stem length ->",
        bouquet.find_flowers_by_param("stem_length", 20)
    )

    print(
        "find flowers by life cycle ->",
        bouquet.find_flowers_by_param("life_cycle", 3)
    )
    print(
        "find flowers by price ->",
        bouquet.find_flowers_by_param("price", 5)
    )
