#Sam Bridgman
#Prof. Jon Ventulett
# Final Project
# May 15 2022

#SOME NOTES:
#From my own self fault, I focused more time on other features than the atributes themselves,
#that in turn led to only the main character traits, strength and health mattering.. which leads to major power inbalances between classes (Tank OP)
#Also, weight attribute in the objs dont do anything, did not have time to work on it,

#when you start game and play the intro, it restarts, so you have to run it again,if this note is here then i did not figure it out
#my guess was that the time.sleep made it restart?

#I intentionally made the game pretty easy so it does not go over the 10 minute mark, which also is why I made the intro optional :)

#when it came to the shop, it says 1) potion because I intended to have armour and weapons to buy aswell, did not have time to do it

import time
import random
import pickle
from Player import Player
from Item import Item
from Enemy import Enemy
from Knight import Knight
from Mage import Mage
from Assassin import Assassin
from Tank import Tank
from Map import Map

border = "--------------------------------------"

#item raritys
COMMON = 1
UNCOMMON = 1.2
RARE = 1.4
LEGENDARY = 1.8


#for level up
levelNotif = """
|-----------------------|
|                       |
|    YOU LEVELED UP     |
|                       |
|-----------------------|
"""


#MAP N MENU
gameMap = Map(10, "-")
gameMap.setPlayerPos(0,1)
gameMap.add(0,0,"S")
idleMenu = """
-----------------------------
1. Inventory 2. Move 3. Save 4. Load
-----------------------------
"""


#shopkeeper stuff
shopkeeperNPCINV = []
healthPotion = Item("Health Potion", "potion", "COMMON", 1, 0, 10)
shopkeeperNPCINV.append(healthPotion)
for i in shopkeeperNPCINV:
    i.generateWorth()
#USED TO ADJUST WORTH TO RARITY
shopkeeperNPC = Player("Rob", "Shopkeeper", 1, shopkeeperNPCINV, 0, 0, 0, 0, 0)
shopMenu = """
1. Buy
2. Sell
3. Leave

"""



#its out here to make it global
playerInventory = []
playersList = []
player = Player("", "", 1, playerInventory, 50, 100, 0, 0, 0)
playerHealth = player.getHealth()

#INTRO SWORDS
commonSword = Item("Basic Sword", "Sword", "Common", 20, 5)
playerInventory.append(commonSword)
commonSword1 = Item("Basic Sword","Sword", "Common", 10, 5)


#Hadlin
hadlinInventory = []
hadlinSword = Item("Hadlin's Sword", "GreatSword", "RARE", 0, 25 )
hadlinInventory.append(hadlinSword)
hadlinNPC = Player("Hadlin", "Knight", 1, hadlinInventory, 100, 200, 50, 50, 50)
#Alexandria
alexandriaSword = Item("Alexandria's Sword", "GreatSword", "RARE", 0, 25)
alexandriaInventory = []
alexandriaInventory.append(alexandriaSword)
alexandriaNPC = Player("Alexandria", "KNIGHT", 1, alexandriaInventory, 100, 100, 50, 0, 0, 0)
#Minion 1
thaerMinionInv = []
thaerMinionInv.append(commonSword1)
thaerMinionNPC = Enemy("Thaer's Minion", 1, thaerMinionInv)
#Minion 2
thaerMinionInv2 = []
thaerMinionInv2.append(commonSword1)
thaerMinion2NPC = Enemy("Thaer's Minion", 1, thaerMinionInv2)
#Minion 3
thaerMinionInv3 = []
thaerMinionInv3.append(commonSword1)
thaerMinion3NPC = Enemy("Thaer's Minion", 1, thaerMinionInv3)


#DAMAGE CALCULATION used for intro** this was my old damage calc so now its used for the intro solely, since every fight, pdamage changes based on user stats and whats equiped
pDamage = player.calculateDamage(playerInventory[0].getItemDamage())

#IMPORTANT NPC STUFF
hadlinDamage = hadlinNPC.calculateDamage(hadlinInventory[0].getItemDamage())
#------------------------------------------------------------------------------


