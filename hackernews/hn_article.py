import requests
import json

#make an API call, & store the response

#define URL to be called with requests.get function
#this url returns the API for a single article
url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
r = requests.get(url)

#check to make sure it was called correctly
print(f"Status code: {r.status_code}")

#explore structure of data
#convert r file(response object) to python dictionary
response_dict = r.json()

#create & open new file and place OG file there
readable_file = "hackernews/readable_hn_data.json"
with open(readable_file, "w") as f:

    #ensure proper nesting with indent of 4
    json.dump(response_dict, f, indent=4)

#basically the purpose of this file was to view and retrieve data
#from the API of a specific ID'd article

#in the next file, we loop thru each of the top 30 files from
#the same website and extract specific data from them