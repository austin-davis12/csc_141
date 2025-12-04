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
    pygame.display.set_caption("13-01: Stars Grid")

    stars = pygame.sprite.Group()
    star = Star(screen)

    star_width, star_height = star.rect.size
    available_space_x = 800 - (2 * star_width)
    number_stars_x = available_space_x // (2 * star_width)

    available_space_y = 600 - (2 * star_height)
    number_rows = available_space_y // (2 * star_height)

    for row in range(number_rows):
        for col in range(number_stars_x):
            new_star = Star(screen)
            new_star.rect.x = star_width + 2 * star_width * col
            new_star.rect.y = star_height + 2 * star_height * row
            stars.add(new_star)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((10, 10, 20))
        stars.draw(screen)
        pygame.display.flip()

run_game()
