from die import Die

from die import Die
import matplotlib.pyplot as plt


die_1 = Die()
die_2 = Die()

results = []
for i in range(5000):
    result  = die_1.roll() + die_2.roll()
    results.append(result)


# count the frequency of values in results
frequencies = []
min_value = 2
max_value = die_1.num_sides + die_2.num_sides

for value in range(min_value, max_value+1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Graph results using matplotlib

x_values = []
for i in range(min_value, max_value+1):
    x_values.append(i)


plt.xlabel=(" Number rolled")
plt.ylabel = ("Frequency of number rolled")
plt.bar(x_values, frequencies)
plt.show()