##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex06
##

class Warrior():
    def __init__(self, name, hp, weapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def __repr__(self):
        return "My name is {}, I have {} hp and my weapon is '{}'".format(self.name, self.hp, self.weapon)

    def talk(self):
        print("My name is {}, I have {} hp and my weapon is '{}'".format(self.name, self.hp, self.weapon))

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