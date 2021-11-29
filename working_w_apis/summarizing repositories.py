import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

# variable for list of repos
repository_dicts = response_dict["items"]

# loop thru every repo in the list
# obtain specific info for every repo in the list of repos (30)
for repository_dict in repository_dicts:
    print("\nSelected info about each repository")

    print(f"Name: {repository_dict['name']}")
    print(f"Owner: {repository_dict['owner']['login']}")
    print(f"Stars: {repository_dict['stargazers_count']}")
    print(f"Repository: {repository_dict['html_url']}")
    print(f"Description: {repository_dict['description']}")
