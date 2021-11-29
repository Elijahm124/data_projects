from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create 2 D6 die
# 2 instances of die
die_1 = Die()
die_2 = Die()

# make some results and store results in a list
results = []
for roll_num in range(1000):
    # result is now the sum of the 2 die rather than one
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze results
frequencies = []

# retrieve frequency of occurance of each number from 2-12
# count the frequency of a result of 2, then 3 etc.
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# x_values are now 2-12
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

# specify x values plotted with dtick (2,3,4,5,6 etc.)
# ensures each number is labeled and it doesnt skip
x_axis_config = {"title": "Result", "dtick": 1}

y_axis_config = {"title": "Frequency of result"}
my_layout = Layout(title="Results of rolling two D6 dice 1000 times",
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="d6_d6.html")
