# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_pathway_debate.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 12:13:03 by asulon          #+#    #+#               #
#  Updated: 2026/03/24 13:15:15 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.transmutation import (elixir_of_life, lead_to_gold,
                                   stone_to_gem, philosophers_stone)
import alchemy.transmutation


def main():
    print("=== Pathway Debate Mastery ===\n")
    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}\n")

    print("Testing Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}\n")

    print("Testing Package Access:")
    result1 = alchemy.transmutation.lead_to_gold()
    print(f"alchemy.transmutation.lead_to_gold(): {result1}")
    result2 = alchemy.transmutation.philosophers_stone()
    print(f"alchemy.transmutation.philosophers_stone(): {result2}\n")
    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
