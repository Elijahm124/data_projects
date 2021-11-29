import requests

# import bar cuz we're doing a bar graph
from plotly.graph_objs import Bar

# import offline cuz we're plotting offline
from plotly import offline

# make API call and store response
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# process results
response_dict = r.json()
repo_dicts = response_dict["items"]

# empty list for x & y values
repo_names, stars = [], []

# for every dictionary in the list
for repo_dict in repo_dicts:
    # add the name & the corresponding amount of stars to the list
    # i guess repo_dicts is already sorted by amount of stars
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

# data aspect of the figure
# bar graph and specify x & y
# remember to put in brackets, cuz it's a list of x & y values
data = [{
    "type": "bar",
    "x": repo_names,
    "y": stars,
}]

# layout aspect of figure
# dont have to import layout class
# cuz we're using a dictionary to create layout

# set title of entire figure
my_layout = {
    "title": "Most Starred Python Projects on Github",

    # x & y axes have their own factors
    # sub-dictionary ft. title for each axis
    "xaxis": {"title": "Repository"},
    "yaxis": {"title": "Stars"},
}

# place data & layout equal to variable, fig(ure)
fig = {"data": data, "layout": my_layout}

# plot figure
offline.plot(fig, filename="first_visual.html")
