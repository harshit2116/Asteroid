import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return;

        self.kill()
        
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        first_velocity = self.velocity.rotate(random_angle)
        second_velocity = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = first_velocity * 1.2
        asteroid2.velocity = second_velocity * 1.2



        