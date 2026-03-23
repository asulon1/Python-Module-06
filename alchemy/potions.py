# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/23 18:02:49 by asulon          #+#    #+#               #
#  Updated: 2026/03/23 18:11:23 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_water, create_air, create_earth, create_fire


def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} and {create_water()}"