#GAME MENU
def gameMenu(playersList):
    print(border)
    print("MENU")
    print("""
PARTY:
""")
    #display player stats
    for i in playersList:
        print(i)
        print(i.getStats())
        print(border)
    print(idleMenu)
#def for entering shop
def enterShop(player, playersList, shopkeeperNPCINV):
    doneShop = False
    print(border)
    print("Hello! Welcome to Rob's Shop, how may I help you?")
    while doneShop == False:
        #print shop menu and player money
        playersList[0].setMoney(player.getMoney())
        print(border)
        print(shopMenu)
        print(border)
        print("Balance:",playersList[0].getMoney())
        #ask what user wants to do
        shopChoice = input("--> ")
        #for buying
        if shopChoice == "buy" or shopChoice == "1":
            print("""
1. Potions
        """)
            shopChoice = input("--> ").lower()
            if shopChoice == "potions" or shopChoice == "1":
                print(shopkeeperNPC.displayInventory(shopkeeperNPCINV))
                shopChoice = input("Pick an item to buy, leave to leave: ")
                try:
                    player.purchaseItem(shopkeeperNPCINV[int(shopChoice) - 1], playerInventory)
                    #playerInventory = player.getInventory()
                    playersList[0].setMoney(player.getMoney())
                except:
                    print("")
            else:
                print("Not a valid selection.")
        #for selling
        if shopChoice == "sell" or shopChoice == "2":
            player.displayInventory(playerInventory)
            print("------")
            print("What would you like to sell?")
            try:
                sellChoice = int(input("--> Enter Number, type leave to leave: "))
                sellChoice -= 1
                player.sellItem(shopkeeperNPCINV, playerInventory, sellChoice)
            except:
                print("")
        #leave the shop
        if shopChoice == "3" or shopChoice == "Leave":
            slowprint("You are leaving.")
            doneShop = True
def slowprint(line, delay = .01):
    import time
    for l in line:
        print(l, end="")
        time.sleep(delay)
    print()
