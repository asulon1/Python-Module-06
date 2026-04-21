# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_transmutation_2.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 06:49:06 by asulon          #+#    #+#               #
#  Updated: 2026/04/21 06:49:43 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy


def main() -> None:
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print("Testing lead to gold: "
          f"{alchemy.lead_to_gold()}")


if __name__ == "__main__":
    main()
