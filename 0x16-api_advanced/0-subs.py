#!/usr/bin/python3
"Module"
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for the given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "CustomClient/1.0"
    }
    res_ = requests.get(url, headers=headers, allow_redirects=False)
    if res_.status_code == 200:
        info_ = res_.json().get('data').get('subscribers')
        return info_
    else:
        return 0