#fight sequence used through the game
def randomFight(eList, pList, player):
    turn = True
    print("""
YOU ARE BEING ATTACKED!
""")
    encounter = 1
    #Not sure if there was better way, but what this does is that it saves player info and any other player ai and stores it before the fight
    #at the end, it loads the save file so player and ai stats reset.
    filehandler = open("fightsave","wb")
    pickle.dump(pList, filehandler)
    filehandler.close()

    while encounter == 1:
        finalBoss = False
        #checks if anyone from plist is dead
        for i in pList[1:]:
            if i.getHealth() <= 0:
                print(i.getName(), "Died!")
                pList.remove(i)
        if eList[0].getName() == "Thaer, The Great Lord":
            finalBoss = True
        for i in eList:
            if i.getHealth() <= 0:
                print(i.getName(), "Died!")
                eList.remove(i)
        if turn == True:
            if pList[0].getHealth() > 0 and len(eList) > 0:
                print("PARTY")
                print(border)
                for i in pList:
                    print(i)
                    print(i.getStats())
                    print(border)
                #players turn
                count = 1
                print("ENEMY(s)")
                print(border)
                for i in eList:
                    print(str(count) + ":", i)
                    count += 1
                print("""
1) Attack
2) Use a Potion
""")
                menuChoice = input("--> ").lower()
                if menuChoice == "1" or menuChoice == "attack":
                    player.setInventory = playerInventory
                    #damage
                    damage = pList[0].calculateDamage(playerInventory[0].getItemDamage())
                    player.setDamage(damage)
                    fightChoice = input("Who would you like to attack? ")
                    eList[int(fightChoice) - 1].takeDamage(damage, player.getName())
                    eListCount = 0
                    #checks for how many elists enemys, then calculates damage and performs damage
                    for i in eList:
                        eListCount += 1
                    for i in pList[1:]:
                        aiDamage = i.calculateDamage(i.getInventory()[0].getItemDamage())
                        playerSelect = random.randint(1, eListCount)
                        eList[playerSelect - 1].takeDamage(aiDamage, i.getName())
                    turn = False
                #use for potions
                elif menuChoice == "2" or menuChoice == "use a potion":
                    for i in playerInventory:
                        if i.getName() == "Health Potion":
                            pList[0].usePotion(i)
                            playerInventory.remove(i)
                            break
                        

                else:
                    print("Not a valid response")
            else: #ends loop
                encounter = 2
                
        #enemy ai turn
        if turn == False:
            for i in pList[1:]:
                #checks to see if anyone died
                if i.getHealth() <= 0:
                    print(i.getName(), "Died!")
                    pList.remove(i)
            for i in eList:
                if i.getHealth() <= 0:
                    print(i.getName(), "Died!")
                    eList.remove(i)
            if pList[0].getHealth() > 0 and len(eList) > 0:
                #checks to see if anyone from eList is dead
                #enemies turn
                if len(eList) > 0:
                    pListCount = 0
                    #checks how many plist players there are
                    for i in pList:
                        pListCount += 1
                    #enemy calculation and who to attack
                    for i in eList:
                        damage = i.calculateDamage(i.getInventory()[0].getItemDamage())
                        playerSelect = random.randint(1, pListCount)
                        pList[int(playerSelect) - 1].takeDamage(damage, i.getName())
                    turn = True
            else:
                encounter = 2
    #if player wins
    if pList[0].getHealth() > 0 and len(eList) <= 0:
        print("ENEMY DEFEATED")
        print("REWARDS: 50 Coins")
        filehandler = open("fightsave","rb")
        tempList = pickle.load(filehandler)
        pList[0] = tempList[0]
        #if ai died
        if len(pList) < 2:
            pList.append(tempList[1])
        else:
            pList[1] = tempList[1]
        filehandler.close()
        #add money and xp towards player
        player.addMoney(50)
        pList[0].gainXP(15, levelNotif)
        #a check to see if fight was Thaer(final boss)
        if finalBoss == True:
                print("""
-----------------------------------------------------------------------
WOW YOU WON!!!! GOODJOB, THAER'S TERROR ACROSS THE LAND IS FINISHED!
-----------------------------------------------------------------------
""")
                player.addMoney(10000)
                #time.sleep(5)
                #quit()
            
        encounter = 2 #closes loop
    #if player dies and enemy lives
    elif pList[0].getHealth() <= 0 and len(eList) > 0:
        print("You died, respawning at shop")
        #loads save file from above to reset player stats
        filehandler = open("fightsave","rb")
        tempList = pickle.load(filehandler)
        pList[0] = tempList[0]
        #if ai died
        if len(pList) < 2:
            pList.append(tempList[1])
        else:
            pList[1] = tempList[1]
        filehandler.close()
        #reset player pos
        gameMap.setPlayerPos(0,1)
        encounter = 2
    #for the rare occasion if player died and eList is empty
    elif pList[0].getHealth() <= 0 and len(eList) <= 1:
        print("You died, respawning at shop")
        filehandler = open("fightsave","rb")
        tempList = pickle.load(filehandler)
        pList[0] = tempList[0]
        if len(pList) < 2:
            pList.append(tempList[1])
        else:
            pList[1] = tempList[1]
        filehandler.close()
        gameMap.setPlayerPos(0,1)
        encounter = 2
            
                
#for the final battle with Thaer
def finalBattle(playersList, player):
    slowprint("Thaer: Ah! Welcome my minions, time for you to die.")
    #make thaer npc and sword
    ThaerSword = Item("Thaers Sword", "Sword", "LEGENDARY", 1, 100, 100)
    thaerInventory = []
    thaerInventory.append(ThaerSword)
    thaerNPC = Enemy("Thaer, The Great Lord", 1, thaerInventory, 400, 50, 25, 25, 0, 0)
    eList = []
    eList.append(thaerNPC)
    #perform fight
    randomFight(eList, playersList, player)
    
