class Item(object):
    #no use
    COMMON = 1
    UNCOMMON = 1.2
    RARE = 1.4
    LEGENDARY = 1.8
    
    def __init__(self, name, iType, rarity, weight, damage = 0, worth = 0):
        self.__name = name
        self.__type = iType
        self.__rarity = rarity
        self.__damage = damage
        self.__weight = weight
        self.__worth = worth

    def __str__(self):
        rep = ""
        rep += "Name: " + str(self.__name) + "\n"
        rep += "Type: " + str(self.__type) + "\n"
        rep += "Rarity: " + str(self.__rarity) + "\n"
        rep += "Worth: " + str(self.__worth)
        return rep
    def getName(self):
        return self.__name
    def getItemDamage(self):
        return self.__damage
    def getWorth(self):
        return self.__worth
    def getType(self):
        return self.__type
    #generates worth for items, updates item worth
    def generateWorth(self):
        if self.__rarity == "COMMON":
            self.__worth = round(self.__worth * 1)
            return self.__worth
        if self.__rarity == "UNCOMMON":
            self.__worth = round(self.__worth * 1.5)
            return self.__worth
        if self.__rarity == "RARE":
            self.__worth = round(self.__worth * 3)
            return self.__worth
        if self.__rarity == "LEGENDARY":
            self.__worth = round(self.__worth * 4)
            return self.__worth
        
