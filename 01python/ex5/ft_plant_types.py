class Plant:
    def __init__(self, name: str, height: float = 15.0, days: int = 10,
                 growth_rate: float = 0.8) -> None:
        self.name: str = name
        self._height: float = 15.0
        self._days: int = 10
        self.set_height(height)
        self.set_age(days)
        self.growth_rate: float = growth_rate

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 1)

    def age(self) -> None:
        self._days += 1

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self._height}cm, "
              f"{self._days} days old")

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_days: int) -> None:
        if new_days >= 0:
            self._days = new_days
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return self._days


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float, color: str) -> None:
        super().__init__(name, height, days, growth_rate)
        self.color = color
        self.is_blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming is True:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.is_blooming = True


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, days, growth_rate)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces", end=" ")
        print(f"a shade of {self._height}cm long and", end=" ")
        print(f"{self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float,
                 harvest_season: str, nutritional_value: float) -> None:
        super().__init__(name, height, days, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {round(self.nutritional_value)}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose: Flower = Flower("rose", 15.0, 10, 0.6, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak: Tree = Tree("oak", 200.0, 365, 1, 5.0)
    oak.show()
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato: Vegetable = Vegetable("tomato", 5.0, 10, 2.1, "April", 0)
    tomato.show()
    print(f"[make {tomato.name} grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
