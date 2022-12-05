import pygame
import Card
import random

class game():
    def __init__(self):
        self.__gameOver = False
        self.__start = True
        self.__paused = False
        self.__playAgain = False
        self.__playerHit = False
        self.__dealerHit = False
        self.__stay = False
        self.__playerWin = False
        self.__dealerWin = False
        self.__draw = False
        self.__bust = False
        self.__deck = []

    def setGameOver(self, boolean):
        self.__gameOver = boolean

    def checkGameOver(self):
        return self.__gameOver

    def checkStart(self):
        return self.__start

    def setStart(self, boolean):
        self.__start = boolean

    def checkPaused(self):
        return self.__paused

    def setPaused(self, boolean):
        self.__paused = boolean

    def checkPlayAgain(self):
        return self.__playAgain

    def setPlayAgain(self, boolean):
        self.__playAgain = boolean

    def checkPlayerHit(self):
        return self.__playerHit

    def setPlayerHit(self, boolean):
        self.__playerHit = boolean

    def checkDealerHit(self):
        return self.__dealerHit

    def setDealerHit(self, boolean):
        self.__dealerHit = boolean

    def checkStay(self):
        return self.__stay

    def setStay(self, boolean):
        self.__stay = boolean

    def checkPlayerWin(self):
        return self.__playerWin

    def setPlayerWin(self, boolean):
        self.__playerWin = boolean

    def checkDealerWin(self):
        return self.__dealerWin

    def setDealerWin(self, boolean):
        self.__dealerWin = boolean

    def checkDraw(self):
        return self.__draw

    def setDraw(self, boolean):
        self.__draw = boolean

    def checkBust(self):
        return self.__bust

    def setBust(self, boolean):
        self.__bust = boolean


    def checkAces(self, player):
        if player.getTotal() > 21:
            for i in range(len(player.getHand())):
                if player.getHand()[i].getValue() == 11 and i not in player.getAceLocations():
                    player.addAce()
                    player.addAceLocation(i)

        if player.getTotal() > 21 and player.getAces() >=1:
            player.setPoints(player.getTotal() - 11)
            player.setPoints(player.getTotal() + 1)
            player.removeAce()
        if player.getTotal() > 21 and player.getAces() >=1:
            player.setPoints(player.getTotal() - 11)
            player.setPoints(player.getTotal() + 1)
            player.removeAce()
        if player.getTotal() > 21 and player.getAces() >=1:
            player.setPoints(player.getTotal() - 11)
            player.setPoints(player.getTotal() + 1)
            player.removeAce()
            

    def checkWin(self, player, dealer):
        if player.getTotal() > 21:
            game.checkAces(self, player)
        if dealer.getTotal() > 21:
            game.checkAces(self, dealer)

        if player.getTotal() > 21 and dealer.getTotal() < 21:
            game.setDealerWin(self, True)
            game.setGameOver(self, True)
        elif player.getTotal() < 21 and dealer.getTotal() > 21:
            game.setPlayerWin(self, True)
            game.setGameOver(self, True)
        elif player.getTotal() == 21 and dealer.getTotal() != 21:
            game.setPlayerWin(self, True)
            game.setGameOver(self, True)
        elif player.getTotal() != 21 and dealer.getTotal() == 21:
            game.setDealerWin(self, True)
            game.setGameOver(self, True)
        elif player.getTotal() == 21 and dealer.getTotal() == 21:
            game.setDraw(self, True)
            game.setGameOver(self, True)
        elif player.getTotal() < 21 and dealer.getTotal() < 21 and player.getTotal() == dealer.getTotal() and game.checkStay(self):
            game.setDraw(self, True)
            game.setGameOver(self, True)
        elif player.getTotal() > 21 and dealer.getTotal() > 21:
            game.setBust(self, True)
            game.setGameOver(self, True)

        elif game.checkStay(self) and dealer.getTotal() >=18:
            if player.getTotal() > dealer.getTotal():
                game.setPlayerWin(self, True)
                game.setGameOver(self, True)
            elif player.getTotal() < dealer.getTotal():
                game.setDealerWin(self, True)
                game.setGameOver(self, True)

    def initializeDeck(self, cardImages):
        values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        count = 0
        i = 0
        while i in range(len(values)-1):
            for j in range(len(cardImages)):
                if count <= 3:
                    self.__deck.append(Card.card(values[i], cardImages[j]))
                    count +=1
                if count == 4:
                    i +=1
                    count = 0

        return self.__deck

    def deckPop(self, deck, player):
        card = deck.pop()

        player.addCard(card)
        player.addPoints(card.getValue())

    def getDeck(self):
        return self.__deck

    def drawPlayerHand(self, player, surface, deck, playerX, playerY):
        if player.getHand() == []:
            random.shuffle(deck)
            game.deckPop(self, deck, player)
            game.deckPop(self, deck, player)

            if player.getTotal() >= 21:
                player.clear()
                player.setPoints(0)
                player.setAces(0)
                game.deckPop(self, deck, player)
                game.deckPop(self, deck, player)

        if game.checkPlayerHit(self):
            random.shuffle(deck)
            game.deckPop(self, deck, player)
            game.setPlayerHit(self, False)

        if game.checkStay(self): #
            game.setPlayerHit(self, False) #

        for i in range(len(player.getHand())):
            if i == 0:
                surface.blit(player.getHand()[i].getImage(), (playerX, playerY))
            if i == 1:
                surface.blit(player.getHand()[i].getImage(), (playerX + 150, playerY))
            if i == 2:
                surface.blit(player.getHand()[i].getImage(), (playerX - 150, playerY))
            if i == 3:
                surface.blit(player.getHand()[i].getImage(), (playerX + 300, playerY))
            if i == 4:
                surface.blit(player.getHand()[i].getImage(), (playerX - 300, playerY))
            if i == 5:
                surface.blit(player.getHand()[i].getImage(), (playerX + 450, playerY))

    def drawDealerHand(self, dealer, surface, deck, dealerX, dealerY, cardBack):
        if dealer.getHand() == []:
            random.shuffle(deck)
            game.deckPop(self, deck, dealer)
            game.deckPop(self, deck, dealer)

            if dealer.getTotal() >= 21:
                dealer.clear()
                dealer.setPoints(0)
                dealer.setAces(0)
                game.deckPop(self, deck, dealer)
                game.deckPop(self, deck, dealer)


        if game.checkDealerHit(self):
            random.shuffle(deck)
            game.deckPop(self, deck, dealer)
            game.setDealerHit(self, False)

        if not game.checkGameOver(self):
            for i in range(len(dealer.getHand())):
                if i == 0:
                    surface.blit(dealer.getHand()[i].getImage(), (dealerX, dealerY))
                if i == 1:
                    surface.blit(cardBack, (dealerX + 150, dealerY))
                if i == 2:
                    surface.blit(cardBack, (dealerX - 150, dealerY))
                if i == 3:
                    surface.blit(cardBack, (dealerX + 300, dealerY))
                if i == 4:
                    surface.blit(cardBack, (dealerX - 300, dealerY))
                if i == 5:
                    surface.blit(cardBack, (dealerX + 450, dealerY))
        
        if game.checkGameOver(self):
            for i in range(len(dealer.getHand())):
                if i == 0:
                    surface.blit(dealer.getHand()[i].getImage(), (dealerX, dealerY))
                if i == 1:
                    surface.blit(dealer.getHand()[i].getImage(), (dealerX + 150, dealerY))
                if i == 2:
                    surface.blit(dealer.getHand()[i].getImage(), (dealerX - 150, dealerY))
                if i == 3:
                    surface.blit(dealer.getHand()[i].getImage(), (dealerX + 300, dealerY))
                if i == 4:
                    surface.blit(dealer.getHand()[i].getImage(), (dealerX - 300, dealerY))
                if i == 5:
                    surface.blit(dealer.getHand()[i].getImage(), (dealerX + 450, dealerY))

    def drawText(self, surface, playerTotal, dealerTotal):
        
        if game.checkStart(self):
            myfont1 = pygame.font.SysFont("Serpentine", 200)
            BLACK = (0, 0, 0)
            label1 = myfont1.render("Blackjack", 1, BLACK)
            surface.blit(label1, (625, 300))

        if not game.checkStart(self):
            myfont2 = pygame.font.SysFont("Serpentine", 50)
            BLACK = (0, 0, 0)
            label2 = myfont2.render("Card Total: " + str(playerTotal), 1, BLACK)
            surface.blit(label2, (843, 750))

        if game.checkGameOver(self) and not game.checkStart(self):
            myfont3 = pygame.font.SysFont("Serpentine", 100)
            BLACK = (0, 0, 0)
            label3 = myfont3.render("Game Over", 1, BLACK)
            surface.blit(label3, (768, 400))

            myfont4 = pygame.font.SysFont("Serpentine", 50)
            BLACK = (0, 0, 0)
            label4 = myfont4.render("Card Total: " + str(dealerTotal), 1, BLACK)
            surface.blit(label4, (843, 300))

            if game.checkPlayerWin(self):
                myfont5 = pygame.font.SysFont("Serpentine", 40)
                BLACK = (0, 0, 0)
                label5 = myfont5.render("You Win", 1, BLACK)
                surface.blit(label5, (902, 500))
            elif game.checkDealerWin(self):
                myfont6 = pygame.font.SysFont("Serpentine", 40)
                BLACK = (0, 0, 0)
                label6 = myfont6.render("You Lose", 1, BLACK)
                surface.blit(label6, (897, 500))
            elif game.checkDraw(self):
                myfont7 = pygame.font.SysFont("Serpentine", 40)
                BLACK = (0, 0, 0)
                label7 = myfont7.render("It's a Draw", 1, BLACK)
                surface.blit(label7, (890, 500))
            elif game.checkBust(self):
                myfont8 = pygame.font.SysFont("Serpentine", 40)
                BLACK = (0, 0, 0)
                label8 = myfont8.render("You Both Bust", 1, BLACK)
                surface.blit(label8, (860, 500))






    