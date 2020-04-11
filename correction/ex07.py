##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex07
##

class Weapon():
    name = "Weapon"
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        self.range = "Melee"

    @classmethod
    def getClassName(cls):
        return cls.__name__

    def attack(self):
        return self.damage

    def isMelee(self):
        return self.range == "Melee"

    def isRange(self):
        return self.range == "Range"

class Sword(Weapon):
    name = "Sword"
    def __init__(self, name, damage):
        Weapon.__init__(self, name, damage)

    def slash(self):
        return self.damage * 2

class Bow(Weapon):
    name = "Bow"
    def __init__(self, name, damage):
        Weapon.__init__(self, name, damage)
        self.range = "Range"

    def shoot(self):
        return self.damage * 1.5

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