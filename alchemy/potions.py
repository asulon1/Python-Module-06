# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/23 18:02:49 by asulon          #+#    #+#               #
#  Updated: 2026/03/24 11:50:03 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def healing_potion() -> str:
    from .elements import create_water, create_fire
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    from .elements import create_earth, create_fire
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    from .elements import create_water, create_air
    return (f"Invisibility potion brewed with {create_air()}"
            f"and {create_water()}")


def wisdom_potion() -> str:
    from .elements import create_water, create_fire, create_air, create_earth
    list_str = [create_earth(), create_fire(), create_air(), create_water()]
    return f"Wisdom potion brewed with all elements: {', '.join(list_str)}"
