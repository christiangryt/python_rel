import pygame
from tree import node

"""
Make nodes to display
"""

n1 = node()

"""
Pygame setup
"""
pygame.init()

#Screen size
x = 1280
y = 720

screen = pygame.display.set_mode((x, y))

#Uvisst om jeg trenger klokke for å displaye en gang
clock = pygame.time.Clock()
#samme med denne
running = True

#font for text
font = pygame.font.Font('freesansbold.ttf', 12)

text = font.render(str(n1.value), True, "black", None)

#get rectangle for text surface
textRect = text.get_rect()

# set center of rect to center of circle
textRect.center = (10, 10)

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill screen to wipe
    screen.fill("white")

    # DRAW TREE
    circ = pygame.draw.circle(screen, "black", (10, 10), 10, 2)

    screen.blit(text, textRect)

    pygame.display.flip()

    clock.tick(1) #only need to draw once so make this very low

pygame.quit()