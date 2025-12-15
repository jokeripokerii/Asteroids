import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.radius = radius
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20,50)
        eka = pygame.math.Vector2.rotate(self.velocity, rand_angle)
        toka = pygame.math.Vector2.rotate(self.velocity, -rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        uusroidi1 = Asteroid(self.position.x, self.position.y, new_radius)
        uusroidi2 = Asteroid(self.position.x, self.position.y, new_radius)
        uusroidi1.velocity = eka * 1.2
        uusroidi2.velocity = toka

