# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  validator.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 13:17:24 by asulon          #+#    #+#               #
#  Updated: 2026/03/24 17:04:41 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
def validate_ingredients(ingredients: str) -> str:
    required_incredients = ["fire", "water", "earth", "air"]
    split_ingredients = ingredients.split()
    valid = True
    for ingredient in split_ingredients:
        if valid is True:
            if ingredient in required_incredients:
                valid = True
            else:
                valid = False
    if valid is True:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredient} - INVALID"
