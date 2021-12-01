import matplotlib.pyplot as plt
from Random_Walk import RandomWalk

while True:
# Make a random walk and plot the points
    rw = RandomWalk() # creating a Class instance 
    rw.fill_walk() # using the fill_walk() method
    plt.scatter(rw.x_values, rw.y_values, s=5)
    plt.show()

    keep_running = input("Do you want to generate a new graph? y/n ")
    if keep_running == 'n':
        break
    

