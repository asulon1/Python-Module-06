# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  basic.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 12:08:15 by asulon          #+#    #+#               #
#  Updated: 2026/03/24 13:06:16 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def lead_to_gold() -> str:
    from alchemy.elements import create_fire
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    from alchemy.elements import create_earth
    return f"Stone transmuted to gem using {create_earth()}"
