import matplotlib.pyplot as plt

plt.style.use("seaborn")
fig, ax = plt.subplots()

#plotting a single point
#takes x,y value for point
#take s value for size
#c stands for color, we can set a color for the line
#RGB can also be used
    #only for lines, values must be between 0 & 1
ax.scatter(2,4,s=200, c="purple")

#set chart title & label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize =14)

#which indicates either major (more important/defined) ticks are determined
#axis indicates which axis or both that will get altered ticks
ax.tick_params(axis="both", which="major", labelsize = 14)


plt.show()