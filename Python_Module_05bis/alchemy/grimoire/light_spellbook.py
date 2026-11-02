#!/usr/bin/python3
from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:

    # 1. Se la pasamos al validator
    validation: str = validate_ingredients(ingredients)

    # 2. Decidimos si se registra o se rechaza
    if "VALID" in validation:
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"
