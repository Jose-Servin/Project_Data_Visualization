import pygal
from die import Die

# Create an instance 
die_1 = Die()
die_2 = Die()

# Define variable to store results
results = []
# Process
for i in range(1000):
    rolled_num_1 = die_1.roll()
    rolled_num_2 = die_2.roll()
    result = rolled_num_1 + rolled_num_2
    results.append(result)

# Analyze the results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides # this returns 1 integer (12 in this case)
for value in range(2,max_results+1): # starting at 2 because min value for die 1 and 2 is 1 (1+1)
    frequency = results.count(value) # referencing results list created above
    frequencies.append(frequency)
print(frequencies)

# Visualize frequencies
hist = pygal.Bar()

hist._title = "Results of rolling two D6 1000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist._x_title = "Results"
hist._y_title = "Frequency of Results"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual2.svg')