#this is used to generate encounters and perform randomfight
def generateEncounter(playersList, player):
    #for elist 1
    thaerMinionInv = []
    e1 = Enemy("Thaer Minion", 1, thaerMinionInv)
    e1.addItem(commonSword1)
    e12 = Enemy("Thaer Minion 2", 1, thaerMinionInv)
    e12.addItem(commonSword1)
    e13 = Enemy("Thaer Minion 3", 1, thaerMinionInv)
    e13.addItem(commonSword1)
    #list 2
    e2INV = []
    e2 = Enemy("Thaers Guardian", 1, e2INV, 350, 40, 25, 25, 25)
    ThaersGuardSword = Item("Thaers Guardian Sword", "Sword", "RARE", 1, 55, 30)
    e2.addItem(ThaersGuardSword)
    #chooses which enemies
    encounterChance = random.randint(1,10)
    #chance of encounter
    if encounterChance < 6:
        elistVal = random.randint(1,2)
        if elistVal == 1:
            eList = [e1,e12,e13]
            randomFight(eList, playersList, player)
        elif elistVal == 2:
            eList = [e2]
            randomFight(eList, playersList, player)
        

#game algorithm
def startGame(playersList, pName, gameMap, player):
    playerInventory.append(healthPotion)
    gameDone = False
    player.setName(pName)
    while gameDone == False:
        #player gets 10k when they beat final boss, so if your 10k and over, game over
        #I did this because true/false flags are being passed through reference so no changes would be done
        #using the player objs money as a flag works...
        if player.getMoney() >= 10000:
            gameDone = True
        else:
            print()
            #asks user what they want to do
            gameMenu(playersList)
            menuChoice = input("-->")
            #for inventory
            if menuChoice == "1":
                print("EQUIPPED")
                #this is how I equip items and unequip
                player.displayInventory(playerInventory)
                invEquipValid = False
                while invEquipValid == False:
                    print("Which item would you like to equip? if none, type none.")
                    invEquip = input("-->")
                    if invEquip == "none":
                        invEquipValid = True
                        print()
                    else:
                        try:
                            #how this works is that in inv list, pos 0 is the equiped item, so when you want to equip an item, it deletes the item, and reinserts to pos 0
                            tempVal = playerInventory[int(invEquip) - 1]
                            del playerInventory[int(invEquip) - 1]
                            playerInventory.insert(0,tempVal)
                            slowprint("Weapon Equipped")
                            invEquipValid = True
                        except:
                            print("Not a valid weapon")
                         
            #used if player wants to go to shop or move on the map
            if menuChoice == "2":
                print("""
    1) Move
    2) Go to Shop
    """)
                menuChoice = input("-->").lower()
                if menuChoice == "1" or menuChoice == "move":
                    #WHERE MAP MOVEMENT HAPPENS
                        print(border)
                        print(gameMap.display())
                        print(border)
                        direction = input("Where would you like to move? ex) up, down, left, right (type leave to leave): ")
                        if direction != "leave":
                            slowprint("Traveling to location...")
                            #if player at row 9 and they move down, thaer boss battle starts
                            if gameMap.getPlayerRow() == 9 and direction == "down":
                                print("Entering Thaer's Castle")
                                finalBattle(playersList, player)
                            else:
                                #normal map movement
                                gameMap.move(direction)
                                generateEncounter(playersList, player)
                            
                        else:
                            slowprint("Exiting...")
                #used when player goes to shop
                elif menuChoice == "2" or menuChoice =="go to shop":
                    slowprint("Traveling to The Shop....")
                    #calls enter shop 
                    enterShop(player, playersList, shopkeeperNPCINV)
                else:
                    print("Not a valid choice.")
            #for saving
            if menuChoice == "3":
                with open('savefile.dat', 'wb') as f:
                    pickle.dump([playersList, gameMap, player], f)
                print("Saved")
            #for loading
            if menuChoice == "4":
                with open('savefile.dat', 'rb') as f:
                    playersList, gameMap, player = pickle.load(f)
                print("Loaded")
        

