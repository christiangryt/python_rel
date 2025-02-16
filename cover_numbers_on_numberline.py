#ta inn en liste med punkter (ikke nødvendigvis heltall)
#ha en gitt lengde stav e.l. for å legge over tallinjen
#hvor få staver kan man bruke for å dekke alle tallene
#innenfor et interval, så det er ikke evig langt
#staver kan ikke overlappe

#A = liste med tall
#l = lengde på stav
#output = start koordinater for hver stav
import math


def cover_numbers_on_numberline(A, l):

    #liste med startpunkt for stav
    s = []

    #forgje lagt stav startkoordinat
    f = -math.inf

    for i in A:
        #sjekker om den er dekket av en stav 
        if  f + l >= i:
            continue
        else:
            f = i
            s.append(f)


    return s

# A = [1,3,4,4.11,4.23,5.22,5.5,5.76,6.66]
# l = 1

# print(cover_numbers_on_numberline(A, l))