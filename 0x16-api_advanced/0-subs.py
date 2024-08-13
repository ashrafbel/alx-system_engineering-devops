#!/usr/bin/python3
"Module"
import requests


def number_of_subscribers(subreddit):
    "queries the Reddit API to return the number of subscribers"
    u = f"https://www.reddit.com/r/{subreddit}/about"


    headers = {
            "User-Agent": "CustomClient/1.0"
    }
    res_ = requests.get(u, headers=headers, allow_redirects=False)
    if res_.status_code == 200:
        info_ = res_.json().get('data').get('subreddit')
        return info_
    else:
        return 0
