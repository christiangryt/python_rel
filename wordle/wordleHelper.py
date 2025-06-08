from wordleBOT import wordleBOT

bot = wordleBOT()

for i in range (10):

    # forslag til løsnings ord
    forslag = bot.findGuess()
    print (forslag)

    # bruker skriver in gjettet ord og resulterende tall verdier (0,1,2)
    # man kan altså også gjette andre ord enn som blir foreslått
    gjett = input ("Skriv inn gjettet ord: ")
    gjett.strip()

    resString = input("Skriv inn tall verdiene for resultatet (typ 22001): ")
    resultat = [int(char) for char in resString]

    bot.updateState(gjett, resultat)
