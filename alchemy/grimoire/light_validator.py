# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  light_validator.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 06:56:15 by asulon          #+#    #+#               #
#  Updated: 2026/04/21 07:21:30 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    for allowed in light_spell_allowed_ingredients():
        if allowed.lower() in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
