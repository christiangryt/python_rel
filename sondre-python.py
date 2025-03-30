import random

# Konstanter
antallTerninger = 2000
antallKast = 0

# mens vi har terninger igjen
while antallTerninger > 0:

    # kast alle terninger
    for terning in range(antallTerninger):

        kast = random.randint(1,6)
        
        # sjekke om teringkast viste 6
        if kast == 6:

            antallTerninger -= 1

    # øk kast
    antallKast += 1

    # formidle statistikk
    print (f"Etter {antallKast} kast, har vi {antallTerninger} terninger igjen")