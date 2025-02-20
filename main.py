from constants import *
import pygame

print(f"Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	timeClock = pygame.time.Clock()
	dt = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill((0,0,0))
		pygame.display.flip()
		dt = timeClock.tick(60) / 1000



if __name__ == "__main__":
    main()
