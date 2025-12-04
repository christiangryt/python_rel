word_length = 12
global_cool_counter = 0

def joltage(array, max_depth=word_length):

    global global_cool_counter

    #print (f"{array}")
    max_voltage = max(array)
    #print (f"{max_voltage} i {depth}")
    global_cool_counter += 1

    if global_cool_counter < max_depth:

        array_len = len(array)
        max_index = array.find(max_voltage)

        hoyre = array[max_index + 1:]
        venstre = array[:max_index]
        #print (f"{hoyre} og {venstre}")

        vv, hh = "", ""

        if len(hoyre) != 0:

            hh = joltage(hoyre)
            #print (f"{global_cool_counter} {hh}")

        if len(venstre) != 0 and global_cool_counter < max_depth:

            vv = joltage(venstre)
            #print (f"{global_cool_counter} {vv}")


        return vv + max_voltage + hh

    else:
        return max_voltage

#print(joltage("987654321111111"))

with open("data.txt") as f:

    s = 0

    while (rad := f.readline().strip()):

        #rad = list(rad)
        volt = joltage(rad)
        print(volt)

        s += int(volt)

        global_cool_counter = 0

    print (s)
