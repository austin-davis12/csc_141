import sys
import pygame

class Star(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect()

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("13-02: Bigger Star Spacing")

    stars = pygame.sprite.Group()
    star = Star(screen)

    star_width, star_height = star.rect.size
    spacing = star_width * 3   # Increased spacing

    available_space_x = 800 - spacing
    number_stars_x = available_space_x // spacing

    available_space_y = 600 - spacing
    number_rows = available_space_y // spacing

    for row in range(number_rows):
        for col in range(number_stars_x):
            new_star = Star(screen)
            new_star.rect.x = spacing * col
            new_star.rect.y = spacing * row
            stars.add(new_star)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((10, 10, 20))
        stars.draw(screen)
        pygame.display.flip()

run_game()
