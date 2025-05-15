from collections import defaultdict

def countInstances():

    # returnere et dict
    ut = defaultdict(lambda: defaultdict(int))

    with open("words.txt", "rb") as f:

        # leser hver linje til filen er ferdig
        while (line := f.readline()):

            for i, letter in enumerate(line.strip()):

                ut[i][chr(letter)] += 1

    return ut

dd = countInstances()

sortert = {
    nummer: dict(sorted(verdi.items()))
    for nummer, verdi in dd.items()
}

# antall ord = antall bokstaver i hver kolonne
tot_ord = 12915

# teste med ord og vektefunksjon
testORD = "PLATE"

#print(sortert)
best = ""
score = 0

with open("words.txt", "rb") as f:

    while (line := f.readline()):

        total = 0
        for i, letter in enumerate(line.strip()):

            # finner forholdet mellom bokstav/total
            antall = dd[i][chr(letter)]
            forhold = antall/tot_ord

            total += 4*forhold - 4*forhold**2

        if total > score:

            best = line.strip()
            score = total

print (best)
print (score)
