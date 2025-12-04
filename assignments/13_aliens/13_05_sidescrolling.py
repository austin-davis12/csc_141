import sys
import pygame
import random

class Star(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 600)
        self.speed = random.uniform(0.5, 2.0)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.left = 800

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("13-05: Side-Scrolling Starfield")

    stars = pygame.sprite.Group()
    for _ in range(80):
        stars.add(Star(screen))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        stars.update()
        screen.fill((0, 0, 15))
        stars.draw(screen)
        pygame.display.flip()

run_game()
