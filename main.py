import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE
from player import Player

def main():
    # create some groups and add all Player classes to it
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    print("Starting Asteroids!")
    pygame.init
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # these are variables needed for the game to work
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    time = pygame.time.Clock()

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))


    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))        # renders the background

        updatable.update(dt)
        for item in drawable:
            item.draw(screen)         # renders the player's model

        pygame.display.flip()       # flips the screen
        dt = time.tick(60) / 1000   # delays to 60 fps















if __name__ == "__main__":
    main()
