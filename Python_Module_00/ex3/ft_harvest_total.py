#!/usr/bin/python3


def ft_harvest_total() -> None:
    in_day_1 = int(input("Day 1 harvest: "))
    in_day_2 = int(input("Day 2 harvest: "))
    in_day_3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {in_day_1 + in_day_2 + in_day_3}")
