##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex07
##

"""
------------------------------- TO DO ------------------------------------------

The goal of this exercice is to make the followings classes:

- Weapon (an absctract class)
- Sword (inheriting from Weapon)
- Bow (inheriting from Weapon)

The class Weapon should respect the following things:
- Name's class property should be "Weapon"
- A constructor with 2 parameters: name and damage.
- The attributes name, damage and range.
- range attribute should be set to "Melee".
- A classmethod "getClassName" which return the name's class.
- A method "attack" which return damage's attribute.
- A method "isMelee" which return a boolean.
- A method "isRange" which return a boolean.

The class Sword should respect the following things:
- Name's class property should be "Sword"
- Inherit from Weapon.
- A method "slash" which return damage's attribute * 2 !

The class Bow should respect the following things:
- Name's class property should be "Bow"
- Inherit from Weapon.
- range's attribute should be "Range".
- A method "shoot" which return damage's attribute * 1.5 !

#Hints:
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