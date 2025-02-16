import sys, pygame
import numpy as np

def distance_to_edges(rect, width, height):
    left_dist = rect.left  # Distance to left edge (x = 0)
    right_dist = width - rect.right  # Distance to right edge
    top_dist = rect.top  # Distance to top edge (y = 0)
    bottom_dist = height - rect.bottom  # Distance to bottom edge
    
    return left_dist, right_dist, top_dist, bottom_dist

pygame.init()               # starte opp pygame

size = width, height = 1020, 840# klink måte å definere flere varibler
speed = pygame.math.Vector2(1,2)
black = (0,0,0)
white = (255,255,255)

screen = pygame.display.set_mode(size)

# definere ball greier
ball_radius = 30
ball_pos = pygame.math.Vector2(width // 2, height // 2)
#ball_pos = [0, 0]

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # oppdatere posisjon
    ball_pos[0] += speed[0]
    ball_pos[1] += speed[1]

    #finner avstand til nærmeste vegg??
    #vecTilVegg = pygame.math.Vector2(min(ball_pos[0], width - ball_pos[0]), min(ball_pos[1], height - ball_pos[1]))

    # vektor til hver vegg
    v1 = pygame.math.Vector2(ball_pos[0], 0)
    v2 = pygame.math.Vector2(ball_pos[0], height)
    v3 = pygame.math.Vector2(0, ball_pos[1])
    v4 = pygame.math.Vector2(width, ball_pos[1])

    screen.fill(black)

    # unngå alle samtidig, nærmere unngår man mer (kjempe dumt men bare for å teste)
    for v in [v1,v2,v3,v4]:

        # avstand mellom ball og vegg
        avs = v - ball_pos
        pygame.draw.line(screen, white, ball_pos, avs)
        # normaliserer avs vektor
        if avs:
            vekkFraVegg = pygame.math.Vector2.normalize(avs)

        # hvor hardt man skal unngå noe
            #vekkKraft = vekkFraVegg * speed
            #speed += vekkFraVegg * speed

    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius> width:
        speed[0] = -speed[0]
    if ball_pos[1] - ball_radius< 0 or ball_pos[1] + ball_radius > height:
        speed[1] = -speed[1]

    pygame.draw.circle(screen, white, ball_pos, ball_radius, 0)         # dette er en rektangel surface med en sirkel inni
    pygame.draw.line(screen, black, ball_pos, ball_pos + speed*ball_radius)
    pygame.draw.line(screen, white, ball_pos, [ball_pos[0], 0])
    pygame.draw.line(screen, white, ball_pos, [ball_pos[0], height])
    pygame.draw.line(screen, white, ball_pos, [0, ball_pos[1]])
    pygame.draw.line(screen, white, ball_pos, [width, ball_pos[1]])

    pygame.display.flip()

    clock.tick(60)