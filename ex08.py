##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex08
##

"""
------------------------------- TO DO ------------------------------------------

The goal of this exercice is to make the following classes:

- Weapon (designates a generic weapon)
- Sword (specific weapon)
- Bow (specific weapon)

The class Weapon should respect the following things:
    - Have a name class attribute, "Weapon"
    - A constructor with 2 parameters: weapon's name and damage.
    - The instance attributes name, damage and range.
    - range attribute should be set to "Melee".
    - A classmethod "getClassName" which returns the class' name.
    - A method "attack" which returns the damage attribute.
    - A method "isMelee" which returns a boolean.
    - A method "isRange" which returns a boolean.

The class Sword should respect the following things:
    - Inherit from Weapon.
    - Class' name attribute should be "Sword"
    - A method "slash" which returns damage attribute times 2 !

The class Bow should respect the following things:
    - Inherit from Weapon.
    - Class' name attribute should be "Bow"
    - range attribute should be "Range".
    - A method "shoot" which returns damage attribute times 1.5 !

Hints:
    - Spend some time in order to understand the main provided !
    - Google is your best friend.
    - @classmethod

--------------------------------------------------------------------------------
"""

#Write your code hereunder

if __name__ == "__main__":
    try:
        weapon = Weapon("weapon", 42)
        sword = Sword("sword", 42)
        bow = Bow("bow", 42)
        if weapon.getClassName() != "Weapon" or sword.getClassName() != "Sword" or bow.getClassName() != "Bow":
            raise Exception("Invalid getCLassName method(s).")
        elif weapon.isMelee() != True or sword.isMelee() != True or bow.isMelee() != False:
            raise Exception("Invalid isMelee method(s).")
        elif weapon.isRange() != False or sword.isRange() != False or bow.isRange() != True:
            raise Exception("Invalid isRange method(s).")
        elif weapon.attack() != 42 or sword.slash() != 42 * 2 or bow.shoot() != 42 * 1.5:
            raise Exception("Invalid attack method(s)")
    except Exception as e:
        print("Your program encountered an error.")
        print("Error:", e)
        exit(84)
    print("Congratulation !")