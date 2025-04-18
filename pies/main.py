import pygame
from constants import *
# imports all the constants. Bad idea normally, but for this small
# project it works fine.
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # This is pretty understandable, just carrying over constants
    # and writing them for players
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Sets up the screen to the desired size
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0,0,0), rect=None, special_flags=0)
        # Somehow removing pygame from the start here has fixed the code.
        # I don't get it. Anywhom.
        pygame.display.flip()
        # Infinite while-loop constantly sets the background to black and
        # then resets the positions of objects onscreen to make sure it's
        # keeping up with player placement
        dt = clock.tick(60) / 1000
        # This just caps the framerate at 60fps to support CPU
    pygame.quit()

if __name__ == "__main__":
    main()
