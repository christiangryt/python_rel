import sys, pygame
import numpy as np
import boid
import random as r

pygame.init()               # starte opp pygame

size = width, height = 1020, 840# klink måte å definere flere varibler

# Vektor vekk fra vegg
def vegg_vektor(width, height, pos):

    ut = (0,0)

    posX, posY = pos

    if width//2 - posX > 0:
        ut[0] = min(1, 1 / posX)
    else:
        ut[0] = min(1, 1 / (posX - width))  # her er width > posX -> ut[0] < 0

    if height//2 - posY > 0:
        ut[1] = min(1, 1 / posY)
    else:
        ut[1] = min(1, 1 / (posY - height))

    return ut

# TEST KODE FRA CHAT
import math
def vinkel_mellom(v1, v2):
    """ Returnerer vinkelen mellom to vektorer i grader """
    dot_product = v1.x * v2.x + v1.y * v2.y  # Skalarprodukt
    length_v1 = math.sqrt(v1.x**2 + v1.y**2)
    length_v2 = math.sqrt(v2.x**2 + v2.y**2)

    if length_v1 == 0 or length_v2 == 0:
        return 0  # Unngå deling på null

    cos_theta = dot_product / (length_v1 * length_v2)  # Cosinus til vinkelen
    cos_theta = max(-1, min(1, cos_theta))  # Unngå numeriske feil

    return math.degrees(math.acos(cos_theta))

# LAGER TEST BOID
spdVek = pygame.math.Vector2([3,1])
bb = []

for i in range (1, 30):

    pos1 = r.randint(40, width - 40)
    pos2 = r.randint(40, height- 40)

    spd = pygame.math.Vector2(1,2)
    spd.rotate_rad_ip(np.floor(r.randint(0, np.floor(2*np.pi))))

    spd = pygame.math.Vector2(spd)
    pos = pygame.math.Vector2(pos1, pos2)

    # ny = boid.boid(pygame.math.Vector2(1,2), [width / (i + 10), height / (i + 10)], 150, 0.02, 100, (0,255,0))
    ny = boid.boid(spd, pos, 100, 0.05, 100, (0,255,0), 100)

    bb.append(ny)

# temp funk sjekker pos utenfor kart
# bruker globale definsjoner ro ned
def utenfor_sjekk(pos):

    if pos[0] <= 0 or pos[0] >= width or pos[1] <= 0 or pos[1] >= height:
        return True
    
    else: 
        return False

speed = pygame.math.Vector2(0 ,2)
#speed = pygame.math.Vector2(0,0)

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

screen = pygame.display.set_mode(size)

# definere ball greier
# ball_radius = 30
# ball_pos = pygame.math.Vector2(width // 2, height - 100)
#ball_pos = [0, 0]

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # oppdatere posisjon
    # ball_pos[0] += speed[0]
    # ball_pos[1] += speed[1]
    # for b in bb:

    #     b.position += b.speed

    #finner avstand til nærmeste vegg??
    #vecTilVegg = pygame.math.Vector2(min(ball_pos[0], width - ball_pos[0]), min(ball_pos[1], height - ball_pos[1]))

    screen.fill(white)

    # sjekk mulige ruter ved stråler
    # looper over ball_pos + speed, ser om den lander utenfor banen
    # om den gjør det, vri vektoren hakk til venstre eller høyre gjenta

    # burde ta høyde for retning og ikke bare hastighet? ellers er syns lengde ubrukelig
    # low key kanskje bedre sånn

    # antallForsok = 10
    # rotMengde = 0.1    # radian
    # synLengde = ball_radius * 9
    # test_retning = pygame.math.Vector2(speed)

    pygame.draw.circle(screen, red, (width //2, height //2), 20)

    for b in boid.boid.instanser:   

        b.position[0] += b.speed[0]
        b.position[1] += b.speed[1]

        test_retning = pygame.math.Vector2(b.speed)

        midtpunkt = pygame.math.Vector2(width // 2, height // 2)
        veggRetning = midtpunkt - b.position

        pygame.draw.line(screen, red, b.position, b.position - veggRetning)

        # vinkel mellom speed og midten
        # vinkel = b.speed.angle_to(veggRetning)
        vinkel = min(vinkel_mellom(b.speed, veggRetning) * (veggRetning.magnitude() - veggRetning.magnitude_squared()) * 0.00001, 1)

        b.speed.rotate_ip(vinkel)
        pygame.draw.line(screen, black, b.position, b.position + b.speed*10)

        # prøve noe annet for å unngå vegger
        """
        for prov in range(1, b.forsok):

            futurePos = b.position + test_retning.normalize() * (b.radius + b.synlen)

            pygame.draw.line(screen, red, b.position, futurePos)

            # print(utenfor_sjekk(futurePos))

            if utenfor_sjekk(futurePos):

                if prov % 2 == 1:

                    test_retning.rotate_rad_ip(b.rotmen * prov)

                else:

                    test_retning.rotate_rad_ip(b.rotmen * -prov)

                # roterer en så en annen ved mod
                # roter speed og prøv igjen

                # print (test_retning)
                # pygame.draw.line(screen, red, b.position, b.position + test_retning)

            else:

                b.speed = test_retning
                break
        """

        lagring = b.seperation()

        pygame.draw.circle(screen, b.color, b.position, b.radius, 0)

        # DEBUG
        pygame.draw.line(screen, red, b.position, b.position - lagring)

    # vektor til hver vegg
    # v1 = pygame.math.Vector2(ball_pos[0], 0)
    # v2 = pygame.math.Vector2(ball_pos[0], height)
    # v3 = pygame.math.Vector2(0, ball_pos[1])
    # v4 = pygame.math.Vector2(width, ball_pos[1])

    # # unngå alle samtidig, nærmere unngår man mer (kjempe dumt men bare for å teste)
    # for v in [v1,v2,v3,v4]:

    #     # avstand mellom ball og vegg
    #     avs = v - ball_pos
    #     pygame.draw.line(screen, white, ball_pos, avs)
    #     # normaliserer avs vektor
    #     if avs:
    #         vekkFraVegg = pygame.math.Vector2.normalize(avs)

    #     # hvor hardt man skal unngå noe
    #         #vekkKraft = vekkFraVegg * speed
    #         #speed += vekkFraVegg * speed

    # if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius> width:
    #     speed[0] = -speed[0]
    # if ball_pos[1] - ball_radius< 0 or ball_pos[1] + ball_radius > height:
    #     speed[1] = -speed[1]

    # pygame.draw.circle(screen, black, ball_pos, ball_radius, 0)         # dette er en rektangel surface med en sirkel inni
    # pygame.draw.line(screen, red, ball_pos, ball_pos + speed*ball_radius)
    # pygame.draw.line(screen, white, ball_pos, [ball_pos[0], 0])
    # pygame.draw.line(screen, white, ball_pos, [ball_pos[0], height])
    # pygame.draw.line(screen, white, ball_pos, [0, ball_pos[1]])
    # pygame.draw.line(screen, white, ball_pos, [width, ball_pos[1]])

    pygame.display.flip()

    clock.tick(30)
