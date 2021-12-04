import pygal
from die import Die

# Define variables
die_1 = Die(8)
die_2 = Die(8)

# Apply functions
results = []

for i in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# Visualize Frequencies

# What numbers can we expect? 
min_value = 2
max_value = die_1.num_sides + die_2.num_sides

frequencies = []
for value in range(min_value, max_value+1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Visualize frequencies
hist = pygal.Bar()
hist._title = "Results of rolling two D8 1000 times"
hist.x_labels = []
for i in range(min_value, max_value + 1):
    hist.x_labels.append(i)
hist._x_title = "Results"
hist._y_title = "Frequency of Results"
hist.add('D8 + D8', frequencies)
hist.render_to_file('die_visual4_D8.svg')
