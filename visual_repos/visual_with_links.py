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

#we now want a list of repo_links instead of just the name
#empty list that will be appended with the links
repo_links, stars, labels = [], [], []

for repo_dict in repo_dicts:

#still define the repo name cuz we still want it seen
    repo_name = repo_dict["name"]

#define repo_url by calling value for html_url key for each repo
    repo_url = repo_dict["html_url"]

#<a href='URL'>link text</a> places link in place of name
#name of repo is shown but also given ability to click on it for the link
    repo_link = f"<a href= '{repo_url}'>{repo_name}</a>"

#appned every repo_link to its corresponding place in the list of repos
    repo_links.append(repo_link)


    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    label = f"{owner}<br />{description}"
    labels.append(label)

data = [{
    "type": "bar",
#now repo_links is new list of x values
    "x": repo_links,

    "y": stars,
    "hovertext": labels,
    "marker": {
        "color": "rgb(60, 100, 150)",
        "line": {"width": 1.5, "color": "rgb(25,25,25)"}
    },
    "opacity": 0.6,
}]

my_layout = {
    "title": "Most Starred Python Projects on Github",
    "titlefont": {"size": 28},
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
offline.plot(fig, filename="visual_links.html")