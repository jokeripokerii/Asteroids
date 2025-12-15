import pygame
import sys
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event

def main():
    pygame.init()
    print(pygame.draw.polygon)
    kello = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #all groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #setting up
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    pelaaja = Player(x, y)
    asteroidikentta = AsteroidField()

    #game loop
    while True:
        log_state()

        #exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #drawing objects
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)

        #update objects
        updatable.update(dt)

        #checking player collision to asteroids
        for roid in asteroids:
            if roid.collides_with(pelaaja) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        #checking bullet hits
        for roid2 in asteroids:
            for buret in shots:
                if roid2.collides_with(buret) == True:
                    log_event("asteroid_shot")
                    roid2.split()
                    buret.kill()

        pygame.display.flip()
        kello.tick(60)
        dt = kello.tick(60) / 1000

if __name__ == "__main__":
    main()
    
