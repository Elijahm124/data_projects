from operator import itemgetter

import requests

#make an API call & store the response
#this url has the IDs of the top stories from the website
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

#process info about each submission
#convert retrieved file (response object) to python list, and set to variable
submission_ids = r.json()

#empty list which will eventually feature the dictionaries of each file
#In hn_article.py we worked with one secific file's dictionary
submission_dicts = []

#for every submission in the top 30
for submission_id in submission_ids[:30]:

    #seperate API call for each submission

#the submission ID is the one difference between all the websites' articles
#so we call each url with the same variable except a different id
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)

#check the status of retrieval for each file retrieved
    print(f"id: {submission_id}\tstatus: {r.status_code}")

    #convert each retrieved json file to python dictionary
    response_dict = r.json()

    #build a dictionary for each article
    #we don't need all the key_value pairs we retrieved
    #so we extract specifics and make a new dictionary for each OG
    try:
        submission_dict = {
            "title": response_dict["title"],
            "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
            "comments": response_dict["descendants"],
        }
    #if there's a KeyError just continue and append
    except KeyError:
        continue

    #add each new dictionary to the empty list
    else:
        submission_dicts.append(submission_dict)

#itemgetter specifies sorting factor for list
#we sort the list by number of comments
#reverse=True means we start with the most comments instead of the least
submission_dicts = sorted(submission_dicts, key=itemgetter("comments"),
                          reverse=True)

#for every new dictionary in the list, we post each element of the dictionary
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")