# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  spellbook.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 13:21:36 by asulon          #+#    #+#               #
#  Updated: 2026/03/24 17:04:36 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    validate = validate_ingredients(ingredients)
    if validate.find("VALID") >= 0:
        return f"Spell recorded: {spell_name} ({validate})"
    else:
        return f"Spell rejected: {spell_name} ({validate})"
