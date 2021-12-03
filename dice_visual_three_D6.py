import pygal
from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

# Apply function(s)

results = []
for number in range(1000):
    rolled_number = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(rolled_number)

# count frequencies
frequencies = []
min_value = 3
max_value = die_1.num_sides + die_2.num_sides + die_3.num_sides

for value in range(min_value, max_value+1):
    frequency_of_num = results.count(value)
    frequencies.append(frequency_of_num)

# Visualize frequencies
hist = pygal.Bar()
hist._title = "Results of rolling three D6 1000 times"
hist.x_labels = []
for i in range(min_value, max_value + 1):
    hist.x_labels.append(i)
hist._x_title = "Results"
hist._y_title = "Frequency of Results"
hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_visual_three_D6.svg')