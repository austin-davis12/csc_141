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
        self.y = float(self.rect.y)

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= 1
        if self.moving_up and self.rect.top > 0:
            self.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1

        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """Print a message when touching any edge."""
        if self.rect.left <= 0:
            print("Hit left edge!")
        if self.rect.right >= self.screen_rect.right:
            print("Hit right edge!")
        if self.rect.top <= 0:
            print("Hit top edge!")
        if self.rect.bottom >= self.screen_rect.bottom:
            print("Hit bottom edge!")

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Screen Edge Detection")

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
                elif event.key == pygame.K_UP:
                    rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    rocket.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    rocket.moving_right = False
                elif event.key == pygame.K_UP:
                    rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = False

        rocket.update()
        rocket.check_edges()

        screen.fill((230, 230, 230))
        rocket.blitme()
        pygame.display.flip()

run_game()
