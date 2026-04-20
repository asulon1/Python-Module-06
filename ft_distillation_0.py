# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_distillation_0.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/20 18:23:09 by asulon          #+#    #+#               #
#  Updated: 2026/04/20 18:27:47 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}")


if __name__ == "__main__":
    main()
