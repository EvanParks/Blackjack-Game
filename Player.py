class player():
    def __init__(self):
        self.__playerHand = []
        self.__playerTotal = 0
        self.__playerX = 810
        self.__playerY = 800
        self.__dealerX = 810
        self.__dealerY = 80
        self.__playerAces = 0
        self.__aceLocations = []

    def addCard(self, card):
        self.__playerHand.append(card)

    def clear(self):
        self.__playerHand.clear()
        self.__playerAces = 0
        self.__playerTotal = 0
        self.__aceLocations.clear()

    def addPoints(self, value):
        self.__playerTotal += value

    def setPoints(self, value):
        self.__playerTotal = value

    def addAce(self):
        self.__playerAces += 1

    def removeAce(self):
        self.__playerAces -= 1

    def setAces(self, value):
        self.__playerAces = value

    def addAceLocation(self, value):
        self.__aceLocations.append(value)

    def getAceLocations(self):
        return self.__aceLocations

    def getAces(self):
        return self.__playerAces

    def getHand(self):
        return self.__playerHand

    def getTotal(self):
        return self.__playerTotal

    def getPlayerX(self):
        return self.__playerX

    def getPlayerY(self):
        return self.__playerY

    def getDealerX(self):
        return self.__dealerX

    def getDealerY(self):
        return self.__dealerY

