def parse_input(arg):
    start, end = arg.split("-")
    return int(start), int(end)

def find_repeated(start, end):

    s = 0

    for n in range(start, end + 1):
        num_len = len(str(n))

        if num_len % 2 == 0:

            halv = str(n)[:int(num_len / 2)]
            andre = str(n)[int(num_len / 2):]

            #print (halv)
            if halv == andre:
                s += n

                print (n)

    return s

#print(parse_input("11-22"))
#print(find_repeated(95, 115))

#print (find_repeated(824824821, 824824827))

with open("data.txt") as f:

    ss = 0

    rad = f.readline()
    id = rad.split(",")

    for i in id:
        start, slutt = parse_input(i)
        ss += find_repeated(start, slutt)

    print (ss)
