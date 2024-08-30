from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1)
        self.position = pygame.Vector2(self.x, self.y)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                           (self.position.x, self.position.y), SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity*dt
