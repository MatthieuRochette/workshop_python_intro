##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex09
##

"""
------------------------------- TO DO ------------------------------------------

Welcome to summoner's rift !

The goal of this exercice is to make Master Yi and Veigar fight !

You must implement the following classes:
    - Weapon (designates a generic weapon)
    - Sword (specific weapon)
    - Scepter (specific weapon)
    - Entity (designates a generic entity)
    - Warrior (specific entity)
    - Mage (specific entity)

The class Weapon should respect the following things:
    - Have a name class attribute, "Weapon".
    - A constructor with 2 parameters: weapon's name and damage.
    - The instance attributes name and damage.
    - A classmethod "getClassName" which returns the class' name.

The class Sword should respect the following things:
    - Inherit from Weapon.
    - Have a name class attribute, "Sword".
    - A constructor with 2 parameters: weapon's name and damage.

The class Scepter should respect the following things:
    - Inherit from Weapon.
    - Have a name class attribute, "Scepter".
    - A constructor with 2 parameters: weapon's name and damage.

The class Entity should respect the following things:
    - Have a name class attribute, "Entity".
    - A constructor with 2 parameters: name and hp.
    - The instance attributes name, hp and weapon.
    - When the instance is created, Weapon = None.
    - A classmethod "getClassName" which returns the class' name.
    - A method "isAlive" which returns True if the entity don't have hp, False otherwise.
    - A method "hit" which take as parameter the amount of hp he will lose.
    - A method "equip" which take as parameter a weapon.

It returns a boolean representing if the entity can equip it or not.

!! A Warrior can only equip a Sword and a Mage can only equip a Scepter !!

    - A method "unequip" which remove the Entity' Weapon.

The class Warrior should respect the following things:
    - Have a name class attribute, "Warrior".
    - A constructor with 3 parameters: name, hp and strength.
    - A method "attack" which take as parameter a target.

It returns True if the attack succeed, False otherwise.
If the target is not an instance inherited from Entity, the attack miss !

The class Mage should respect the following things:

- Have a name class attribute, "Mage".

- A constructor with 3 parameters: name, hp and power.

- A method "attack" which take as parameter a target.
It returns True if the attack succeed, False otherwise.
He cannot attack the target if he don't have weapon equipped !
If the target is not an instance inherited from Entity, the attack miss !

#Output:

##############################
#Welcome to summoner's rift !#
##############################

Master Yi join the summoner's rift !
Veigar join the summoner's rift !
Master Yi cannot fight with a Scepter, he is a Warrior !
Veigar cannot fight with a Sword, he is a Mage !
Veigar cannot attack without a Scepter !
Master Yi attack an invalid target !
Veigar attack an invalid target !
Master Yi attacked Veigar !
Veigar attacked Master Yi !
Master Yi attacked Veigar !
Veigar attacked Master Yi !
Master Yi: -120 hp
Veigar: 660 hp
Master Yi has been slain.
Congratulation !

#Hints:

Take a look at these functions:
- issubclass()
- type()

Spend some time reading the outputs expected and the main provided !

--------------------------------------------------------------------------------
"""

#Write your code hereunder

if __name__ == "__main__":
    try:
        print("##############################")
        print("#Welcome to summoner's rift !#")
        print("##############################\n")
        master_yi = Warrior("Master Yi", 1000, 80)
        wits_end = Sword("Wit's End", 40)
        veigar = Mage("Veigar", 900, 500)
        void_staff = Scepter("Void Staff", 60)
        master_yi.equip(void_staff)
        veigar.equip(wits_end)
        if master_yi.weapon or veigar.weapon:
            raise Exception("Invalid while equipping wrong weapons !")
        master_yi.equip(wits_end)
        veigar.attack(master_yi)
        veigar.equip(void_staff)
        if master_yi.weapon.name != "Wit's End" or veigar.weapon.name != "Void Staff":
            raise Exception("Invalid while equipping a valid weapon !")
        elif master_yi.attack("dommage") or veigar.attack("fromage"):
            raise Exception("Invalid while attacking an invalid target !")
        elif master_yi.attack(veigar) == False or veigar.hp != 780:
            raise Exception("Invalid while Master Yi attacked Veigar !")
        elif veigar.attack(master_yi) == False or master_yi.hp != 440:
            raise Exception("Invalid while veigar attacked Master Yi !")
        while master_yi.isAlive() and veigar.isAlive():
            master_yi.attack(veigar)
            veigar.attack(master_yi)
            print(master_yi)
            print(veigar)
        if master_yi.isAlive():
            print("Veigar has been slain.")
        else:
            print("Master Yi has been slain.")
    except Exception as e:
        print("Your program encountered an error.")
        print("Error:", e)
        exit(84)
    print("Congratulation !")