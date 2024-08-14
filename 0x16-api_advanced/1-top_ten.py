#!/usr/bin/python3
"Module Queries Reddit API"

import requests

def top_ten(subreddit):
    "Queries Reddit API to print the first 10 hot post titles for a subreddit"
    u = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "Custom"
    }
    
    res_ = requests.get(u, headers=headers, allow_redirects=False)
    
    if res_.status_code == 200:
        Info_ = res_ .json().get('data')
        if Info_:
            posts = Info_.get('children', [])
            for p in posts:
                print(p['data']['title'])
        else:
            print(None)
    else:
        print(None)
