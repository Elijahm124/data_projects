import matplotlib.pyplot as plt
from random_walk import RandomWalk

#as long as i say yes, code generates a new random walk visual
while True:

    #change 5000 to 50,000 for this specfic instance for
    # number of points (5000 is OG parameter value)
    rw = RandomWalk(50_000)

    #call function which makes list of x & y values
    rw.fill_walk()

    plt.style.use("classic")

    #alter size of entire figure so points can fit screen better
    #fig size takes tuple as dimensions of screen
    fig, ax = plt.subplots(figsize=(15,9))

    #create a list of numbers from 0 - 4999
    #0-4999 is basis for colormap shift
    point_numbers = range(rw.num_points)

    #create scatterplot based on list of values
    #list of numbers is basis for colormap change
    #as point_number(1,2,3..etc) increases, color progressively becomes darker Blue
    #no edge coloring because we passed None
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolors="none", s = 1)

    #emphasize first point, always gonna be (0,0)
    #distinct green and 100 size
    #this function plots the value as a scatterplot point
    ax.scatter(0,0,c="green", edgecolors="none", s=100 )

    #emphsize last point
    #always gonna be last x & y value from list (-1)
    #distinct red and 100 size
    #this function plots the value as a scatterplot point
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red",
               edgecolors="none", s = 100)

    #remove the axes
    #get_axis is a specific method
    #set visible is false which means to turn off axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    #create input variable
    keep_running = input("Make another walk? (y/n): ")

    #end while loop if i say no
    if keep_running == "n":
        break

#when loop runs, i have to quit figure to get option of new figure