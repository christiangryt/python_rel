
class boid():
    '''
    Klasseobjekt som skal simulere flokk bevegelser
    '''

    def __init__(self, speed, position, color):
        '''
        Ny boid tar in hastighet (vektor), posisjon (vektor) og en farge (hex elr no)
        '''

        self.speed = speed
        self.position = position            # kan sette denne manuelt, eller bare mate den med coords om man skal spawne nye
        self.color = color
        self.radius = 25                    # før jeg lager en ordentlig sprite bruker jeg bare en sirkel

