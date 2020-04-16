##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex07
##

"""
------------------------------- TO DO ------------------------------------------

Let's create Olaf from League of Legends !

We will implement some quotes from this website:
https://leagueoflegends.fandom.com/wiki/Olaf/Quotes

Olaf is a Warrior, let's create a class Warrior which respect the following things:

- A constructor with two parameters: name and weapon.
In the constructor, the warrior say "Leave nothing behind !".

- The instance attributes name and weapon.

- A destructor which display "I'm going.".

- When you print a warrior or use the method "talk", it should print:
"name": I've got my "weapon's name".

- A static method "move" which print:
"name": "random Olaf moving quotes"

- A static method "taunt" which print:
"name": "Olaf taunt quotes"

- A static method "joke" which print:
"name": "Olaf joke quote"

- A static method "attack" which print:
"name": "random Olaf attack quotes"

#Hints: import random

#Outputs example:
Olaf: Leave nothing behind !
Olaf: I've got my Axe
Olaf: I've got my Axe
Olaf: The worth of a man can be measured by the length of his beard, and the girth of his belt buckle.
Olaf: C'mon, I won't hurt you. I promise !
Olaf: Urge to kill, rising !
Olaf: The might of Lokfar approaches !
Olaf: My axe is thirsty.
Olaf: Faster to battle !
Olaf: I'm going.
Congratulation !

--------------------------------------------------------------------------------
"""

#Code here

if __name__ == "__main__":
    try:
        olaf = Warrior("Olaf", "Axe")
        olaf.talk()
        print(olaf)
        olaf.joke()
        olaf.taunt()
        olaf.move()
        olaf.move()
        olaf.attack()
        olaf.attack()
        del olaf
    except Exception as e:
        print("Your program encountered an error.")
        print("Error:", e)
        exit(84)
    print("Congratulation !")