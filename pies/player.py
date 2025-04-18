from circleshape import *
from constants import PLAYER_RADIUS

class Player:
    def __init__(self, x, y):
        super().__init__(x, y)
        rotation = 0
        self.radius = PLAYER_RADIUS
        self.rotation = rotation

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
