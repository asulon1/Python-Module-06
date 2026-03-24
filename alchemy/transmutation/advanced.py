# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  advanced.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 12:09:51 by asulon          #+#    #+#               #
#  Updated: 2026/03/24 13:10:03 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    return (f"Philosopher’s stone created using {lead_to_gold()} "
            f"and {healing_potion()}")


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
