import pygal
from die import Die

# Create an instance
die_1 = Die()
die_2 = Die(10)

# Define variables to store results (possible combinations)
results = []

# roll dice
for i in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Look through results and count frequencies
min_possible_result = 2 #(die_1 rolls 1 and die_2 rolls 1)
max_possible_result = die_1.num_sides + die_2.num_sides #( die_1 rolls 6 and die_2 rolls 10)

frequencies = []
for value in range(min_possible_result, max_possible_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize Frequencies
hist = pygal.Bar()
hist._title = "Results of rolling a D6 and D10 die 50,000 times"
# Generate the labels with a for loop 
hist.x_labels = []
for value in range(min_possible_result, max_possible_result+1):
    hist.x_labels.append(value)
hist._x_title = "Results"
hist._y_title = "Frequency of Results"
hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual3.svg')

