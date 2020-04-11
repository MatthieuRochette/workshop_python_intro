##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex06
##

"""
------------------------------- TO DO ------------------------------------------

Let's create a class Warrior !

In its constructor, you must provide a name, health points and a weapon name.

A Warrior can introduce itself with the method "talk" or when you print it.

--------------------------------------------------------------------------------
"""

#Code here


if __name__ == "__main__":
    try:
        salucromu = Warrior("salucromu", 100, "laptop")
        salucromu.talk()
        print(salucromu)
    except Exception as e:
        print("Your program encountered an error.")
        print("Error:", e)
        exit(84)
    print("Congratulation !")