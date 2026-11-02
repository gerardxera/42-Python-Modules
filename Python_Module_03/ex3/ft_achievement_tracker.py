#!/usr/bin/python3
import random


# Constante inmutable con el catálogo de todos los logros del juego
ACHIEVEMENTS: tuple[str, ...] = (
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
)


def gen_player_achievements() -> set[str]:
    count = random.randint(3, 10)
    sampled_archivement = random.sample(ACHIEVEMENTS, count)
    return set(sampled_archivement)


def main() -> None:
    print("=== Achievement Tracker System ===")

    players: list[tuple[str, set[str]]] = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements()),
    ]

    for name, achi in players:
        print(f"Player {name}: {achi}")
    print()

    achi_sets: list[set[str]] = []
    for name, achi in players:
        achi_sets.append(achi)

    all_achi = set.union(*achi_sets)
    common_achi = set.intersection(*achi_sets)
    print(f"All distinct achievements: {all_achi}")
    print()
    print(f"Common achievements: {common_achi}")
    print()

    for name, achi in players:
        other_set: list[set[str]] = []
        for other_name, other_achi in players:
            if name != other_name:
                other_set.append(other_achi)
        other_union = set.union(*other_set)
        unique_achi = set.difference(achi, other_union)
        print(f"Only {name} has: {unique_achi}")
    print()

    catalog = set(ACHIEVEMENTS)
    for name, achi in players:
        missing_arch = set.difference(catalog, achi)
        print(f"{name} is missing: {missing_arch}")


if __name__ == "__main__":
    main()
