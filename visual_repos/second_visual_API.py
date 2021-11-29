import requests

from plotly.graph_objs import Bar
from plotly import offline

#make API call and store response
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#process results
response_dict = r.json()
repo_dicts = response_dict["items"]

#labels is corresponding info for each repo
repo_names, stars, labels = [], [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]

    #define what we want each label to say as info
    #<br /> means line break, basically new line
    #we say the owner of the project, and it's description
    label = f"{owner}<br />{description}"

    #add each lable to the empty list
    labels.append(label)

data = [{
    "type": "bar",
    "x": repo_names,
    "y": stars,

    #key hovertext means what happens when mouse cursor is over the bar
    #when that happens, the corresponding label appears
    "hovertext": labels,

#like type, marker is a dictionary feauture for the x & y vlaues
#defines the bars of the graph(idk why its not in layout)
    "marker": {

#marker has its own individual settings that can be defined
#color is color of bars and is specified RGB style
        "color": "rgb(60, 100, 150)",

#line is outline of bars, has its own features like width & color
        "line": {"width": 1.5, "color": "rgb(25,25,25)"},

#opacity is transparency of bars, it belongs in marker settings
        "opacity": 0.6
    },
}]

my_layout = {
    "title": "Most Starred Python Projects on Github",

    #titlefont is its own key, has key_value pair that defines size
    "titlefont": {"size": 28},

    #axes have their own features
    #what the title says, size of title, and size of ticks
    "xaxis": {"title": "Repository",
              "titlefont": {"size": 24},
              "tickfont": {"size": 14},
              },
    "yaxis": {"title": "Stars",
              "titlefont": {"size": 24},
              "tickfont": {"size": 14},
              },
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="second_visual.html")