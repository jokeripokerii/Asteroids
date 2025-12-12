import pygame
from circleshape import CircleShape
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    print(pygame.draw.polygon)
    kello = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    pelaaja = Player(x, y)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pelaaja.draw(screen)
        pelaaja.update(dt)
        pygame.display.flip()
        kello.tick(60)
        dt = kello.tick(60) / 1000

if __name__ == "__main__":
    main()
    
