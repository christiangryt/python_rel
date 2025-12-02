start_nummer = 50

def vri(f, op):

    fortegn = op[0]
    tall = int(op[1:])

    if fortegn == "L":
        ny = (f - tall) % 100

    elif fortegn == "R":
        ny = (f + tall) % 100

    if ny == 0:
        return ny, 1

    return ny, 0


with open('data-real.txt') as f:
    forrige = start_nummer
    antall_null = 0

    while (rad := f.readline()):
        ny, null = vri(forrige, rad)

        antall_null += null
        forrige = ny

    print (antall_null)
