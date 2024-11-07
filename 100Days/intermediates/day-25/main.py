 # Method to output a SINGLE list with multiple items
with open("./100Days/intermediates/day-25/weather_data.csv") as weather_conditions:
    data = [line.rstrip() for line in weather_conditions]
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
    # print(temperatures)

import pandas as pd

df = pd.read_csv("./100Days/intermediates/day-25/weather_data.csv")
# print(df["temp"])

# print(df["day"])

# data_dict = df.to_dict()
# print(data_dict)

# temp_list = df["temp"].to_list()
# print(temp_list)
# print(len(temp_list))

# print(df["temp"].max())

#Get data in rows
# print(df[df.day == "Monday"])

# Get row with highest temp
# print(df[df.temp == df.temp.max()])
monday = df[df.day == "Monday"]
# print(df)
def c_to_f(temp_c):
    return (temp_c * 1.8) + 32
print(c_to_f(monday.temp.iloc[0]))
