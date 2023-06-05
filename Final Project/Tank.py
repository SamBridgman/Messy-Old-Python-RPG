from Player import Player

class Tank(Player):
    def __init__(self, pName, pClass, pLevel = 1, inventory = [], pStrength = 100, pHealth = 175, pMana = 0, pStamina = 15, pDex = 0, money = 0, xp = 0, damage = 0):
        super().__init__(pName, pClass, pLevel, inventory, pStrength, pHealth, pMana, pStamina, pDex, money, xp, damage)

    def __str__(self):
        rep = super().__str__()
        return rep
    