def main(player):
    fullGameDone = False
    while fullGameDone == False:
        #prompts user if they want to skip intro, mostly benefits me so I dont have to go through it everytime :)
        skipIntro = input("Would you like to skip the intro? y/n ").lower()
        if skipIntro == "n":
            slowprint("Hadlin: Hey! wake up! they're almost through the baricade!")
            #time.sleep(1)
            slowprint("Hadlin: Thaer's men have pillaged the city, and he is going for the king!")
            #time.sleep(1)
            slowprint("Hadlin: I went searching through the city to find survivors and that's when I found you.")
            #time.sleep(1)
            slowprint("Hadlin: What is your name son?")
            
            
            pName = input("--> ")
            
            slowprint("Hadlin: Well, " + pName + ", pleasure to meet you but we must save the pleasantries until we escape this mess.")
            slowprint("Hadlin: Here, take this sword and help bring down the siege!")
            print("Basic Sword Equppied")

            
            #INRODUCTION FIGHT

            
            slowprint("Hadlin: They've broken in! " + pName + ", prepare to defend!")

            #Turn
            pTurn = True

            
            while int(thaerMinionNPC.getHealth()) != 0 and int(thaerMinion2NPC.getHealth()) != 0 and int(thaerMinion2NPC.getHealth()) != 0:
                if pTurn == True:
                    hadlinHealth = hadlinNPC.getHealth()
                    print("-----------------------------------")
                    #players turn

                    #so health values do not go negative
                    if thaerMinionNPC.getHealth() < 0:
                        thaerMinionNPC.setHealth(0)
                    if thaerMinion2NPC.getHealth() < 0:
                        thaerMinion2NPC.setHealth(0)
                    if thaerMinion3NPC.getHealth() < 0:
                        thaerMinion3NPC.setHealth(0)
                    #intro fight menu
                    print("Who would you like to attack")
                    print()
                    print("1.", thaerMinionNPC), "\n"
                    print("2.", thaerMinion2NPC), "\n"
                    print("3.", thaerMinion3NPC), "\n"
                    print("---------------------------")
                    print("Your Health:", playerHealth)
                    print("Hadlin's Health", hadlinHealth)
                    print("---------------------------")


                    choice = input("-->")
                    #Players turn
                    if choice == "1":
                        thaerMinionNPC.takeDamage(pDamage, player.getName())
                        
                    elif choice == "2":
                        thaerMinion2NPC.takeDamage(pDamage, player.getName())
                    elif choice == "3":
                        thaerMinion3NPC.takeDamage(pDamage, player.getName())
                    else:
                        print("Not a valid target.")

                    #hadlins turn
                    print("Hadlin Attacks!")
                    if thaerMinionNPC.getHealth() > 0:
                        thaerMinionNPC.takeDamage(hadlinDamage, hadlinNPC.getName())
                    elif thaerMinion2NPC.getHealth() > 0:
                        thaerMinion2NPC.takeDamage(hadlinDamage, hadlinNPC.getName())
                    else:
                        thaerMinion3NPC.takeDamage(hadlinDamage, hadlinNPC.getName())          
                    
                    pTurn = False
                else:#MINIONS FIGHT
                    print("-----------------------------------")
                    print("Thaers Minions Attack!")
                    #Thaer Minion damage
                    thaerMinionDamage = thaerMinionNPC.calculateDamage(hadlinInventory[0].getItemDamage())
                    enemyHealth1 = thaerMinionNPC.getHealth()
                    enemyHealth2 = thaerMinion2NPC.getHealth()
                    enemyHealth3 = thaerMinion3NPC.getHealth()
                    if thaerMinionNPC.getHealth() > 0:
                        e1Choice = random.randint(1,2)
                        if e1Choice == "1":
                            player.takeDamage(thaerMinionDamage, thaerMinionNPC.getName())
                        else:
                            hadlinNPC.takeDamage(thaerMinionDamage, thaerMinionNPC.getName())
                    if thaerMinion2NPC.getHealth() > 0:
                        e1Choice = random.randint(1,2)
                        if e1Choice == "1":
                            player.takeDamage(thaerMinionDamage, thaerMinionNPC.getName())
                        else:
                            hadlinNPC.takeDamage(thaerMinionDamage, thaerMinionNPC.getName())
                    if thaerMinion3NPC.getHealth() > 0:
                        e1Choice = random.randint(1,2)
                        if e1Choice == "1":
                            player.takeDamage(thaerMinionDamage, thaerMinionNPC.getName())
                        else:
                            hadlinNPC.takeDamage(thaerMinionDamage, thaerMinionNPC.getName())
                    pTurn = True
            #---------------------------------------
            print("----------------------------------------------------------")
            slowprint("Hadlin: hmph, where'd you learn to fight like that eh?")
            print("""
            1. My parents taught me how to fight from a young age.
            2. No idea, I have never held a sword before.
            3. I am a demi-god.

                """)
            #dialouge
            introDioChoice = input("-->")
            if introDioChoice == "1":
                print(pName + ": My parents taught me how to fight from a young age.")
                slowprint("Hadlin: Ah! twas only right to teach a child how to fight in times like these.")
            if introDioChoice == "2":
                print(pName + ": No idea, I have never held a sword before.")
                slowprint("Hadlin: Hmm.. beginners luck I suppose.")
            if introDioChoice == "3":
                print(pName + ": I am a demi-god.")
                slowprint("Hadlin: What.")
            slowprint("Hadlin: Anways, well, this is only the beginning")
            slowprint("Hadlin: Please, you must help take the fight against Thaer, if he wins, the world will crumble.")
            slowprint("Hadlin: Here take this key, and go to the armory to restock, you have a long ways to go. ")
            
            #5time.sleep(2)

                
            title = """                                                                                                                                                                                                                                                                                                                                            
         ____    _    ____ ____  _____ ____     ____ ___  __  __ __  __    _    _   _ ____  
        / ___|  / \  / ___|  _ \| ____|  _ \   / ___/ _ \|  \/  |  \/  |  / \  | \ | |  _ \ 
        \___ \ / _ \| |   | |_) |  _| | | | | | |  | | | | |\/| | |\/| | / _ \ |  \| | | | |
         ___) / ___ | |___|  _ <| |___| |_| | | |__| |_| | |  | | |  | |/ ___ \| |\  | |_| |
        |____/_/   \_\____|_| \_|_____|____/   \____\___/|_|  |_|_|  |_/_/   \_|_| \_|____/
        """
                                                                                                                                                                                                                                                                                                                                      
            print(title)

                            
            slowprint("You enter the armory and find four sets of pieces, Knight, Mage, Assassin, Tank")
            #it deletes player from intro so it can be reinstating to the users class.
            del player

        #END OF INTRO-------------------------------------------------------------------------------------------------
        else:
            pName = input("What is your name? ")
            print("Intro skipped.")
        #char selection

        #show user the menu and stats for each type of player
        classMenu = """
    --------------------------------------
        KNIGHT:
        Health: 100
        Stamina: 50
        Strength: 40
        Mana: 0
        Dexerity: 10

        MAGE:
        Health: 75
        Stamina: 35
        Strength: 5
        Mana: 100
        Dexerity: 10

        ASSASSIN:
        Health: 75
        Stamina: 125
        Strength: 25
        Mana: 20
        Dexerity: 100

        TANK:
        Health: 175
        Stamina: 15
        Strength: 100
        Mana: 0
        Dexerity: 0
    --------------------------------------


    """

        print(classMenu)
        
        #user selects type
        del playerInventory[0]
        classChoiceValid = False
        while classChoiceValid == False:
            classChoice = input("Select Class --> ").upper()
            #knight
            if classChoice == "KNIGHT":
                player = Knight(pName, "KNIGHT")
                knightSword = Item("Knight Sword", "Sword", "COMMON", 10, 50, 20)
                knightSword.generateWorth()
                playerInventory.append(knightSword)
                classChoiceValid = True
            #mage
            elif classChoice == "MAGE":
                player = Mage(pName, "MAGE")
                mageStaff = Item("Mage Staff", "Staff", "COMMON", 10, 50, 20)
                mageStaff.generateWorth()
                playerInventory.append(mageStaff)
                classChoiceValid = True
            #assassin
            elif classChoice == "ASSASSIN":
                player = Assassin(pName, "ASSASSIN")
                assassinDagger = Item("Assassin Dagger", "Dagger", "COMMON", 10, 50, 20)
                assassinDagger.generateWorth()
                playerInventory.append(assassinDagger)
                classChoiceValid = True
            #tank
            elif classChoice == "TANK":
                player = Tank(pName, "TANK")
                tankLongSword = Item("Tank Long-Sword", "Long-Sword", "COMMON", 10, 50, 20)
                tankLongSword.generateWorth()
                playerInventory.append(tankLongSword)
                classChoiceValid = True
            else:
                print("Not a valid class, you have to type out the class name.")
        #after user selects type, present a menu that lets the user adjust the set points for each attribute, give them 25 points to attribute to any type
        playersList.append(player)
        charPoints = 25
        pointSelect = True
        #where user selects where they want char points to go to
        while pointSelect:
            print(border)
            print(player.getStats())
            print(border)
            print("You have " + str(charPoints) + " points left.")
            print("Select an attribute to add points to.")
            print("Type done when finished")
            charPointSelect = input("--> ").lower()
            if charPoints > 0:
                #for mana
                if charPointSelect == "mana":
                    charPointSelect = int(input("points towards Mana --> "))
                    if charPointSelect <= charPoints and charPointSelect > 0:
                        tempValue = int(player.getMana()) + int(charPointSelect)
                        player.setMana(tempValue)
                        print("Stat Updated")
                        charPoints -= charPointSelect
                    else:
                        print("Not valid amount of points.")
                #for health
                elif charPointSelect == "health":
                    charPointSelect = int(input("points towards Health --> "))
                    if charPointSelect <= charPoints and charPointSelect > 0:
                        tempValue = int(player.getHealth()) + int(charPointSelect)
                        player.setHealth(tempValue)
                        print("Stat Updated")
                        charPoints -= charPointSelect
                    else:
                        print("Not valid amount of points.")
                #for stamina
                elif charPointSelect == "stamina":
                    charPointSelect = int(input("points towards Stamina --> "))
                    if charPointSelect <= charPoints and charPointSelect > 0:
                        tempValue = int(player.getStamina()) + int(charPointSelect)
                        player.setStamina(tempValue)
                        print("Stat Updated")
                        charPoints -= charPointSelect
                    else:
                        print("Not valid amount of points.")
                #for dex
                elif charPointSelect == "dex":
                    charPointSelect = int(input("points towards Dexerity --> "))
                    if charPointSelect <= charPoints and charPointSelect > 0:
                        tempValue = int(player.getDex()) + int(charPointSelect)
                        player.setDex(tempValue)
                        print("Stat Updated")
                        charPoints -= charPointSelect
                    else:
                        print("Not valid amount of points.")
                #for strength
                elif charPointSelect == "strength":
                    charPointSelect = int(input("points towards Strength --> "))
                    if charPointSelect <= charPoints and charPointSelect > 0:
                        tempValue = int(player.getStrength()) + int(charPointSelect)
                        player.setStrength(tempValue)
                        print("Stat Updated")
                        charPoints -= charPointSelect
                    else:
                        print("Not valid amount of points.")
                else:
                    print("Not an attribute.")
            if charPoints == 0:
                pointSelect = False
            if charPointSelect == "done":
                pointSelect = False

            #ENd OF CHAR SELECTION -------------------------------------------------------
        print(border)
        slowprint("You run out of the destroyed city and into the woods, after hours of traveling, you stumble upon a shop keeper tavern, you find a women in battle gear.")
        slowprint("Alexandria: You were in the captial weren't you?")
        print("""
        1. Yes, I am on the hunt to find Thaer and kill me before he takes out the king, you must help me [Strength 30].
        2. Yes, care to join me?

            """)
        #this is the dialouge for when alexandria is introduced and added to playerlist
        dioChoice = input("-->")
        if dioChoice == "1":
            if player.getStrength() >= 30:
                slowprint("Alexandria: Awesome! care if I join?.")
                slowprint("Alexandria has joined your party")
                player.gainXP(15, levelNotif)
                playersList.append(alexandriaNPC)
            else:
                slowprint("Action failed.")
                slowprint("Alexandria: Wow, good luck with that.")
        if dioChoice == "2":
            slowprint("Alexandria: Yes, I suppose.")
            playersList.append(alexandriaNPC)
            slowprint("Alexandria has joined your party")
        slowprint("You begin your journey.")

        #STARTS GAME------------
        startGame(playersList, pName, gameMap, player)
        fullGameDone = True
            
            
            
        
        
    
    
        
    
    
    
    


main(player)

