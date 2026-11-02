#!/usr/bin/python3
from ex3 import TransformCreatureFactory


def test_transform() -> None:
    """
    Test the transformation and reversion cycle on base and evolved creatures.
    """
    factory = TransformCreatureFactory()

    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print("\nevolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    """Main function of the test"""
    print("Testing Creature with transform capability")
    test_transform()


if __name__ == "__main__":
    main()
