# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_4.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/20 18:05:55 by asulon          #+#    #+#               #
#  Updated: 2026/04/20 18:14:15 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        print("Testing the hidden create_earth:"
              f"{alchemy.create_earth()}")
    except ImportError as error:
        print(error)


if __name__ == "__main__":
    main()
