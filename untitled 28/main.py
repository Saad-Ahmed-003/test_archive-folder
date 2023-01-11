import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature_number = []
    for row in data:
        print(row)
