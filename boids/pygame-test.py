import pygame, sys
import numpy as np

# teste vinkel mellom pygame vektorer (burde vel nesten bare begynne å bruke numpy elr no)

pygame.init()

size = width, height = 1020, 840

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

screen = pygame.display.set_mode(size)

screen.fill(white)


t1 = pygame.math.Vector2(700, 500)
t2 = pygame.math.Vector2(650, 800)

vink = t1.angle_to(t2)

pygame.draw.line(screen, red, [0,0], t1)
pygame.draw.line(screen, black, [0,0], t2)

minAvstandX = t1[0] - np.ceil(width / 2)
minAvstandY = t1[1] - np.ceil(height / 2)

midten = pygame.math.Vector2(minAvstandX, minAvstandY)

mot = pygame.math.Vector2(t1 + midten)

pygame.draw.line(screen, red, [0,0], mot)

print (vink)

pygame.display.flip()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()