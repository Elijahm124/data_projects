#allow us to randomly decide what to do
from random import choice

class RandomWalk:
    "a class to generate random walks"

    #5000 is default number of steps to take
    #basically we have a max of 5000 steps
    def __init__(self, num_points=5000):
        """initialize attributes of a walk"""
        self.num_points = num_points

        #lists to store x & y values
        #all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all points in the walk"""

        #keep taking steps until walk reaches desired length
        #based only on amount of steps taken horizontally (x_values)
        #basically we can take 5000 steps hoirizontally, doesnt matter direction
        #doesnt matter if its len of x or y_values we just need a basis to reach 5000 steps
        while len(self.x_values) < self.num_points:

            #decide which direction to go & how far to go in that direction
            #choice function randomly chooses element from lists
            #we include zero so we can do single axis movement for one direction
            #direction of - or + indicates direction (-4, 3, -3)
            x_direction = choice([1, -1])
            x_distance = choice([0,1,2,3,4])

            #step = either positve movement, negative movment, or non movement
            #in a certain direction
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #reject moves that go nowhere
            #if both x & y dont move, we skip remainder of loop and start again
            #we don't include 0,0 values as countable moves
            if x_step == 0 and y_step == 0:
                continue

            #postion of x/y is based on previous position of x/y & indicated distance
            #self.valus[-1] cuz its the most recent x on list so its the current position
            x = self.x_values[-1] + x_step
            y= self.y_values[-1] + y_step

            #append new value of x/y so it can be new most recent position
            self.x_values.append(x)
            self.y_values.append(y)

            #as long as x list(or y list) doesnt have 5000 values, we append new values to be plotted
