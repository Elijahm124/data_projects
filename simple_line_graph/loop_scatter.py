import matplotlib.pyplot as plt

#array of number from 1 to 1000
x_values = range(1,1001)
#list comprehended list of numbers based on list of x_values
y_values = [x ** 2 for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()

#scatter plot list of looped data
#smaller size points cuz more points
#cmap = range of shades of a color, light to sark
#color is based on y value this time c= y_values
#line goes from light to dark blue as y increases
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)

#set chart title & label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize =14)

#create a range for axes at bottom & side (min & max x and y)
ax.axis([0,1100, 0, 1100000])

#save a plot to a file (as a png)
#bbox_inches = trims extra whitespace from plot
plt.savefig("blue_squares_plot.png", bbox_inches="tight")
