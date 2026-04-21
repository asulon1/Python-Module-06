# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  recipes.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 06:35:52 by asulon          #+#    #+#               #
#  Updated: 2026/04/21 06:45:04 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_air
from elements import create_fire
from ..potions import strength_potion


def lead_to_gold() -> str:
    return ("Recipe transmuting Lead to Gold: brew "
            f"’{create_air()}’ and ’{strength_potion()}’ mixed with "
            f"’{create_fire()}’")
