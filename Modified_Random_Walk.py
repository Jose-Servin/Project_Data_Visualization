from random import choice

class RandomeWalkMod():
    """A class to generate a random walk with different parameters"""
    
    def __init__(self, number_of_points=50000):
        """Initialize attributes for walk"""
        self.number_of_points = number_of_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all the points in the walk"""
        while len(self.x_values) < self.number_of_points:

            # Decide what direction to go and what distance to travel
            x_direction = choice([1,-1]) 
            x_distance = choice([0,1,2,3,4,5,6,7,8])
            x_step = x_direction * x_distance

            y_direction = choice([1])
            y_distance = choice([0,1,2,3,4,5,6,7,8])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

            

