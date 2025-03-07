import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # initialize game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # create clock to limit framerate and track delta time
    clock = pygame.time.Clock()
    dt = 0
    #create groups
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable)
    # create player
    mid_x = SCREEN_WIDTH / 2
    mid_y = SCREEN_HEIGHT / 2
    p1 = Player(mid_x, mid_y)
    af = AsteroidField()
    # game loop
    while True:
        # check for quit signal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # draw to the screen
        screen.fill("black")
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        # update the screen & set framerate
        pygame.display.flip()
        dt = clock.tick(30) / 1000
        # check game condition
        for a in asteroids:
            if p1.collision(a):
                print("Game over!")
                return

if __name__ == "__main__":
    main()

