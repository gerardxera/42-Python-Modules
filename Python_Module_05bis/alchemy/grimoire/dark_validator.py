#!/usr/bin/python3
from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validator_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = dark_spell_allowed_ingredients()

    ingredients_lower = ingredients.lower()

    for ingredient in allowed_ingredients:
        if ingredient.lower() in ingredients_lower:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
