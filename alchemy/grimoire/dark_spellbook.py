# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  dark_spellbook.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 07:24:20 by asulon          #+#    #+#               #
#  Updated: 2026/04/21 07:26:31 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import List
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> List[str]:
    return ["earth", "air", "fire", "water"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    res = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({res})"
