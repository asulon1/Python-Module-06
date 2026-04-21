# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  light_spellbook.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 06:50:54 by asulon          #+#    #+#               #
#  Updated: 2026/04/21 07:19:49 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import List


def light_spell_allowed_ingredients() -> List[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    res = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({res})"
