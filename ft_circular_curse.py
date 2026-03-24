# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_circular_curse.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 14:38:18 by asulon          #+#    #+#               #
#  Updated: 2026/03/24 17:08:57 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.grimoire import validate_ingredients, record_spell


def main():
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print(
        'validate_ingredients("fire air"): '
        f'{validate_ingredients("fire air")}')
    print(
        'validate_ingredients("dragon scales"): '
        f'{validate_ingredients("dragon scales")}\n')

    print("Testing spell recording with validation:")
    print(
        f'record_spell("Fireball", "fire air"): {record_spell("Fireball", "fire air")}')
    print(
        f'record_spell("Dark Magic", "shadow"): {record_spell("Dark Magic", "shadow")}\n')

    print("Testing late import technique:")
    print(
        f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}\n')

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
