import pygame
import math
import random

pygame.init()                           # starte opp pygame
size = width, height = 1020, 840        # Bane
clock = pygame.time.Clock()             # Klokka

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

# ==============
# Boid Class
# ==============
class boid(pygame.sprite.Sprite):

    def __init__(self, position, speed, color, radius):
        """
        Speed: length and angle
        Position: X and Y
        """

        pygame.sprite.Sprite.__init__(self) # pygame sprite constructor

        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(position[0], position[1], radius, radius)
        #self.area = screen.get_rect()
        self.speed = pygame.math.Vector2(speed)
        self.position = pygame.math.Vector2(position)

    def update(self):
        newpos = self.calcnewpos(self.rect, self.speed)

        self.rect = newpos

    def calcnewpos(self, rect, speed):
        return rect.move(speed)

    def get_pos_vector(self):
        return pygame.math.Vector2(self.rect[:2])

    # ==============
    # Rules for Boids
    # ==============
    def toward_center(self, other_boids):

        perceived_center = pygame.math.Vector2()

        for boid in other_boids:
            if boid != self:
                pos = boid.get_pos_vector()
                perceived_center = perceived_center + pos

        perceived_center = perceived_center / (len(other_boids) - 1)
        pygame.draw.rect(screen, black, pygame.Rect(perceived_center[0], perceived_center[1], 5, 5))

        return (perceived_center - self.get_pos_vector()) / math.exp(9)

    def avoid_obstacle(self, other_boids):
        c = pygame.math.Vector2()

        for boid in other_boids:
            if boid != self:
                if pygame.math.Vector2.length(boid.get_pos_vector() - self.get_pos_vector()) < 30:
                    c = c - (boid.get_pos_vector() - self.get_pos_vector())

        return c / 30

    def match_velocity(self, other_boids):

        perceived_velocity = pygame.math.Vector2()

        for boid in other_boids:
            if boid != self:
                perceived_velocity = perceived_velocity + boid.speed

        perceived_velocity = perceived_velocity / (len(other_boids) - 1)

        return (perceived_velocity - self.speed) / math.exp(5)

    def dodge_walls(self):

        away_from_wall_x = 0
        away_from_wall_y = 0

        pos = self.get_pos_vector()

        if pos[0] <  50:
            away_from_wall_x = 1
        elif pos[0] > self.screen.get_width() - 50:
            away_from_wall_x = -1

        if pos[1] < 50:
            away_from_wall_y = 1
        elif pos[1] > self.screen.get_height() - 50:
            away_from_wall_y = -1

        return pygame.math.Vector2(away_from_wall_x, away_from_wall_y) / 5

    def update_movement(self):
        """
        Oppdater speed vektor, update tar resten
        """

        max_speed = 5

        center_movement = self.toward_center(instanser)
        avoid_movement = self.avoid_obstacle(instanser)
        match_movement = self.match_velocity(instanser)
        dodge_movement = self.dodge_walls()

        self.speed = self.speed + center_movement + avoid_movement + match_movement + dodge_movement
        #self.speed = self.speed + center_movement + match_movement + dodge_movement
        #self.speed = self.speed + dodge_movement

        if self.speed.length() > max_speed:
            self.speed = (self.speed / self.speed.length()) * max_speed
        #self.speed = self.speed + avoid_movement

# ==============
# Simulation vars
# ==============
def make_boids(n, width, height):

    instanser = []

    for i in range(n):

        # random spawn
        x = random.randint(1, width)
        y = random.randint(1, height)
        position = pygame.math.Vector2(x, y)

        sped_x = random.randint(-3, 3)
        sped_y = random.randint(-3, 3)

        speed = pygame.math.Vector2([sped_x,sped_y])

        b = boid(position, speed, "red", 5)
        instanser.append(b)

    return instanser

screen = pygame.display.set_mode(size)

instanser = make_boids(100, screen.get_width(), screen.get_height())
print (instanser[0].rect[:2])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    for b in instanser:
        pygame.draw.rect(screen, red, b.rect)

        b.update_movement()
        b.update()

    pygame.display.flip()

    clock.tick(30)
