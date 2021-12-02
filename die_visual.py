import pygal
from die import Die

# Create an instance 
my_dice = Die()

# Define variable to store results
results = []
# Process
for i in range(1000):
    rolled_num = my_dice.roll()
    results.append(rolled_num)

# Analyze the results
frequencies = []
possible_values = list(range(1, my_dice.num_sides+1))
for value in possible_values:
    frequency = results.count(value) # referencing results list created above
    frequencies.append(frequency)
print(frequencies)

# Visualize frequencies
hist = pygal.Bar()

hist._title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist._x_title = "Results"
hist._y_title = "Frequency of Results"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')


