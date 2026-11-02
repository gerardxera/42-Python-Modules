#!/usr/bin/python3
from ex3 import FlameFactory, TransformCreatureFactory
from ex4 import NormalStrategy, AggressiveStrategy
from ex4.strategy import BattleStrategy
from ex3.factory import CreatureFactory


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for index in range(len(opponents)):
        factory1, strategy1 = opponents[index]

        for other_index in range(index + 1, len(opponents)):
            factory2, strategy2 = opponents[other_index]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("\n* Battle *")
            print(creature1.describe())
            print("VS")
            print(creature2.describe())
            print("now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except ValueError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def main() -> None:
    # Tournament 0 (basic)
    print("Tournament 0 (basic)")
    opponents = [
        (FlameFactory(), NormalStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    print("[ (Flameling+Normal), (Shiftling+Aggressive) ]")
    battle(opponents)

    # Tournament 1 (error)
    print("\nTournament 1 (error)")
    opponents_error: list[tuple[CreatureFactory, BattleStrategy]] = [
        (TransformCreatureFactory(), AggressiveStrategy()),
        (FlameFactory(), AggressiveStrategy()),
    ]
    print("[ (Shiftling+Aggressive), (Flameling+Aggressive) ]")
    battle(opponents_error)


if __name__ == "__main__":
    main()
