class Plant:
    def __init__(self, name: str, height: float,
                 growth_rate: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.growth_rate: float = growth_rate
        self.days: int = days

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")
    p1: Plant = Plant("Rose", 25.0, 0.8, 30)
    p1.show()
    in_the_beninging: float = p1.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        p1.grow()
        p1.age()
        p1.show()
    in_the_end: float = round(p1.height - in_the_beninging, 1)
    print(f"Growth this week: {in_the_end}cm")


if __name__ == "__main__":
    main()
