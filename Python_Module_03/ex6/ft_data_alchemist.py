#!/usr/bin/python3
import random


PLAYERS: list[str] = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {PLAYERS}")
    all_capitalize: list[str] = [player.capitalize() for player in PLAYERS]
    print(f"New list with all names capitalized: {all_capitalize}")
    only_capitalize: list[str] = [
        player for player in PLAYERS
        if player.istitle()
    ]
    print(f"New list of capitalized names only: {only_capitalize}")
    players_scores: dict[str, int] = {
        player: random.randint(1, 500)
        for player in all_capitalize
    }
    print(f"Score dict: {players_scores}")
    avarage_score: float = sum(players_scores.values()) / len(players_scores)
    print(f"Score average is {round(avarage_score, 2)}")
    high_scores: dict[str, int] = {
        player: score
        for player, score in players_scores.items()
        if score > avarage_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
