import numpy as np
import pygal
import ansur_functions as funcs


# Set the x and y coordinates
coordinates = funcs.cords_gen("HIP_BRTH", "STATURE", "ansur1_female.csv")

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Correlation'
xy_chart.add('A', coordinates)

#xy_chart.render_in_browser()

coordinates = coordinates[1:20]
#coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6]]
print(funcs.line_of_best_fit(coordinates))
#print(coordinates)
#print(funcs.avg_and_sd_calc(funcs.ratio_gen(coordinates)))


thing = [335, 1528], [350, 1567], [356, 1836], [358, 1546], [317, 1524], [364, 1836], [342, 1626], [320, 1549], [325, 1632], [324, 1662], [339, 1621], [318, 1648], [340, 1633], [325, 1646], [364, 1727], [399, 1636], [327, 1626], [334, 1568], [347, 1617]

x = [coord[0] for coord in thing]
y = [coord[1] for coord in thing]

#print(x, y)