import matplotlib.pyplot as plt
from Random_Walk import RandomWalk

while True:
# Make a random walk and plot the points
    rw = RandomWalk(50000) # creating a Class instance 
    rw.fill_walk() # using the fill_walk() method

    # Introducing a colormap 
    point_numbers = list(range(rw.number_points))
    plt.scatter(rw.x_values, rw.y_values, c =point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=3)

    # Emphasize starting and ending point
    plt.scatter(0,0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s= 50)

    plt.axis('off')

    plt.show()

    keep_running = input("Do you want to generate a new graph? y/n ")
    if keep_running == 'n':
        break
    

