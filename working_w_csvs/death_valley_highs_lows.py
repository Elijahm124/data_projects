import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = "data/death_valley_2018_simple.working_w_csvs"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []

#one of the rows has empty strings for columns 4-6
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")

        #try to get the column values for every row
        try:
            high = int(row[4])
            low = int(row[5])

        #if there's a value error, print statement then move on
        except ValueError:
            print(f"missing data for {current_date}")

        #if no value error make values apart of list
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#plot just skips over missing data instead of cancelling loop & plot

    plt.style.use("seaborn")

    fig, ax = plt.subplots()

    ax.plot(dates, highs, c="red", alpha=.5)
    ax.plot(dates, lows, c="blue", alpha=.5)
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=.1)

    title="Daily high & low temps - 2018\nDeath Valley, CA"
    plt.title(title, fontsize=20)
    plt.xlabel("",fontsize=16)

    fig.autofmt_xdate()

    plt.ylabel("Temperature (F)", fontsize=16)

    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()
