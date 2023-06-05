from Player import Player

class Knight(Player):
    def __init__(self, pName, pClass = "Knight", pLevel = 1, inventory = [], pStrength = 40, pHealth = 100, pMana = 0, pStamina = 50, pDex = 10, money = 0, xp = 0, damage = 0):
        super().__init__(pName, pClass, pLevel, inventory, pStrength, pHealth, pMana, pStamina, pDex, money, xp, damage)

    def __str__(self):
        rep = super().__str__()
        return rep
    
