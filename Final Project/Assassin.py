from Player import Player

class Assassin(Player):
    def __init__(self, pName, pClass = "Assassin", pLevel = 1, inventory = [], pStrength = 25, pHealth = 75, pMana = 20, pStamina = 125, pDex = 100, money = 0, xp = 0, damage = 0):
        super().__init__(pName, pClass, pLevel, inventory, pStrength, pHealth, pMana, pStamina, pDex, money, xp, damage)
    def __str__(self):
        rep = super().__str__()
        return rep
    
