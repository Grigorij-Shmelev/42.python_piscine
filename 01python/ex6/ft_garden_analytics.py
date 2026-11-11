class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def count_grow(self) -> None:
            self._grow_calls += 1

        def count_age(self) -> None:
            self._age_calls += 1

        def count_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self, name: str, height: float = 15.0, days: int = 10,
                 growth_rate: float = 0.8) -> None:
        self.name: str = name
        self._height: float = 15.0
        self._days: int = 10
        self.set_height(height)
        self.set_age(days)
        self.growth_rate: float = growth_rate
        self._stats: Plant._Stats = self._Stats()

    @staticmethod
    def old_enough(days: int) -> bool:
        return days > 365

    @classmethod
    def anon(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def get_stats(self) -> "Plant._Stats":
        return self._stats

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 1)
        self._stats.count_grow()

    def age(self, days: int = 1) -> None:
        self._days += days
        self._stats.count_age()

    def show(self) -> None:
        self._stats.count_show()
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


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant.get_stats().display()


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 days: int, growth_rate: float, color: str) -> None:
        super().__init__(name, height, days, growth_rate)
        self.color = color
        self.is_blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def bloom(self) -> None:
        self.is_blooming = True


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float, color: str, seed_count: int) -> None:
        super().__init__(name, height, days, growth_rate, color)
        self._seed_count: int = seed_count
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = self._seed_count

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def count_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    _stats: "Tree._Stats"

    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, days, growth_rate)
        self.trunk_diameter: float = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats.count_shade()
        print(f"Tree {self.name.capitalize()} now produces "
              f"a shade of {self._height}cm long and "
              f"{self.trunk_diameter}cm wide.")


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

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 0.5 * days

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {round(self.nutritional_value)}")


def main() -> None:
    print("=== Garden Statistics ===")
    print("=== Check year-old")
    for days in (30, 400):
        print(f"Is {days} days more than a year? -> {Plant.old_enough(days)}")
    print("\n=== Flower")
    rose: Flower = Flower("rose", 15.0, 10, 8.0, "red")
    rose.show()
    display_stats(rose)
    print(f"[asking the {rose.name} to grow and bloom]")
    rose.bloom()
    rose.grow()
    rose.show()
    display_stats(rose)

    print("\n=== Tree")
    oak: Tree = Tree("oak", 200.0, 365, 1, 5.0)
    oak.show()
    display_stats(oak)
    print(f"[asking the {oak.name} to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    print("\n=== Seed")
    sunflower: Seed = Seed("Sunflower", 80.0, 45, 30, "yellow", 42)
    sunflower.show()
    print(f"[make {sunflower.name} grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)

    print("\n=== Anonymous")
    unknown_plant: Plant = Plant.anon()
    unknown_plant.show()
    display_stats(unknown_plant)


if __name__ == "__main__":
    main()
