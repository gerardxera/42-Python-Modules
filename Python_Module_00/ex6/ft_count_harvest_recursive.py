#!/usr/bin/python3


def recursive(day: int, total_day: int) -> None:
    if total_day > 0:
        print(f"Day {day}")
        recursive(day + 1, total_day - 1)
    else:
        print("Harvest time!")
        return


def ft_count_harvest_recursive() -> None:
    total_day = int(input("Days until harvest: "))
    day = 1
    recursive(day, total_day)
