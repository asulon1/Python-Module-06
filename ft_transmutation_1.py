# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_transmutation_1.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 06:45:34 by asulon          #+#    #+#               #
#  Updated: 2026/04/21 06:49:20 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print("Testing lead to gold: "
          f"{alchemy.transmutation.lead_to_gold()}")


if __name__ == "__main__":
    main()
