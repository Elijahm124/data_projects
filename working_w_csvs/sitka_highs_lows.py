import csv

from datetime import datetime

import matplotlib.pyplot as plt

filename = "data/sitka_weather_2018_simple.working_w_csvs"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#multiple assignment, empty lists that will be appended
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")

        #lows in row are element #5
        high = int(row[5])

        #highs in row are element #6
        low = int(row[6])

        #append each row's called value to the empty list
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    plt.style.use("seaborn")

    fig, ax = plt.subplots()

    #call two separate plots (lines)
    #different colors for different plots
    #alpha value is how transparent (lightly colored) the lines are
    ax.plot(dates, highs, c="red", alpha=.5)
    ax.plot(dates, lows, c="blue", alpha=.5)

    #fill between function
    #takes x values and 2 y values to color between on graph
    #facecolor is color shaded between two lines
    #very light purple
    plt.fill_between(dates, highs, lows, facecolor="purple", alpha=.1)

    plt.title("Daily high & low temps - 2018", fontsize=24)
    plt.xlabel("",fontsize=16)

    fig.autofmt_xdate()

    plt.ylabel("Temperature (F)", fontsize=16)

    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()



