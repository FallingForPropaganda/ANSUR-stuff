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

def line_of_best_fit(coordinates):
    x_total = 0
    y_total = 0
    total = 0
    for item in coordinates:
        x_total += item[0]
        y_total += item[1]
        total += 1
    x_average = x_total/total
    y_average = y_total/total
    
    x_minus_x_average = []
    y_minus_y_average = []
    for item in coordinates:
        x_minus_x_average.append(item[0] - x_average)
        y_minus_y_average.append(item[1] - y_average)

    x_y = 0
    x_x = 0
    counter = 0
    while counter != len(coordinates):
        x_x += (x_minus_x_average[counter] * x_minus_x_average[counter])
        x_y += (x_minus_x_average[counter] * y_minus_y_average[counter])
        counter += 1
    slope = x_y/x_x
    
    b = y_average - slope*x_average

    return slope, b