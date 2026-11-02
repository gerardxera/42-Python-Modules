#!/usr/bin/python3


class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        growth: float,
        plant_age: int
    ) -> None:
        self.name = name
        self.height = height
        self.growth = growth
        self.plant_age = plant_age

    def age(self) -> None:
        self.plant_age = self.plant_age + 1

    def grow(self) -> None:
        self.height = round(self.height + self.growth, 1)

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm,"
            f" {self.plant_age} days old"
        )


def main() -> None:
    rose = Plant("Rose", 25.0, 0.80, 30)
    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.age()
        rose.grow()
        rose.show()
    total_growth = round(rose.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()
