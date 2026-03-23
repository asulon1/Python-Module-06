# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_sacred_scroll.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/23 15:02:48 by asulon          #+#    #+#               #
#  Updated: 2026/03/23 18:02:07 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy


def main():
    print("=== Sacred Scroll Mastery ===\n")
    try:
        print("Testing direct module access:")
        print(
            f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
        print(
            f"alchemy.elements.create_fire(): {alchemy.elements.create_water()}")
        print(
            f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
        print(
            f"alchemy.elements.create_air(): {alchemy.elements.create_air()}\n")
    except AttributeError as error:
        print(f"Error: While create elements : {error.name}")

    print("Testing package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed\n")

    print("Package metadata")
    print(f"Version : {alchemy.__version__}")
    print(f"Author : {alchemy.__author__}")


if __name__ == "__main__":
    main()
