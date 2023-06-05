from Item import Item

class Player(object):


    def __init__(self, pName, pClass, pLevel, inventory, pStrength, pHealth, pMana, pStamina, pDex, money = 0, xp = 0, damage = 0):
        self.__pName = pName
        self.__pClass = pClass
        self.__pLevel = pLevel
        self.__inventory = inventory
        self.__pStrength = pStrength
        self.__pHealth = pHealth
        self.__pMana = pMana
        self.__pStamina = pStamina
        self.__pDex = pDex
        self.__money = money
        self.__xp = xp
        self.__damage = damage

    def __str__(self):
        rep = ""
        rep += "Name: " + str(self.__pName) + "\n"
        rep += "Level: " + str(self.__pLevel) + "\n"
        rep += "Class: " + str(self.__pClass)
        return rep
    
    def addItem(self, item):
        self.__inventory.append(item)
    
    def death(self):
        self.__pHealth <= 0
    def calculateDamage(self, newDamage): #damage
        damage = int(self.__pStrength) + int(newDamage)
        return damage
    #getters & setters
    def getMoney(self):
        return self.__money
    def addMoney(self, money):
        self.__money += money
        return self.__money
    def setMoney(self, newMoney):
        self.__money = newMoney
    def getLevel(self):
        return self.__level
    def setLevel(self, newLevel):
        self.__level = newLevel
        return self.__level
    def getXP(self):
        return self.__xp
    def setXP(self, xp):
        self.__xp = self.__xp + xp
    def getHealth(self):
        return self.__pHealth
    def setHealth(self, newHealth):
        self.__pHealth = newHealth
    def setMana(self, newMana):
        self.__pMana = newMana
    def getMana(self):
        return self.__pMana
    def setStamina(self, newStamina):
        self.__pStamina = newStamina
    def getStamina(self):
        return self.__pStamina
    def setDex(self, newDex):
        self.__pDex = newDex
    def getDex(self):
        return self.__pDex
    def setStrength(self, newStrength):
        self.__pStrength = newStrength
    def getStrength(self):
        return self.__pStrength
    def getName(self):
        return self.__pName
    def setName(self, newName):
        self.__pName = newName
        return self.__pName
    def getInventory(self):
        return self.__inventory
    def setInventory(self, newInv):
        self.__inventory = newInv
    def setDamage(self, newDamage):
        self.__damage = newDamage
    def getDamage(self):
        return self.__damage
    def getClass(self):
    	return self.__pClass
    def getStats(self):
        rep = ""
        rep += "Health: " + str(round(self.__pHealth)) + "\n"
        rep += "Stamina: " + str(round(self.__pStamina)) + "\n"
        rep += "Strength: " + str(round(self.__pStrength)) + "\n"
        rep += "Mana: " + str(round(self.__pMana)) + "\n"
        rep += "Dex: " + str(round(self.__pDex))
        return rep
    def takeDamage(self, damage, eName): 
        self.__pHealth = self.__pHealth - damage
        print(self.__pName + " has taken " + str(damage) + " damage by " + eName + "!")
        return self.__pHealth
    #this is level up system, since you can only gain xp by 15, i just made it so every 30xp points you level up
    def levelUp(self):
        PERM = 1.2
        self.__pLevel += 1
        self.__pStrength = self.__pStrength * PERM
        round(self.__pStrength)
        self.__pHealth = self.__pHealth * PERM
        round(self.__pHealth)
        self.__pMana = self.__pMana * PERM
        round(self.__pMana)
        self.__pStamina = self.__pStamina * PERM
        round(self.__pStamina)
        self.__pDex = self.__pDex * PERM
        round(self.__pDex)
        return self.__pDex, self.__pStamina, self.__pStrength, self.__pHealth, self.__pMana
    #this is where things got sligtly wonky,
    #I had a hard time figuring out why somethings worked with playersList[0](player) and not player obj
    #which explains why things got back and fourth, but it works!
    def displayInventory(self, playerInventory):
        count = 0
        for i in playerInventory:
            count += 1
            print(str(count) +  ": ", i)
    def purchaseItem(self, Item, playerInventory):
        if self.__money > Item.getWorth():
            self.__money -= int(Item.getWorth())
            playerInventory.append(Item)
            print("Item Purchased.")
        else:
            print("You do not have enough money")
    def sellItem(self, shopkeeperinv, playerInventory, sellChoice):
        self.__money += playerInventory[sellChoice].getWorth()
        print("You sold", playerInventory[sellChoice].getName(), "for", playerInventory[sellChoice].getWorth(), "dollars!")
        del playerInventory[sellChoice]
        return shopkeeperinv
    def gainXP(self, xp, levelNotif):
        self.__xp = self.__xp + xp
        print("You have gained,", xp, "xp!")
        #XP TIER SYSTEM
        if self.__xp == 30: #1
            self.levelUp()
            print(levelNotif)
        elif self.__xp == 60:#2
            self.levelUp()
            print(levelNotif)
        elif self.__xp == 90:#3
            self.levelUp()
            print(levelNotif)
        elif self.__xp == 120:#4
            self.levelUp()
            print(levelNotif)
        elif self.__xp == 150:#5
            self.levelUp()
            print(levelNotif)
        elif self.__xp == 180:#6
            self.levelUp()
            print(levelNotif)
        elif self.__xp == 210:#7
            self.levelUp()
            print(levelNotif)
    def usePotion(self, potion):
        self.__pHealth += 50
        print("Potion Used.")

            
    
        
        
    
            
        
        
        
            
"""    
    def takeDamage(self, damage, eName):
        self.__pHealth -= damage
        return pName + "has taken " + damage + " damage by" + eName + "!"
"""

        
        
        


    
    
