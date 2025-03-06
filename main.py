import pygame
from constants import *
from player import Player
from asteroid import Asteroid

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
    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    # create player
    mid_x = SCREEN_WIDTH / 2
    mid_y = SCREEN_HEIGHT / 2
    p1 = Player(mid_x, mid_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

