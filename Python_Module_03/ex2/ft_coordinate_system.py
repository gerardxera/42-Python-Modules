#!/usr/bin/python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as "
                           "floats in format 'x,y,z': ")
        posicion = user_input.split(',')
        if len(posicion) == 3:
            coords: list[float] = []
            for leter in posicion:
                param = leter.strip()
                try:
                    coords.append(float(param))
                except ValueError as error:
                    print(f"Error on parameter '{param}': {error}")
            if len(coords) == 3:
                return (coords[0], coords[1], coords[2])
        else:
            print("Invalid syntax")


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    x1, y1, z1 = pos1
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    center = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    print(f"Distance to center: {round(center, 4)}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    x2, y2, z2 = pos2
    between = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between the 2 sets of coordinates: {round(between, 4)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user Ctrl + C.")
    except EOFError:
        print("\nProgram interrupted by user Ctrl + D.")
