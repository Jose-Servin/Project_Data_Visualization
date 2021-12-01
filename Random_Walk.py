from random import choice
# Creating the RandomWalk() class
class RandomWalk():
    """A class to generate random walks"""
    def __init__(self, number_points=5000):
        """Initialize attributes of a walk"""
        self.number_points = number_points
        # Define starting position
        self.x_values = [0] # list to hold randomly generated x-values 
        self.y_values = [0] # list to hold randomly generated y-values
    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Walk until x_values have reached number_points
        while len(self.x_values) < self.number_points:

            # Decide what direction to go and what distance to travel
            x_direction = choice([1,-1]) # represents right or left
            x_distance = choice([0,1,2,3,4]) # pick from these options 
            x_step = x_direction * x_distance # how far you travel

            y_direction = choice([1,-1]) # represents up or down
            y_distance = choice([0,1,2,3,4]) # pick from these options 
            y_step = y_direction * y_distance # how far you travel 
            
            # Reject moves that go nowhere (how far you travel in both directions == 0)
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values 
            next_x = self.x_values[-1] + x_step # first run [-1] index x_position == 0
            next_y = self.y_values[-1] + y_step # first run [-1] index y_position == 0

            self.x_values.append(next_x)
            self.y_values.append(next_y)

