import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Import file
file_path = ('Chapter_16/sitka_weather_2014.csv')
with open(file_path) as file:
    reader = csv.reader(file)
    headers = next(reader)
    print(headers)

# Get max temperature data and date data from reader object
    max_temps = []
    min_temps = []
    dates = []
    for row in reader:
        temp_max = int(row[1])
        max_temps.append(temp_max)

        temp_min = int(row[3])
        min_temps.append(temp_min)

        row_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(row_date)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, max_temps, c='red')
plt.plot(dates, min_temps, c='blue')
plt.fill_between(dates, max_temps, min_temps, facecolor = 'blue', alpha = 0.1)
plt.title("Yearly Sitka Max and Min Temperatures for 2014")
plt.xlabel("Date")
plt.ylabel("Max and Min Temperature F")
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim((0,120))
plt.show()