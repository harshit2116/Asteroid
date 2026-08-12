import pygame
import sys
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(x, y)
    asteroidfield = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(True):
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        dt = (clock.tick(60)/1000)
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        print(dt)
if __name__ == "__main__":
    main()