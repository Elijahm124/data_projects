#comma separated values
import csv

#import working_w_csvs file and assign to variable
filename = 'data/sitka_weather_07-2018_simple.working_w_csvs'

#open file as variable
with open(filename) as f:

    #reader() object makes rows of CSVs turn into iterables
    #basically every row it's own number, row 1, row 2, etc.
    reader = csv.reader(f)


    #next() object makes next single iterable turn into a list
    #this is because it specifies one row
    #it also allows us to skip this row when iterating thru rest of rows
    #in this case we printed a list of the first row
    header_row = next(reader)
    print(header_row)

    #enumerate function returns value and corresponding index
    #tells us which index to call and use
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #get high temperatures from this file
    #empty list
    highs = []

    #the row in reader has its own list, so 5 is the fifth placement
    #so for every row, call the 5th element, which is the high
    #place every high in the empty list for a list of highs
    #doesnt include first row because of next function
    for row in reader:
        high = int(row[5])
        highs.append(high)

print(highs)