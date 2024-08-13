#!/usr/bin/python3
"Module"
import requests
def number_ofsubscribers(subreddit):
    "queries the Reddit API to return the number of subscribers"
    u = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
            "User-Agent": "Custom"
    }
    res = requests.get(u, headers=headers, allowredirects=False)
    if res.statuscode == 200:
        info = res.json().get('data').get('subreddit')
        if info:
            return info_
    else:
        return 0
