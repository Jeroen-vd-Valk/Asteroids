import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # create some groups and add classes to it
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    


    print("Starting Asteroids!")
    pygame.init
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # these are variables needed for the game to work
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    time = pygame.time.Clock()

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))        # renders the background

        updatable.update(dt)
        for item in drawable:
            item.draw(screen)         # renders the player's model

        for asteroid in asteroids:
            if (asteroid.collision_checker(player)):
                print("Game over!")
                exit()

        for asteroid in asteroids:
            for bullet in shots:
                if(asteroid.collision_checker(bullet)):
                    asteroid.split()
                    bullet.kill()


        pygame.display.flip()       # flips the screen
        dt = time.tick(60) / 1000   # delays to 60 fps















if __name__ == "__main__":
    main()
