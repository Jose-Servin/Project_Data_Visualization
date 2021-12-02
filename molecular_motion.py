import matplotlib.pyplot as plt
from Random_Walk import RandomWalk

while True:
# Make a random walk and plot the points
    rw = RandomWalk() # creating a Class instance 
    rw.fill_walk() # using the fill_walk() method

    # Introducing a colormap 
    plt.plot(rw.x_values, rw.y_values, linewidth=.5)

    # Emphasize starting and ending point
    plt.scatter(0,0, s=25, c='green')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], s=25, c='red')

    plt.axis('off')

    plt.show()

    keep_running = input("Do you want to generate a new graph? y/n ")
    if keep_running == 'n':
        break
    

