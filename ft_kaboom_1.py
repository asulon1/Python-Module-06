# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_kaboom_1.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 07:23:21 by asulon          #+#    #+#               #
#  Updated: 2026/04/21 07:28:09 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.grimoire.dark_spellbook


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    record = alchemy.grimoire.dark_spellbook.dark_spell_record(
        "Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {record}")


if __name__ == "__main__":
    main()
