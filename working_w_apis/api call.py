import requests

# make an API call & store the response
# this website has info abt github projects
# store url in url variable
# api.github.com = responds to API calls
# search/repositories = search repositiories
# ? = pass an argument
# q=specify a query, language: python
# &sort=stars, sorts projects by number of stars
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

# define a header for the API call
# tells program to specifically use version 3 of API
# accept = we allow use of version 3 of github
headers = {"Accept": "application/vnd.github.v3+json"}

# make the call to the API
# bascially means use this URL and use version 3 of github when doing so
# becomes a response object based on request
r = requests.get(url, headers=headers)

# r.status_code tells us if request for API was successfull (200)
print(f"Status code: {r.status_code}")

# store API response in a variable
# r.json() converts url data to python dictionary
# becomes a response dictionary
response_dict = r.json()

# process results
# these are the main keys of the dictionary/url data
print(response_dict.keys())
