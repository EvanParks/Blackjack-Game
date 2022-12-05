import pygame
import Game
import Button
import Player
import random

class main():

    newGame = Game.game()
    player = Player.player()
    dealer = Player.player()

    pygame.init()    
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption("BlackJack")

    #making empty lists
    directory = []
    actualDeck = []
    #making list of directories
    for i in range(1,14):
        for j in range(1,5):
            directory.append("Images\\" + str(i) + "_" + str(j) + ".png")
    #making deck of images from list of directories
    for card in directory:
        actualDeck.append(pygame.transform.smoothscale(pygame.image.load(card), (150, 200)))

    #background
    bg = pygame.image.load("Images\\backgroundImage.png").convert_alpha()

    #making cardback image
    cardBack = pygame.image.load("Images\\red_back.png").convert_alpha()
    cardBack = pygame.transform.smoothscale(cardBack, (150, 200)) 

    #start image
    startImage = pygame.image.load("Images\\startImage2.png").convert_alpha()
    startImage = pygame.transform.smoothscale(startImage, (120, 60))
    #300, 300

    #quit image
    exitImage = pygame.image.load("Images\\exitImage2.png").convert_alpha()
    exitImage = pygame.transform.smoothscale(exitImage, (120, 60))

    #pause button image
    pause = pygame.image.load("Images\\pauseImage.png").convert_alpha()
    pause = pygame.transform.smoothscale(pause, (45, 45))

    #hit image
    hitImage = pygame.image.load("Images\\hitImage2.png").convert_alpha()
    hitImage = pygame.transform.smoothscale(hitImage, (120, 60))

    #stay image
    stayImage = pygame.image.load("Images\\standImage2.png").convert_alpha()
    stayImage = pygame.transform.smoothscale(stayImage, (120, 60))

    #exit image
    leaveImage = pygame.image.load("Images\\leaveImage2.png").convert_alpha()
    leaveImage = pygame.transform.smoothscale(leaveImage, (120, 60))

    #continue image
    contImage = pygame.image.load("Images\\resumeImage2.png").convert_alpha()
    contImage = pygame.transform.smoothscale(contImage, (120, 60))

    #play again image
    playAgain = pygame.image.load("Images\\restartImage2.png").convert_alpha()
    playAgain = pygame.transform.smoothscale(playAgain, (120, 60))

    #exit image
    quitImage = pygame.image.load("Images\\quitImage2.png").convert_alpha()
    quitImage = pygame.transform.smoothscale(quitImage, (120, 60))

    #Buttons
    start_button = Button.makeButton(897, 500, startImage)
    exit_button = Button.makeButton(897, 600, exitImage)
    
    pause_button = Button.makeButton(10, 10, pause)
    hit_button = Button.makeButton(1780, 600, hitImage)
    stay_button = Button.makeButton(1780, 700, stayImage)
    
    cont_button = Button.makeButton(897, 500, contImage)
    leave_button = Button.makeButton(897, 600, leaveImage)

    play_again = Button.makeButton(800, 600, playAgain)
    quit_button = Button.makeButton(1000, 600, quitImage) 

    newGame.initializeDeck(actualDeck)
    playDeck = newGame.getDeck().copy()

    running = True
    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

        #screen.fill([53,101,77])
        screen.blit(bg, (0,0))

        if newGame.checkStart():
            newGame.drawText(screen, player.getTotal(), dealer.getTotal())
            newGame.setPaused(False)
            if start_button.drawButton(screen):
                print('Start')
                newGame.setStart(False)
            if exit_button.drawButton(screen):
                print('Quit')
                running = False

        elif newGame.checkPaused():
            if cont_button.drawButton(screen):
                print('Continue')
                newGame.setPaused(False)
            if leave_button.drawButton(screen):
                print('Exit')
                newGame.setPlayAgain(True)
                newGame.setPaused(False)
                newGame.setStart(True)
                
        elif newGame.checkPlayAgain():
            playDeck = newGame.getDeck().copy()
            random.shuffle(playDeck)
            player.clear()
            dealer.clear()
            player.setPoints(0)
            dealer.setPoints(0)
            player.setAces(0)
            dealer.setAces(0)
            newGame.setGameOver(False)
            newGame.setPaused(False)
            newGame.setPlayerHit(False)
            newGame.setDealerHit(False)
            newGame.setStay(False)
            newGame.setPlayerWin(False)
            newGame.setDealerWin(False)
            newGame.setDraw(False)
            newGame.setBust(False)
            newGame.setPlayAgain(False)

        elif newGame.checkGameOver():
            newGame.drawPlayerHand(player,screen, playDeck, player.getPlayerX(), player.getPlayerY())
            newGame.drawDealerHand(dealer, screen, playDeck, dealer.getDealerX(), dealer.getDealerY(), cardBack) #
            newGame.drawText(screen, player.getTotal(), dealer.getTotal())
            if play_again.drawButton(screen):
                print('Play Again')
                newGame.setPlayAgain(True)
            if quit_button.drawButton(screen):
                print('Exit')
                newGame.setPlayAgain(True)
                newGame.setStart(True)

        else:
            if pause_button.drawButton(screen):
                print('Paused')
                newGame.setPaused(True)

            if hit_button.drawButton(screen):
                print('hit')
                if player.getTotal() < 21 and not newGame.checkStay():
                    newGame.setPlayerHit(True)
                    newGame.drawPlayerHand(player,screen, playDeck, player.getPlayerX(), player.getPlayerY()) 
                if dealer.getTotal() < 18 and not newGame.checkStay():
                    newGame.setDealerHit(True)
                    newGame.drawDealerHand(dealer, screen, playDeck, dealer.getDealerX(), dealer.getDealerY(), cardBack) #
                    print(dealer.getTotal())

            if stay_button.drawButton(screen):
                print('stay')
                newGame.setStay(True)
                
            if dealer.getTotal() < 18 and newGame.checkStay():
                newGame.setDealerHit(True)
                newGame.drawDealerHand(dealer, screen, playDeck, dealer.getDealerX(), dealer.getDealerY(), cardBack) #

            newGame.drawPlayerHand(player,screen, playDeck, player.getPlayerX(), player.getPlayerY())
            newGame.drawDealerHand(dealer, screen, playDeck, dealer.getDealerX(), dealer.getDealerY(), cardBack) #
            newGame.checkWin(player, dealer)
            newGame.drawText(screen, player.getTotal(), dealer.getTotal())
    
        pygame.display.update()
        
    pygame.quit()


if __name__ == '__main__':
    main()