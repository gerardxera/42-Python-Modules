#!/usr/bin/python3


class Plant():
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        self.height = round(self.height + 0.5, 1)

    def age(self) -> None:
        self.plant_age = self.plant_age + 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm,"
              f" {self.plant_age} days old")


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, plant_age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self.bloomed:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.height}cm "
              f"long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def grow(self) -> None:
        self.height = round(self.height + 2.1, 1)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.age()
        tomato.grow()
    tomato.show()


if __name__ == "__main__":
    main()
