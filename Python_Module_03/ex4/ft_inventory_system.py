#!/usr/bin/python3
import sys


def parse_item(argument: str) -> tuple[str, int]:
    parts = argument.split(':')
    if len(parts) != 2:
        raise ValueError(f"Error - invalid parameter '{argument}'")

    try:
        quantity = int(parts[1])
    except ValueError as error:
        raise ValueError(f"Quantity error for '{parts[0]}': {error}")
    return parts[0], quantity


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for argument in sys.argv[1:]:
        try:
            name, quantity = parse_item(argument)
        except ValueError as error:
            print(f"{error}")
            continue

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        inventory[name] = quantity

    print(f"Got inventory: {inventory}")
    names = list(inventory.keys())
    print(f"Item list: {names}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for item, quantity in inventory.items():
        porcentatge = round((quantity / total) * 100, 1)
        print(f"Item {item} represents {porcentatge}%")

    most_item = ""
    least_item = ""
    most_quantity = 0
    least_quantity = 0

    for item, quantity in inventory.items():
        if most_item == "" or quantity > most_quantity:
            most_item = item
            most_quantity = quantity
        if least_item == "" or quantity < least_quantity:
            least_item = item
            least_quantity = quantity

    print(f"Item most abundant: {most_item} with quantity {most_quantity}")
    print(f"Item least abundant: {least_item} with quantity {least_quantity}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
