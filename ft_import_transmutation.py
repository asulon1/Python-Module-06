# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_import_transmutation.py                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/23 18:02:42 by asulon          #+#    #+#               #
#  Updated: 2026/03/23 18:10:01 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy
from alchemy import create_water
from alchemy.potions import healing_potion as heal


def main():
    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print(
        f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}\n")

    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}")

    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")


if __name__ == "__main__":
    main()
