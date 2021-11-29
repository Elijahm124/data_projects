#import pyplot & random walk class
import matplotlib.pyplot as plt
from random_walk import RandomWalk

#make a random walk instance
rw = RandomWalk()

#call method in random walk class, fill_walk, for instance rw
rw.fill_walk()

#plot points in the walk
plt.style.use("classic")
fig, ax = plt.subplots()

#create a scatter plot with instance's random x & y values
#size of dots is 15
ax.scatter(rw.x_values, rw.y_values, s = 15)

plt.show()

