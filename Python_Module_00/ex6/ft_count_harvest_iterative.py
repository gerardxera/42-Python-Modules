#!/usr/bin/python3


def ft_count_harvest_iterative() -> None:
    in_day = int(input("Days until harvest: "))
    for i in range(1, in_day + 1):
        print(f"Day {i}")
    print("Harvest time!")
