# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_kaboom_1.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 07:23:21 by asulon          #+#    #+#               #
#  Updated: 2026/04/21 10:55:00 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        record = dark_spell_record(
            "Fantasy", "Earth, wind and fire")
        print(f"Testing record light spell: {record}")
    except ImportError as error:
        print(f"ImportError: {error}")


if __name__ == "__main__":
    main()
