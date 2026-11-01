class Plant:
    def __init__(self, name: str, height: float, days: int,
                 growth_rate: float = 0.8) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days
        self.growth_rate: float = growth_rate

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, "
              f"{self.days} days old")


def main() -> None:
    print("=== Plant Factory Output ===")
    p1: Plant = Plant("Rose", 25.0, 30)
    p2: Plant = Plant("Oak", 200.0, 365)
    p3: Plant = Plant("Cactus", 5.0, 90)
    p4: Plant = Plant("Sunflower", 80.0, 45)
    p5: Plant = Plant("Fern", 15.0, 120)
    garden: list[Plant] = [p1, p2, p3, p4, p5]
    for p in garden:
        print("Created:", end=" ")
        p.show()


if __name__ == "__main__":
    main()
