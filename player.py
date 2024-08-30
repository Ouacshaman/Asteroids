from circleshape import CircleShape
import pygame
from constants import (PLAYER_RADIUS, PLAYER_TURN_SPEED,
                       PLAYER_SPEED, PLAYER_SHOOT_SPEED,
                       PLAYER_SHOOT_COOLDOWN)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = PLAYER_RADIUS
        super().__init__(self.x, self.y, self.radius)
        self.position = pygame.Vector2(self.x, self.y)
        self.rotation = 0
        self.timer = 0

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = (pygame.Vector2(0, 1).rotate(self.rotation + 90) *
                 self.radius / 1.5)
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN
        self.timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity = direction * PLAYER_SHOOT_SPEED
