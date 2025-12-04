
import sys
import pygame

class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("rocket.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)

        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= 1

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rocket Left/Right")

    rocket = Rocket(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rocket.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    rocket.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    rocket.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    rocket.moving_right = False

        rocket.update()
        screen.fill((230, 230, 230))
        rocket.blitme()

        pygame.display.flip()

run_game()
