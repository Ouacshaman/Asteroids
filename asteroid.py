from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1)
        self.position = pygame.Vector2(self.x, self.y)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                           (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        blue_angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(blue_angle)
        vec2 = self.velocity.rotate(-blue_angle)
        new_r = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position.x, self.position.y, new_r)
        new_ast2 = Asteroid(self.position.x, self.position.y, new_r)
        new_ast1.velocity = vec1 * 1.2
        new_ast2.velocity = vec2 * 1.2
