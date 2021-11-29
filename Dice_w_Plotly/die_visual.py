from die import Die

#create a D6 (die with 6 sides)
#instance of die class
die = Die()

#make some rolls and store results in list
#empty list
results = []

#roll die 100 times
for roll_num in range(100):
    #result is a number based off the function
    result = die.roll()

    #store number in list
    results.append(result)

#analyze results
print(results)

#empty list to store values
frequencies = []

#for numbers 1-6, count their occurence in the list
#after that, store frequency for each value in list
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
