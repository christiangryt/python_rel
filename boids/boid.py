import pygame
import math 

class boid(pygame.sprite.Sprite):
    '''
    Klasseobjekt som skal simulere flokk bevegelser
    '''

    def __init__(self, speed, position, synlen, rotmen, forsok, color):
        '''
        Ny boid tar in hastighet (vektor), posisjon (vektor) og en farge (hex elr no)
        '''

        self.radius = 10                         # hitbox tall TODO gjør noe samrtere

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
        self.forsok = math.ceil(2*math.pi / rotmen)    # hvor mange stråler

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