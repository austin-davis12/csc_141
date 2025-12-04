

import pygame
import sys
import random
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, K_a, K_d, K_p, K_q, K_ESCAPE, K_r

# ---------- Configuration ----------
WIDTH, HEIGHT = 900, 640
FPS = 60

SHIP_WIDTH, SHIP_HEIGHT = 60, 14
SHIP_COLOR = (220, 220, 255)
SHIP_SPEED = 6

BULLET_WIDTH, BULLET_HEIGHT = 4, 12
BULLET_COLOR = (255, 255, 100)
BULLET_SPEED = 10
MAX_BULLETS = 4

ALIEN_ROWS = 4
ALIEN_COLUMNS = 9
ALIEN_WIDTH, ALIEN_HEIGHT = 44, 36
ALIEN_H_GAP = 18
ALIEN_V_GAP = 14
ALIEN_COLOR = (160, 255, 160)

FLEET_DROP_SPEED = 28
BASE_FLEET_SPEED = 0.8  # horizontal speed (pixels per frame)
SPEEDUP_SCALE = 1.15     # how much speed increases each level

SCORE_ALIEN = 50
FONT_NAME = None  # default font

# ---------- Game objects ----------
class Ship:
    def __init__(self, x, y, width=SHIP_WIDTH, height=SHIP_HEIGHT):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = SHIP_SPEED
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left:
            self.rect.x -= self.speed
        if self.moving_right:
            self.rect.x += self.speed
        # clamp to screen
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(WIDTH, self.rect.right)

    def draw(self, surface):
        # draw a triangular ship using polygon for visual flair
        cx, cy = self.rect.centerx, self.rect.centery
        w, h = self.rect.width, self.rect.height
        points = [
            (cx - w//2, cy + h//2),
            (cx + w//2, cy + h//2),
            (cx, cy - h*2)
        ]
        pygame.draw.polygon(surface, SHIP_COLOR, points)
        # small shadow
        pygame.draw.polygon(surface, (50, 50, 60), [(p[0], p[1]+2) for p in points], 0 if False else 0)

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, BULLET_WIDTH, BULLET_HEIGHT)
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, BULLET_COLOR, self.rect)

