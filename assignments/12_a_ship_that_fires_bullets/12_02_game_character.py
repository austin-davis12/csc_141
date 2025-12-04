import pygame
import sys

class GameCharacter:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center

    def draw(self):
        self.screen.blit(self.image, self.rect)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Character")

bg_color = (135, 206, 235)  

character = GameCharacter(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)
    character.draw()
    pygame.display.flip()