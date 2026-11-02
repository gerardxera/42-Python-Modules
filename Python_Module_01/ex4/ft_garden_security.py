#!/usr/bin/python3


class Plant():
    def __init__(
        self,
        name: str,
        height: float,
        plant_age: int,
        growth: float = 0.5
    ) -> None:
        self._name = name
        self._height = height
        self._plant_age = plant_age
        self._growth = growth

    def age(self) -> None:
        self._plant_age = self._plant_age + 1

    def grow(self) -> None:
        self._height = round(self._height + self._growth, 1)

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm,"
              f" {self._plant_age} days old")

    # GETTERS (para leer)
    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age

    # SETTERS (para modificar con filtro de seguridad)
    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {int(new_height)}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._plant_age = new_age
            print(f"Age updated: {int(new_age)} days")


def main() -> None:
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-10)
    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
