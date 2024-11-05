# Method to output a SINGLE list with multiple items
# with open("./100Days/intermediates/day-25/weather_data.csv") as weather_conditions:
#     data = [line.rstrip() for line in weather_conditions]
# print(data)

import csv

with open("./100Days/intermediates/day-25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        temperatures.append(row[1])
        # print(row)
    temperatures.pop(0)
    temperatures = [int(value) for value in temperatures]
    print(temperatures)