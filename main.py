from constants import *
from player import *
import pygame
print(f"Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        timeClock = pygame.time.Clock()
        player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
        dt = 0
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return
                screen.fill((0,0,0))
                player.update(dt)
                player.draw(screen)
                pygame.display.flip()
                dt = timeClock.tick(60) / 1000

if __name__ == "__main__":
    main()