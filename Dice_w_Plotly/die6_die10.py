from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#create 2 D6 die
#2 instances of die
die_1 = Die()

#instance of die but now change parameter num_sides to 10
die_2 = Die(10)


results = []
for roll_num in range(50_000):
    #result is now the sum of the 2 die rather than one
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyze results
frequencies = []

# retrieve frequency of occurance of each number from 2-16
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#x_values are now 2-16
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of result"}
my_layout = Layout(title="Results of rolling a D6 & D10 dice 50,000 times",
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data":data, "layout": my_layout}, filename="d6_d10.html")