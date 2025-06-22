#stein saks oaoir spill elller no
import random

valg = input("Stein, Saks, Papir!: ")

#funk for ssp
# tar in skrift der bruker skriver "Stein" f.eks.
# dette ender nok opp i en kontekst hvor liste over verider er definert
# håndterer det her for     
def spill(valg):
    
    #mulige output
    liste = ["Stein", "Saks", "Papir"]
    verdier = [0,1,2]

    # gjør om valget til spiller fra tekst til tall
    

    # pc velger random valg
    tall = random.randint (1, len(liste))
    npc = verdier[tall]

    # sammenlikning av de to valgene


# - Skriver in valg
# - Sammenlikner de to