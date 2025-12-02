import re

def parse_input(arg):
    start, end = arg.split("-")
    return int(start), int(end)

def find_repeated(start, end):

    s = 0

    for n in range(start, end + 1):

        streng_n = str(n)
        lengde_streng_n = len(streng_n)
        max_window_size = lengde_streng_n // 2 + 1

        for i in range(1, max_window_size):

            gor_opp = lengde_streng_n % i
            if gor_opp == 0:

                suspect = re.findall(i * '.', streng_n)

                suspect_set = set(suspect)

                if len(suspect_set) == 1:
                    s += n
                    break
    return s

with open('data.txt') as f:

    ss = 0

    rad = f.readline()
    id = rad.split(",")

    for i in id:
        start, slutt = parse_input(i)
        ss += find_repeated(start, slutt)

    print(ss)
