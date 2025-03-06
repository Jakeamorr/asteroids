from circleshape import CircleShape 
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):

    def draw(self):
        pygame.draw.circle(self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

