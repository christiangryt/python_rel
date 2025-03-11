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

        #sum av avstander til alle andre boids
        # fant feilen, ved å referere til self.speed lager jeg ikke en kopi av speed, men jeg peker på samme objekt, altså vil hastigheten til boiden øke
        mellom = self.speed.copy()

        for b in boid.instanser:            # alle boids

            # mellom = pygame.math.Vector2(self.speed)

            # om jeg sjekker meg selv forkaster jeg
            if self == b:
                continue

            # avstand mellom 2 boid
            diffPos = self.position - b.position
            avstand = (diffPos.magnitude_squared() + self.radius) * 0.001

            # Ved å sette denne til - blir de trukket mot hverandre
            # mindre avstand dytter mer
            mellom += diffPos / avstand

        #vinkel mellom ny retning og speed Vec2 akk nå
        vinkel_mellom = vinkelMellom(self.speed, mellom)

        # angle_to GIR RARE VINKLER
        # vinkel_mellom = self.speed.angle_to(mellom)

        # skalerer vinkel med lengden på mellom, men aldri mer enn 1
        # rot_faktor = min(1, mellom.magnitude_squared() / 1690000)
        rot_faktor = 0.05

        self.speed.rotate_ip(vinkel_mellom * rot_faktor)

        # avstands vektor
        #avstandsVektor += mellom * (1 / avstand)
        # print (avstandsVektor)

        #vinkelKraft = self.speed.angle_to(avstandsVektor.normalize())

        # DEBUG
        return mellom

        # self.speed += avstandsVektor.normalize() * 0.05
        # skalerer vinkel med avstand
        #vinkelKraft *= 0.05

        #roterer speed med så mye

        # DENNE ER DOOKIE FORDI DEN BARE VRIR SEG SAMME VEG
        # FINN EN MÅTE Å FINNE KORTESTE VINKEL
        #self.speed.rotate_ip(vinkelKraft)

        # return avstandsVektor
