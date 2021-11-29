import csv

#allow proper use of dates in working_w_csvs file
from datetime import datetime

#allows plotting of data
import matplotlib.pyplot as plt

filename = "data/sitka_weather_07-2018_simple.working_w_csvs"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#multiple assignment, empty list to store dates & highs (x-axis, y-axis)
    dates, highs = [], []
    for row in reader:

        #striptime converts string to datetime object
        #first argument row[2] is third column which is dates
        #second argument is format of datetime object, year-month-date
        current_date = datetime.strptime(row[2], "%Y-%m-%d")

        high = int(row[5])

        #place each date & high in the list,
        # date corresponds to the temperature cuz they're in same row (loop)
        dates.append(current_date)
        highs.append(high)

#specific font
    plt.style.use("seaborn")

#return and use figure and axes objects
    fig, ax = plt.subplots()

#plot highs along axis, dates is x value, highs is y value
    ax.plot(dates, highs, c="red")

    #format plot
    plt.title("Daily high temperatures, July 2018", fontsize=24)
    plt.xlabel("",fontsize=16)

    #draw dates diagonally, basically automatically fits the x ticks
    fig.autofmt_xdate()

    plt.ylabel("Temperature (F)", fontsize=16)

    #set size of ticks(numbers on axis)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()