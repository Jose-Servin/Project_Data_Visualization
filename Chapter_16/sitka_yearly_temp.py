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
    dates = []
    for row in reader:
        temp = row[1]
        max_temps.append(temp)

        row_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(row_date)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, max_temps, c='red')
plt.title("Yearly Sitka High Temperature")
plt.xlabel("Date")
plt.ylabel("High Temperature F")
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()