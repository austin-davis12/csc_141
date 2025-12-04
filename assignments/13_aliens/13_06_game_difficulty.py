import sys
import pygame
import random

class Star(pygame.sprite.Sprite):
    def __init__(self, screen, difficulty=1.0):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 600)
        self.speed = random.uniform(0.5, 2.0) * difficulty

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.left = 800

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("13-06: Increasing Difficulty")

    difficulty = 1.0
    stars = pygame.sprite.Group()

    for _ in range(70):
        stars.add(Star(screen, difficulty))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Difficulty increases slowly over time
        difficulty += 0.0005

        # Refresh stars with increased difficulty occasionally
        if random.random() < 0.01:
            stars.add(Star(screen, difficulty))

        stars.update()
        screen.fill((0, 0, 20))
        stars.draw(screen)
        pygame.display.flip()

        clock.tick(60)

run_game()
