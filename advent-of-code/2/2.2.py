def parse_input(arg):
    start, end = arg.split("-")
    return int(start), int(end)

def find_repeated(start, end):

    s = 0

    for n in range(start, end + 1):

        streng_n = str(n)
        lengde_streng_n = len(streng_n)

        for i in range(1, lengde_streng_n // 2 + 1):

            antall_del_ord = lengde_streng_n % i

            suspect = streng_n[:i]

            print(suspect)

    return s

find_repeated(95, 105)
