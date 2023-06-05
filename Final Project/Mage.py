from Player import Player

class Mage(Player):
    def __init__(self, pName, pClass = "Mage", pLevel = 1, inventory = [], pStrength = 5, pHealth = 75, pMana = 100, pStamina = 35, pDex = 10, money = 0, xp = 0, damage = 0):
        super().__init__(pName, pClass, pLevel, inventory, pStrength, pHealth, pMana, pStamina, pDex, money, xp, damage)

    def __str__(self):
        rep = super().__str__()
        return rep
    
