#!/usr/bin/python3


def ft_water_reminder() -> None:
    in_days = int(input("Days since last watering: "))
    if in_days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
