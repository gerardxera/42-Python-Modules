#!/usr/bin/python3


class Plant():
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        growth: float = 0.5
    ) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.growth = growth

    def age(self) -> None:
        self.plant_age = self.plant_age + 1

    def grow(self) -> None:
        self.height = round(self.height + self.growth, 1)

    def show(self) -> None:
        print(
            f"Created: {self.name}: {round(self.height, 1)}cm,"
            f" {self.plant_age} days old"
        )


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    plants = [rose, oak, cactus, sunflower, fern]

    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()
