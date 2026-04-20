# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_3.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/20 17:55:48 by asulon          #+#    #+#               #
#  Updated: 2026/04/20 18:05:42 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using"
          "'from ... import ...' structure")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
