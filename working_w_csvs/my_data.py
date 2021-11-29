import csv

import matplotlib.pyplot as plt

from datetime import datetime

#basically a copy of sitka highs lows, except i downloaded my own data

filename = "data/COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.working_w_csvs"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_number in enumerate(header_row):
        print(index, column_number)

    dates, cases, hops = [], [], []

    for row in reader:
#idk how i did this but i matched the string to it's date format
#idk how it removed the times in the actual graph but whatev haha
        date = datetime.strptime(row[0], "%m/%d/%Y %H:%M:%S %p")
        case = int(row[1])
        hop = int(row[2])

        dates.append(date)
        cases.append(case)
        hops.append(hop)

    plt.style.use("seaborn")

    fig, ax = plt.subplots()

    ax.plot(dates, cases, alpha=.5, color="red")
    ax.plot(dates, hops, alpha=.5, color="yellow")
    plt.fill_between(dates, cases, hops, alpha =.1, facecolor ="orange")

    plt.title("Covid Cases & Hospitalizations in NYC", fontsize = 24)

    plt.xlabel("", fontsize=16)

    fig.autofmt_xdate()

    plt.ylabel("People", fontsize=16)

    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()




