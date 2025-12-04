import sys

import pygame

class bluesky:
    

    def __init__(self):
        
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")

        
        self.bg_color = (0, 0, 255)

    def run_game(self):
        
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

           
            self.screen.fill(self.bg_color)


            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = bluesky()
    ai.run_game()