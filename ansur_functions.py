import csv
import numpy

def cords_gen(measurement1, measurement2, dataset):
    cords = []
    with open (dataset) as ansur:
        csvfile = csv.reader(ansur)
        measurements = next(csvfile)
        loc1 = measurements.index(measurement1)
        loc2 = measurements.index(measurement2)
        for row in csvfile:
            temp = []
            temp.append(int(row[loc1]))
            temp.append(int(row[loc2]))
            cords.append(temp)
    return cords

def list_gen(measurement, dataset):
    list1 = []
    with open (dataset) as ansur:
        csvfile = csv.reader(ansur)
        measurements = next(csvfile)
        loc = measurements.index(measurement)
        for row in csvfile:
            list1.append(int(row[loc]))
    return list1

def ratio_gen(cords):
    list1 = []
    for item in cords:
        list1.append(item[0]/item[1])
    return list1

def avg_and_sd_calc(inputlist):
    sd = numpy.std(inputlist)
    total = 0
    for item in inputlist:
        total += item
    avg = total/len(inputlist)
    return sd, avg

def print_line():
    return " ------------------------------------------------------------------------------------------------------------------------------------------"

def fourty_lines():
    return "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

def blank_line():
    return " |                                                                                                                                        |"

def better_print(input_string):
    add_spaces = (137-len(input_string))//2
    counter = add_spaces
    output_string = " |"
    for x in range(counter):
        output_string += " "
    output_string += input_string
    counter = add_spaces
    while len(output_string) != 138:
        output_string += " "
    output_string += "| "
    #print(len(output_string))
    return output_string


def resize():
    print(f"{print_line()}")
    for x in range(10):
        print(better_print(' '))
    print(f"{better_print('Expand/resize your window until this box just fits inside it with no spaces between each vertical line, then press enter.')}")
    for x in range(10):
        print(better_print(' '))
    print(f"{print_line()}")
    
    return