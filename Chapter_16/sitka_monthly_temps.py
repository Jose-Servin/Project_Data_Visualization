import csv
import matplotlib.pyplot as plt 
from datetime import datetime

# Import csv file 
file  = 'Chapter_16/sitka_weather_07-2014.csv'
with open(file) as f:
    reader = csv.reader(f) # creates an object with the csv data 
    header_row = next(reader)
    print(header_row)

# Read index values and headers 
    for index, header_name in enumerate(header_row):
        print(index, header_name)
# data exploration will now follow columns with index 0 and 1 (AKDT and Max TemperatureF)

# Extract max temperature from the csv object created and store it in a list as integers
    max_temps = []
    dates = []
    for row in reader:
        date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(date)

        temp = int(row[1])
        max_temps.append(temp) # max_temps are the row values from column 1 in the reader object

    
# Plot temperature data 
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, max_temps, c='red')
plt.title("Daily High Temperatures, July 2014", fontsize=24)
plt.ylabel("Temperature (F)", fontsize=15)
plt.xlabel("Date")
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major',labelsize=16)
plt.show()