import json

#explore structure of data
#import and name json file
filename = "data/eq_data_1_day_m1.json"
with open(filename) as f:

#json.load converts file into (kinda) readable python dictionary
    all_eq_data = json.load(f)

#create a new file with ability to write to it
readable_file = "data/readable_eq_data.json"
with open(readable_file, "w") as f:

    #json.dump writes json data(dictionary) to file
    #im guessing theres 4 sublevels of data so we
        #dump the data indented 4 times
    json.dump(all_eq_data, f, indent=4)


#features is key-value with list of each earthquake
#each feature is one earthquake and its features
#each erthquake is one dictionary in the list

#call value associated with key features
#value = list of all earthquake data dictionaries
all_eq_dicts = all_eq_data["features"]

#158 values in list
print(len(all_eq_dicts))

#empty lists to store magnitude, latitude, longitude values
#for each earthquake
mags, lons, lats = [], [], []

#for each dictionary in the list of dictionary
#obtain its magnitude, latitude, longitude values
for eq_dict in all_eq_dicts:

#nested dictionary
    #call value associated with "mag" key
    #mag key is in itself, a value of "properties" key
    mag = eq_dict["properties"]["mag"]

    #call specific (0th) value associated with "coordinates" key
    #coordinates key is value of geometry key
    lon = eq_dict["geometry"]["coordinates"][0]

    #call specific (1st) value associated with "coordinates" key
    #coordinates key is value of geometry key
    lat = eq_dict["geometry"]["coordinates"][1]

#for each value defined, place in list,
# values correspond cuz obtained from same dictionary in list
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])