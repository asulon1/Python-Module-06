# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_kaboom_0.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 07:00:51 by asulon          #+#    #+#               #
#  Updated: 2026/04/21 07:22:09 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    record = alchemy.grimoire.light_spell_record(
        "Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {record}")


if __name__ == "__main__":
    main()
