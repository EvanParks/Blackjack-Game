import pygame

class makeButton():
        def __init__(self, xpos, ypos, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (xpos,ypos)
            self.buttonClicked = False

        def drawButton(self, surface):
            pressed = False

            mousePosition = pygame.mouse.get_pos()

            if self.rect.collidepoint(mousePosition):
                if pygame.mouse.get_pressed()[0] == 1 and self.buttonClicked == False:
                    self.buttonClicked = True
                    pressed = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.buttonClicked = False

            surface.blit(self.image, (self.rect.x, self.rect.y))

            return pressed