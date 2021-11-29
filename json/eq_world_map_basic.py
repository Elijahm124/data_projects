#we're using json data
#see die histo for plotly help
import json

#plotly works well with json
#graph_objs is a set of figures module
#Scattergeo is a specific figure = scatterplot on a map
#Layout sets layour of scatterplot?
from plotly.graph_objs import Scattergeo, Layout

#offline module allows making of map?
from plotly import offline

filename = "data/readable_eq_data.json"
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

#call Scattergeo class which plots list of x & y values
#Scattergeo plots them as coordinates
data = [Scattergeo(lon=lons, lat=lats)]

#call and specify layout of class
my_layout = Layout(title="Global Earthquakes")

#create variable for data and layour objects
fig = {"data": data, "layout": my_layout}

#plot figure variable along to specific file
offline.plot(fig, filename="global_earthquakes.html")