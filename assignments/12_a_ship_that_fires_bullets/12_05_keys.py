import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Key Logger")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                print(f"Key pressed: {pygame.key.name(event.key)}")

            elif event.type == pygame.KEYUP:
                print(f"Key released: {pygame.key.name(event.key)}")

        screen.fill((230, 230, 230))
        pygame.display.flip()

run_game()