class Alien:
    def __init__(self, x, y, w=ALIEN_WIDTH, h=ALIEN_HEIGHT):
        self.rect = pygame.Rect(0, 0, w, h)
        self.rect.x = x
        self.rect.y = y
        self.alive = True
        # small internal animation phase
        self.phase = random.uniform(0, 3.14)

    def update(self):
        # little bobbing motion
        self.phase += 0.06
        # y offset for bob visually (not modifying rect)
        # handled in drawing

    def draw(self, surface):
        # draw alien as rounded rect + eyes
        r = self.rect
        # body
        body = pygame.Rect(r.x, r.y, r.width, r.height)
        pygame.draw.rect(surface, ALIEN_COLOR, body, border_radius=8)
        # eyes
        eye_w = r.width // 7
        eye_h = r.height // 5
        eye_y = r.y + r.height // 4
        pygame.draw.circle(surface, (30, 30, 50), (r.x + r.width//3, eye_y), eye_w//2)
        pygame.draw.circle(surface, (30, 30, 50), (r.x + 2*r.width//3, eye_y), eye_w//2)

# ---------- Game manager ----------
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.reset_stats()
        self.font = pygame.font.Font(FONT_NAME, 20)
        self.large_font = pygame.font.Font(FONT_NAME, 42)

        self.ship = Ship(WIDTH//2, HEIGHT - 24)
        self.bullets = []
        self.aliens = []
        self.fleet_speed = BASE_FLEET_SPEED
        self.fleet_direction = 1  # 1 => right, -1 => left
        self.game_active = True
        self.paused = False

        self.create_fleet()

    def reset_stats(self):
        self.score = 0
        self.level = 1
        self.lives = 3
        self.game_active = True

    def create_fleet(self):
        self.aliens.clear()
        # calculate starting position
        total_w = ALIEN_COLUMNS * ALIEN_WIDTH + (ALIEN_COLUMNS - 1) * ALIEN_H_GAP
        offset_x = (WIDTH - total_w) // 2
        start_y = 60

        for row in range(ALIEN_ROWS):
            for col in range(ALIEN_COLUMNS):
                x = offset_x + col * (ALIEN_WIDTH + ALIEN_H_GAP)
                y = start_y + row * (ALIEN_HEIGHT + ALIEN_V_GAP)
                alien = Alien(x, y)
                self.aliens.append(alien)

        # fleet parameters
        self.fleet_speed = BASE_FLEET_SPEED * (SPEEDUP_SCALE ** (self.level - 1))
        self.fleet_direction = 1

    def check_fleet_edges(self):
        for alien in self.aliens:
            if alien.rect.right >= WIDTH or alien.rect.left <= 0:
                return True
        return False

    def change_fleet_direction(self):
        for alien in self.aliens:
            alien.rect.y += FLEET_DROP_SPEED
        self.fleet_direction *= -1

    def fire_bullet(self):
        if len(self.bullets) >= MAX_BULLETS:
            return
        b = Bullet(self.ship.rect.centerx, self.ship.rect.top)
        self.bullets.append(b)

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.update()
            # remove if off-screen
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        # check collisions with aliens
        for bullet in self.bullets[:]:
            for alien in self.aliens[:]:
                if bullet.rect.colliderect(alien.rect):
                    try:
                        self.bullets.remove(bullet)
                    except ValueError:
                        pass
                    try:
                        self.aliens.remove(alien)
                    except ValueError:
                        pass
                    self.score += SCORE_ALIEN
                    break

    def update_aliens(self):
        # move horizontally
        dx = self.fleet_speed * self.fleet_direction
        for alien in self.aliens:
            alien.rect.x += dx
            alien.update()

        if self.check_fleet_edges():
            self.change_fleet_direction()

        # check if any alien hit bottom (ship loses a life)
        for alien in self.aliens:
            if alien.rect.bottom >= self.ship.rect.top:
                self.ship_hit()
                break

    def ship_hit(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_active = False
        else:
            # reset a bit: clear bullets, reposition ship, respawn fleet
            self.bullets.clear()
            self.ship.rect.centerx = WIDTH // 2
            self.create_fleet()
            pygame.time.delay(600)

    def check_level_complete(self):
        if not self.aliens:
            self.level += 1
            self.create_fleet()
            # speed up bullets a touch and allow more bullets in later levels:
            global BULLET_SPEED, MAX_BULLETS
            BULLET_SPEED = int(BULLET_SPEED * 1.05)
            MAX_BULLETS = min(6, MAX_BULLETS + 1)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key in (K_LEFT, K_a):
                    self.ship.moving_left = True
                if event.key in (K_RIGHT, K_d):
                    self.ship.moving_right = True
                if event.key == K_SPACE:
                    self.fire_bullet()
                if event.key == K_p:
                    self.paused = not self.paused
                if event.key in (K_q, K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if not self.game_active and event.key == K_r:
                    self.reset_after_game_over()

            # KEYUP events:
            if event.type == pygame.KEYUP:
                if event.key in (K_LEFT, K_a):
                    self.ship.moving_left = False
                if event.key in (K_RIGHT, K_d):
                    self.ship.moving_right = False

    def reset_after_game_over(self):
        self.reset_stats()
        self.ship = Ship(WIDTH//2, HEIGHT - 24)
        self.bullets.clear()
        self.create_fleet()
        self.game_active = True

    def draw_hud(self):
        # score
        score_surf = self.font.render(f"Score: {self.score}", True, (230, 230, 230))
        self.screen.blit(score_surf, (10, 8))

        # level
        level_surf = self.font.render(f"Level: {self.level}", True, (230, 230, 230))
        self.screen.blit(level_surf, (WIDTH - 120, 8))

        # lives
        lives_surf = self.font.render(f"Lives: {self.lives}", True, (230, 230, 230))
        self.screen.blit(lives_surf, (WIDTH//2 - 40, 8))

        # pause text
        if self.paused:
            p = self.large_font.render("PAUSED", True, (255, 210, 60))
            self.screen.blit(p, (WIDTH//2 - p.get_width()//2, HEIGHT//2 - 40))

    def draw_background(self):
        # starfield background
        self.screen.fill((10, 10, 25))
        # subtle stars
        for i in range(50):
            x = (i * 37) % WIDTH
            y = (i * 61) % HEIGHT
            pygame.draw.circle(self.screen, (20, 20, 40), (x, y), 1)

    def update(self):
        if not self.game_active:
            return
        if self.paused:
            return

        self.ship.update()
        self.update_bullets()
        self.update_aliens()
        self.check_level_complete()

    def draw(self):
        self.draw_background()
        # draw ship
        self.ship.draw(self.screen)
        # draw bullets
        for b in self.bullets:
            b.draw(self.screen)
        # draw aliens
        for alien in self.aliens:
            alien.draw(self.screen)
        # HUD
        self.draw_hud()

        if not self.game_active:
            self.show_game_over()

        pygame.display.flip()

    def show_game_over(self):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((8, 8, 10, 180))
        self.screen.blit(overlay, (0, 0))
        go_text = self.large_font.render("GAME OVER", True, (255, 80, 80))
        sub = self.font.render(f"Final Score: {self.score}  —  Press R to restart", True, (220, 220, 220))
        self.screen.blit(go_text, (WIDTH//2 - go_text.get_width()//2, HEIGHT//2 - 60))
        self.screen.blit(sub, (WIDTH//2 - sub.get_width()//2, HEIGHT//2 + 10))

    def run(self):
        # main loop
        while True:
            dt = self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

# ---------- Main ----------
def main():
    pygame.init()
    pygame.display.set_caption("Alien Invasion (Pygame)")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()
