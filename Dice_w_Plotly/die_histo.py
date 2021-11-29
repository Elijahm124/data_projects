from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die


die = Die()

#store results in list
results = []

#analyze the results
for roll_num in range(1000):
    result = die.roll()
    results.append(result)


#empty list to store values
frequencies = []

#for numbers 1-6, count their occurence in the list
#after that, store frequency for each value in list
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize results
#we already have a list of intended y values(frequencies)
#x_values is list of x values (1-6) to correspond to it's frequency
x_values = list(range(1, die.num_sides+1))

#call Bar class which takes list of x & y values
#Bar class represents a data set, thus why there's square brackets
#data set has multiple elements
data = [Bar(x=x_values, y=frequencies)]

#configuration of axes= setting title of each axis
x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of Result"}

#Layout class specifies layout and configuration of graph
#title of graph and axes are specified
my_layout = Layout(title="Results of rolling one D6 1000 times",
                   xaxis=x_axis_config, yaxis=y_axis_config)

#offline.plot needs dictionary with data and layout objects
#filename is specified name of file
offline.plot({"data": data, "layout": my_layout}, filename="d6.html")

