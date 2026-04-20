# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/20 18:15:46 by asulon          #+#    #+#               #
#  Updated: 2026/04/20 18:29:35 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def healing_potion() -> str:
    from alchemy.elements import create_air, create_earth
    return (f"Healing potion brewed with '{create_earth()}' "
            f"and '{create_air()}'")


def strength_potion() -> str:
    from elements import create_fire, create_water
    return (f"Strength potion brewed with '{create_fire()}' "
            f"and '{create_water()}'")
