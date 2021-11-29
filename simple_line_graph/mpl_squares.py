#import module as plt
import matplotlib.pyplot as plt

#list for data to plot
#squares is y, input_values is x
input_values = [1,2,3,4,5,6,7]
squares = [1,4,9,16,25,36,49]

#pyplot has array of fonts and stuff for the plot to stylize
#function allows use of a certain style
plt.style.use("grayscale")

#subplots returns a tuple containing figure and axes objects
#fig = entire figure or collection of plots
#ax = single plot
fig, ax = plt.subplots()

#plot indicated list
#alter linewidth attribute, thicker line when plotted
# y axis is default plotted with index of list as x
#having an x value plots the relationship between x & y
#c stands for color, we can set a color for the line
#RGB can also be used
    #only for lines, values must be between 0 & 1
ax.plot(input_values, squares, linewidth = 3, c=(0,0,1))

#set chart title & label axes
#ax.set_ = functions that creates indicated thing (title, x, y)
#in parentheses is the name and size of font
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set size of tick labels
#ticks are numbers on sides of graphs, (left and bottom)
#"both" means do function for both x & y
ax.tick_params(axis="both", labelsize=14)

#displays plot, like a print function
plt.show()