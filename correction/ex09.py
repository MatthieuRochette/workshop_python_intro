##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex08
##

class Weapon():
    name = "Weapon"

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    @classmethod
    def getClassName(cls):
        return cls.__name__

class Sword(Weapon):
    name = "Sword"

    def __init__(self, name, damage):
        Weapon.__init__(self, name, damage)

class Scepter(Weapon):
    name = "Scepter"

    def __init__(self, name, damage):
        Weapon.__init__(self, name, damage)

class Entity():
    name = "Entity"

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.weapon = None
        print("{} join the summoner's rift !".format(self.name))

    def __repr__(self):
        return "{}: {} hp".format(self.name, self.hp)

    @classmethod
    def getClassName(cls):
        return cls.__name__

    def isAlive(self):
        return self.hp >= 0

    def hit(self, damage):
        self.hp -= damage
        return

    def equip(self, weapon):
        if self.getClassName() == "Warrior" and weapon.getClassName() != "Sword":
            print("{} cannot fight with a {}, he is a {} !".format(self.name, weapon.getClassName(), self.getClassName()))
            return False
        elif self.getClassName() == "Mage" and weapon.getClassName() != "Scepter":
            print("{} cannot fight with a {}, he is a {} !".format(self.name, weapon.getClassName(), self.getClassName()))
            return False
        elif self.weapon:
            print("{} has already a weapon equipped !".format(self.name))
            return False
        self.weapon = weapon
        return True

    def unequip(self):
        if self.weapon:
            print("{} unequiped {} !".format(self.name, self.weapon.name))
            self.weapon = None
            return True
        print("{} don't have weapon equiped !".format(self.name))
        return False

class Warrior(Entity):
    name = "Warrior"

    def __init__(self, name, hp, strength):
        Entity.__init__(self, name, hp)
        self.strength = strength

    def attack(self, target):
        if issubclass(type(target), Entity) == False:
            print("{} attack an invalid target !".format(self.name))
            return False
        if self.weapon == None:
            target.hit(self.strength)
        else:
            target.hit(self.weapon.damage + self.strength)
        print("{} attacked {} !".format(self.name, target.name))
        return True

class Mage(Entity):
    name = "Mage"

    def __init__(self, name, hp, power):
        Entity.__init__(self, name, hp)
        self.power = power

    def attack(self, target):
        if issubclass(type(target), Entity) == False:
            print("{} attack an invalid target !".format(self.name))
            return False
        if self.weapon:
            target.hit(self.weapon.damage + self.power)
            print("{} attacked {} !".format(self.name, target.name))
            return True
        print("{} cannot attack without a Scepter !".format(self.name))
        return False


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