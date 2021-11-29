import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "//sixteen/data/eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)


all_eq_dicts = all_eq_data["features"]
title = all_eq_data["metadata"]["title"]

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:


    #title of each earthquake
    # every title is added to the list
    # matches corresponding location
    hover_texts.append(eq_dict["properties"]["title"])

    # call value corresponding to title key
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])



#alternate way of specifying needed data
#data still has scattergeo type, lon & lat values
#however, it now incorporates other values like color and text
#still a data set, thus the square brackets surrounding the dictionary
data = [{
    #specifies scattergeo class
    "type": "scattergeo",

    #lon & lat values
    "lon": lons,
    "lat": lats,

    #specifies text
    #label for each marker
    "text": hover_texts,

    #specifies marker with its own dictionary
    "marker": {
        #list comprehension
        #a little bit bigger dots, can see disparity in size better
        "size": [5 * mag for mag in mags],

        #color is based on magnitude, colorscale tells specific colors
        "color": mags,

        #specific range of colors
        "colorscale": "Viridis",

        #tells which values are darker and which are lighter
        "reversescale": True,

        #appearance of colorbar on side of map, we give it a title
        "colorbar": {"title": "Magnitude"},
    },
}]
my_layout = Layout(title=title)

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes_updated.html")