def vri(f, op):

    fortegn = op[0]
    tall = int(op[1:])

    antall_vri = tall // 100
    rest_vri = tall - antall_vri*100

    if rest_vri == 0:
        return f, antall_vri

    else:

        if fortegn == "L":
            ny = (f - tall) % 100
            if (ny > f or ny == 0) and f != 0:
                antall_vri += 1
                print (f"{ny} > {f}. +1")

        elif fortegn == "R":
            ny = (f + tall) % 100
            if ny < f:
                antall_vri += 1
                print (f"{ny} < {f}. +1")
    return ny, antall_vri


start_nummer = 50

with open('data-real.txt') as f:
    forrige = start_nummer
    antall_null = 0

    while (rad := f.readline()):
        ny, null = vri(forrige, rad)

        antall_null += null
        forrige = ny

        print (antall_null)

    print (antall_null)
