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
        print(f"{self.name}: {self._height}cm, "
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


def main() -> None:
    print("=== Garden Security System ===")
    p: Plant = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    p.show()
    p.set_height(25)
    print("")
    print(f"Height updated: {p.get_height()}cm")
    p.set_age(30)
    print(f"Age updated: {p.get_age()} days")
    print("")
    p.set_height(-3.3)
    p.set_age(-3)
    print("")
    print("Current state:", end=" ")
    p.show()


if __name__ == "__main__":
    main()
