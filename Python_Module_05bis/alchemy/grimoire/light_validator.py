#!/usr/bin/python3

def validate_ingredients(ingredients: str) -> str:
    ''' import pakage prevent circular explosion '''
    from .light_spellbook import light_spell_allowed_ingredients
    ''' get words originals '''
    allowed_ingredients = light_spell_allowed_ingredients()
    ''' get word lowers '''
    ingredients_lower = ingredients.lower()

    for ingrediant in allowed_ingredients:
        if ingrediant.lower() in ingredients_lower:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
