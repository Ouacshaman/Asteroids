import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shot, updatable, drawable)
    player = Player(x, y)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for i in updatable:
            i.update(dt)
        for j in asteroids:
            if j.collision(player):
                print("Game over!")
                sys.exit()
            for bullet in shot:
                if bullet.collision(j):
                    bullet.kill()
                    j.split()
        for k in drawable:
            k.draw(screen)
        pygame.display.flip()
        val = clock.tick(60)
        dt = val/1000


if __name__ == "__main__":
    main()
