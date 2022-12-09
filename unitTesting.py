import unittest
import Game
import Player
import pygame
import Card

class Testing(unittest.TestCase):
    pygame.init()
    screen = pygame.display.set_mode((1000,750))

    def test_Case1(self):

        newGame = Game.game()
        player = Player.player()
        dealer = Player.player()

        player.addPoints(19)
        dealer.addPoints(18)
        newGame.setStay(True)

        newGame.checkWin(player, dealer)

        self.assertTrue(newGame.checkPlayerWin(), True)

    def test_Case2(self):

        newGame = Game.game()
        player = Player.player()
        dealer = Player.player()

        player.addPoints(18)
        dealer.addPoints(19)
        newGame.setStay(True)

        newGame.checkWin(player, dealer)

        self.assertTrue(newGame.checkDealerWin(), True)

    def test_Case3(self):

        newGame = Game.game()
        player = Player.player()
        dealer = Player.player()

        player.addPoints(21)
        dealer.addPoints(19)

        newGame.checkWin(player, dealer)

        self.assertTrue(newGame.checkPlayerWin(), True)

    def test_Case4(self):

        newGame = Game.game()
        player = Player.player()
        dealer = Player.player()

        player.addPoints(19)
        dealer.addPoints(21)

        newGame.checkWin(player, dealer)

        self.assertTrue(newGame.checkDealerWin(), True)

    def test_Case5(self):

        newGame = Game.game()
        player = Player.player()
        dealer = Player.player()

        player.addPoints(19)
        dealer.addPoints(22)

        newGame.checkWin(player, dealer)

        self.assertTrue(newGame.checkPlayerWin(), True)

    def test_Case6(self):

        newGame = Game.game()
        player = Player.player()
        dealer = Player.player()

        player.addPoints(22)
        dealer.addPoints(20)

        newGame.checkWin(player, dealer)

        self.assertTrue(newGame.checkDealerWin(), True)

    def test_Case7(self):

        newGame = Game.game()
        player = Player.player()
        dealer = Player.player()

        player.addPoints(21)
        dealer.addPoints(21)

        newGame.checkWin(player, dealer)

        self.assertTrue(newGame.checkDraw(), True)

    def test_Case8(self):

        newGame = Game.game()
        player = Player.player()
        dealer = Player.player()

        player.addPoints(20)
        dealer.addPoints(20)
        newGame.setStay(True)

        newGame.checkWin(player, dealer)

        self.assertTrue(newGame.checkDraw(), True)

    def test_Case9(self):

        newGame = Game.game()
        player = Player.player()
        dealer = Player.player()

        player.addPoints(22)
        dealer.addPoints(22)
        newGame.setStay(True)

        newGame.checkWin(player, dealer)

        self.assertTrue(newGame.checkBust(), True)

    def test_Case10(self):
        cardBack = pygame.image.load("Images\\red_back.png").convert_alpha()
        cardBack = pygame.transform.smoothscale(cardBack, (150, 200))

        newGame = Game.game()
        player = Player.player()
        dealer = Player.player()
        card1 = Card.card(11, cardBack)
        card2 = Card.card(20, cardBack)
        player.addPoints(31)
        dealer.addPoints(20)
        player.addCard(card1)
        player.addCard(card2)

        newGame.checkWin(player, dealer)

        self.assertTrue(newGame.checkPlayerWin(), True)

        player.clear()
        dealer.clear()

        card1 = Card.card(11, cardBack)
        card2 = Card.card(19, cardBack)
        card3 = Card.card(11, cardBack)
        player.addPoints(41)
        dealer.addPoints(20)
        player.addCard(card1)
        player.addCard(card3)
        player.addCard(card2)

        newGame.checkWin(player, dealer)

        self.assertTrue(newGame.checkPlayerWin(), True)

        player.clear()
        dealer.clear()

        card1 = Card.card(11, cardBack)
        card2 = Card.card(18, cardBack)
        card3 = Card.card(11, cardBack)
        card4 = Card.card(11, cardBack)
        player.addPoints(51)
        dealer.addPoints(20)
        player.addCard(card1)
        player.addCard(card3)
        player.addCard(card2)
        player.addCard(card4)

        newGame.checkWin(player, dealer)

        self.assertTrue(newGame.checkPlayerWin(), True)

    def test_Case11(self):
        cardBack = pygame.image.load("Images\\red_back.png").convert_alpha()
        cardBack = pygame.transform.smoothscale(cardBack, (150, 200))

        newGame = Game.game()
        player = Player.player()
        card1 = Card.card(11, cardBack)
        card2 = Card.card(18, cardBack)
        card3 = Card.card(11, cardBack)
        player.addCard(card1)
        player.addCard(card3)
        player.addCard(card2)
        player.setPoints(40)

        newGame.checkAces(player)
        
        self.assertEqual(player.getAces(), 0)
        self.assertEqual(len(player.getAceLocations()), 2)
        self.assertEqual(player.getTotal(), 20)

    def test_Case12(self):
        cardBack = pygame.image.load("Images\\red_back.png").convert_alpha()
        cardBack = pygame.transform.smoothscale(cardBack, (150, 200))

        card1 = Card.card(11, cardBack)

        self.assertEqual(card1.getValue(), 11)

    def test_Case13(self):
        cardBack = pygame.image.load("Images\\red_back.png").convert_alpha()
        cardBack = pygame.transform.smoothscale(cardBack, (150, 200))

        card1 = Card.card(11, cardBack)

        self.assertEqual(card1.getImage(), cardBack)

    def test_Case14(self):
        newGame = Game.game()

        self.assertEqual(newGame.checkStart(), True)
        self.assertEqual(newGame.checkPaused(), False)
        self.assertEqual(newGame.checkGameOver(), False)
        self.assertEqual(newGame.checkPlayAgain(), False)
        self.assertEqual(newGame.checkPlayerHit(), False)
        self.assertEqual(newGame.checkDealerHit(), False)
        self.assertEqual(newGame.checkStay(), False)
        self.assertEqual(newGame.checkPlayerWin(), False)
        self.assertEqual(newGame.checkPlayerWin(), False)
        self.assertEqual(newGame.checkDealerWin(), False)
        self.assertEqual(newGame.checkDraw(), False)
        self.assertEqual(newGame.checkBust(), False)
        self.assertEqual(len(newGame.getDeck()), 0)

    def test_Case15(self):
        cardBack = pygame.image.load("Images\\red_back.png").convert_alpha()
        cardBack = pygame.transform.smoothscale(cardBack, (150, 200))
        cardImages = [cardBack, cardBack, cardBack, cardBack, cardBack, cardBack, cardBack, cardBack, cardBack, cardBack]

        newGame = Game.game()
        player = Player.player()
        dealer = Player.player()
        screen = pygame.display.set_mode((1000,750))

        newGame.initializeDeck(cardImages)
        playDeck = newGame.getDeck()

        newGame.drawPlayerHand(player, screen, playDeck, player.getPlayerX(), player.getPlayerY())
        newGame.drawDealerHand(dealer, screen, playDeck, dealer.getDealerX(), dealer.getDealerY(), cardBack)

        newGame.setPlayerHit(True)
        newGame.drawPlayerHand(player, screen, playDeck, player.getPlayerX(), player.getPlayerY())

        newGame.setDealerHit(True)
        newGame.drawDealerHand(dealer, screen, playDeck, dealer.getDealerX(), dealer.getDealerY(), cardBack)

        self.assertEqual(len(player.getHand()), 3)
        self.assertEqual(len(dealer.getHand()), 3)

    def test_Case16(self):
        cardBack = pygame.image.load("Images\\red_back.png").convert_alpha()
        cardBack = pygame.transform.smoothscale(cardBack, (150, 200))
        cardImages = [cardBack, cardBack, cardBack, cardBack, cardBack, cardBack, cardBack, cardBack, cardBack, cardBack]

        newGame = Game.game()
        player = Player.player()
        dealer = Player.player()
        screen = pygame.display.set_mode((1000,750))

        newGame.initializeDeck(cardImages)
        playDeck = newGame.getDeck()

        newGame.drawPlayerHand(player, screen, playDeck, player.getPlayerX(), player.getPlayerY())
        newGame.drawDealerHand(dealer, screen, playDeck, dealer.getDealerX(), dealer.getDealerY(), cardBack)

        newGame.setStay(True)
        newGame.drawPlayerHand(player, screen, playDeck, player.getPlayerX(), player.getPlayerY())

        self.assertEqual(newGame.checkPlayerHit(), False)
        self.assertEqual(len(player.getHand()), 2)

    def test_Case17(self):
        cardBack = pygame.image.load("Images\\red_back.png").convert_alpha()
        cardBack = pygame.transform.smoothscale(cardBack, (150, 200))

        player = Player.player()
        dealer = Player.player()
        screen = pygame.display.set_mode((1000,750))
        newGame = Game.game()

        newGame.setStart(True)
        newGame.drawText(screen, player.getTotal(), dealer.getTotal())
        newGame.setStart(False)
        
        player.setPoints(15)
        dealer.setPoints(15)
        newGame.checkWin(player, dealer)
        self.assertEqual(newGame.checkGameOver(), False)
        newGame.drawText(screen, player.getTotal(), dealer.getTotal())


        player.addPoints(6)
        newGame.checkWin(player, dealer)
        self.assertEqual(newGame.checkPlayerWin(), True)
        self.assertEqual(newGame.checkGameOver(), True)
        newGame.drawText(screen, player.getTotal(), dealer.getTotal())
        newGame.setPlayerWin(False)
        newGame.setGameOver(False)
        player.setPoints(15)
        

        dealer.addPoints(6)
        newGame.checkWin(player, dealer)
        self.assertEqual(newGame.checkDealerWin(), True)
        self.assertEqual(newGame.checkGameOver(), True)
        newGame.drawText(screen, player.getTotal(), dealer.getTotal())
        newGame.setDealerWin(False)
        newGame.setGameOver(False)
        dealer.setPoints(15)


        player.addPoints(7)
        dealer.addPoints(7)
        newGame.checkWin(player, dealer)
        self.assertEqual(newGame.checkBust(), True)
        self.assertEqual(newGame.checkGameOver(), True)
        newGame.drawText(screen, player.getTotal(), dealer.getTotal())
        newGame.setBust(False)
        newGame.setGameOver(False)
        dealer.setPoints(15)
        player.setPoints(15)


        player.addPoints(3)
        dealer.addPoints(3)
        newGame.setStay(True)
        newGame.checkWin(player, dealer)
        self.assertEqual(newGame.checkDraw(), True)
        self.assertEqual(newGame.checkGameOver(), True)
        newGame.drawText(screen, player.getTotal(), dealer.getTotal())

if __name__ == '__main__':
    unittest.main()
