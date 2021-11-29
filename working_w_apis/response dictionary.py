import requests

#make an API call & store the response
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#store API response in a variable as dictionary
response_dict = r.json()

#retrieve value associated with "total" key in dictionary
#get total amount of repositories on github
print(f"Total repositories: {response_dict['total_count']}")

#explore information abt repositories
#repository dicts != response dict
#repository_dicts/items is a list of
    # dictionaries for each repository (project)
repository_dicts = response_dict["items"]

#30 dictionaries in the list = 30 repositories
print(f"Repositories returned: {len(repository_dicts)}")

#examine first repository

#first element of repository dictionaries
repo_dict_one = repository_dicts[0]

#there are 74 key-value pairs in the first repository dictionary
#74 pieces of info for each repositroy dictionary
print(f"\nKeys: {len(repo_dict_one)}")

#print out each key in alphabetical order
#allow us to see specifc info we have for each repo
for key in sorted(repo_dict_one.keys()):
    print(key)

#certain values for first repo
#call specific keys for values in first repo dictionary
print("\nSelected info about first repository")

#name is the name of the project/repo
print(f"Name: {repo_dict_one['name']}")

#there is a dictionary containing owner info nested in first repo
#so we call value for key "login", which is a value for key "owner"
#login is their username for github
print(f"Owner: {repo_dict_one['owner']['login']}")

# amount of times the repo has been starred/liked
print(f"Stars: {repo_dict_one['stargazers_count']}")

#url/website name
print(f"Repository: {repo_dict_one['html_url']}")

#time created & most recent time updated
print(f"Created: {repo_dict_one['created_at']}")
print(f"Updated: {repo_dict_one['updated_at']}")

#what the creator of the repo put as a description
print(f"Description: {repo_dict_one['description']}")