#!/usr/bin/python3


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    # Pongo el import en esta posicion pq si no, no imprime los print
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(dark_spell_record("Darkness", "bats and frogs"))


if __name__ == "__main__":
    main()
