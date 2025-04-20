import pygame
import math 

# TEST KODE FRA CHAT
import math
def vinkelMellom(v1, v2):
    """ Returnerer vinkelen mellom to vektorer i grader """
    dot_product = v1.x * v2.x + v1.y * v2.y  # Skalarprodukt
    length_v1 = math.sqrt(v1.x**2 + v1.y**2)
    length_v2 = math.sqrt(v2.x**2 + v2.y**2)

    if length_v1 == 0 or length_v2 == 0:
        return 0  # Unngå deling på null

    cos_theta = dot_product / (length_v1 * length_v2)  # Cosinus til vinkelen
    cos_theta = max(-1, min(1, cos_theta))  # Unngå numeriske feil

    return math.degrees(math.acos(cos_theta))

class boid(pygame.sprite.Sprite):
    '''
    Klasseobjekt som skal simulere flokk bevegelser
    '''

    instanser = []                          # liste inneholder alle boid objekter

    def __init__(self, speed, position, synlen, rotmen, forsok, color, bubble):
        '''
        Ny boid tar in hastighet (vektor), posisjon (vektor) og en farge (hex elr no)
        '''

        self.radius = 10                    # hitbox tall TODO gjør noe samrtere

        pygame.sprite.Sprite.__init__(self) # pygame sprite constructor

        # SPRITE SURFACE???
        self.image = pygame.Surface([self.radius, self.radius])
        self.image.fill(color)              # fyller sprite med gitt farge
        self.rect = self.image.get_rect()   # Sprite boks

        self.speed = speed                  # vektor
        self.position = position            # kan sette denne manuelt, eller bare mate den med coords om man skal spawne nye
        self.color = color                  # (x,y,z)
        self.synlen = synlen                # hvor langt boid skal bry seg (mtp hindringer)
        self.rotmen = rotmen                # radianer mellom hvert forsøk
        self.forsok = forsok
                                            # hvor mange stråler
        self.bubble = bubble                # avstand før boid tar unnvergelsesmanøver

        boid.instanser.append(self)         # legg seg selv til listen

        #før jeg lager en ordentlig sprite bruker jeg bare en sirkeller?)

    # sjekke om utenfor gitte grenser?
    def utenfor(self, vektor, kart):        # grov skisse
        '''
        vektor: speed rotert
        kart: vegger + evt hindringer

        Om nåværenede hastighets vektor vil føre til at jeg ender opp
        på et ulovlig sted

        Returnerer True om self.pos + vektor ulovlig
            False om ikke
        '''

    # sjekke avstand til naboer
    def seperation(self):
        '''
        Ser på alle andre boids og sjekker om de er for nærme.
        Om sant, styr unna
        '''

        mellom = self.speed.copy()

        for b in boid.instanser:            # alle boids

            # om jeg sjekker meg selv forkaster jeg
            if self == b:
                continue

            # avstand mellom 2 boid
            diffPos = self.position - b.position
            avstand = (diffPos.magnitude_squared() + self.radius) * 0.1

            # Ved å sette denne til - blir de trukket mot hverandre
            # mindre avstand dytter mer
            mellom += diffPos / avstand

        #vinkel mellom ny retning og speed Vec2 akk nå
        vinkel_mellom = vinkelMellom(self.speed, mellom)

        rot_faktor = 0.05

        self.speed.rotate_ip(vinkel_mellom * rot_faktor)
        # DEBUG
        return mellom
