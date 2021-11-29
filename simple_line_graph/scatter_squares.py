import matplotlib.pyplot as plt

#series of values for scatter plot
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.style.use("seaborn")
fig, ax = plt.subplots()

#plots scatter plot of lists of x & y
#plots (1,1),(2,4),(3,9) etc.
ax.scatter(x_values, y_values,s=100)

#set chart title & label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize =14)


ax.tick_params(axis="both", which="major", labelsize = 14)


plt.show()