#!/usr/bin/python3


class Plant():
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self._name = name
        self._height = height
        self._plant_age = plant_age
        self._stats: Plant.Stats = self.Stats()

    def grow(self) -> None:
        self._height = round(self._height + 0.5, 1)
        self._stats.count_grow()

    def age(self) -> None:
        self._plant_age = self._plant_age + 1
        self._stats.count_age()

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._plant_age} days old")
        self._stats.count_show()

    @staticmethod
    def is_year_old(days: int) -> bool:
        if days > 365:
            return True
        else:
            return False

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats():
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def count_grow(self) -> None:
            self._grow_count += 1

        def count_age(self) -> None:
            self._age_count += 1

        def count_show(self) -> None:
            self._show_count += 1

        def show(self) -> None:
            print(f"Stats: {self._grow_count} grow, {self._age_count} age,"
                  f" {self._show_count} show")


class Flower(Plant):
    def __init__(
                self,
                name: str,
                height: float,
                plant_age: int,
                color: str
    ) -> None:
        super().__init__(name, height, plant_age)
        self.color = color
        self.bloomed = False

    def grow(self) -> None:
        self._height = round(self._height + 8, 1)
        self._stats.count_grow()

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self.bloomed:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        super().__init__(name, height, plant_age)
        self.trunk_diameter = 5.0
        self._stats: Tree.Stats = self.Stats()

    def produce_shade(self) -> None:
        self._stats.count_shade()
        print(f"Tree {self._name} now produces a shade of {self._height}"
              f"cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def count_shade(self) -> None:
            self._shade += 1

        def show(self) -> None:
            super().show()
            print(f"{self._shade} shade")


class Seed(Flower):
    def __init__(
                self,
                name: str,
                height: float,
                plant_age: int,
                color: str
    ) -> None:
        super().__init__(name, height, plant_age, color)
        self.seed = 0

    def grow(self) -> None:
        self._height = round(self._height + 30, 1)
        self._stats.count_grow()

    def age(self) -> None:
        self._plant_age = self._plant_age + 20
        self._stats.count_age()

    def bloom(self) -> None:
        super().bloom()
        self.seed = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed}")


def display_statistics(plant: Plant) -> None:
    plant._stats.show()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_year_old(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365)
    oak.show()
    print("[statistics for Oak]")
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_statistics(oak)
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_statistics(sunflower)
    print()
    print("=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
