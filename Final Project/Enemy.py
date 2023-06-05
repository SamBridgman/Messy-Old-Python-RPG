class Enemy(object):
    #
    def __init__(self, eName, level, inventory = [], eHealth = 25, eStrength = 5, eMana = 50, eStamina = 25, eDex = 25, damage = 0):
        self.__eName = eName
        self.__level = level
        self.__eInventory = inventory
        self.__eHealth = eHealth
        self.__eStrength = eStrength
        self.__eMana = eMana
        self.__eStamina = eStamina
        self.__eDex = eDex
        self.__damage = 0

    def __str__(self):
        rep = ""
        rep += "Name: " + str(self.__eName) + "\n"
        rep += "Health: " + str(self.__eHealth)
        return rep
    def displayStats(self):
        rep = ""
        rep += str(eName) + ": " + "\n"
        rep += "Health: " + str(eHealth) + "\n"
        rep += "Weapon: " + str(eInventory[0])
    def addItem(self, item):
        self.__eInventory.append(item)
    def death(self):
        self.__eHealth <= 0
    def getInventory(self):
        return self.__eInventory
    def calculateDamage(self, newDamage):
        damage = self.__eStrength + newDamage
        return damage
    def setDamage(self, newDamage):
        self.__damage = newDamage
    def getDamage(self):
        return self.__damage
    def getHealth(self):
        return self.__eHealth
    def setHealth(self, newHealth):
        self.__eHealth = newHealth
        return self.__eHealth
    def getName(self):
        return self.__eName
    def takeDamage(self, damage, pName):
        self.__eHealth = self.__eHealth - damage
        print(self.__eName + " has taken " + str(damage) + " damage by " + pName + "!")
        return self.__eHealth
        
        
