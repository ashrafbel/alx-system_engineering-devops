#!/usr/bin/python3
"Module for Recursively queries Reddit API"
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recurse queries Reddit API for all hot article titles in a subreddit"""
    u = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Custom"
    }
    params = {"after": after} if after else {}

    res_ = requests.get(u, headers=headers, params=params,
                        allow_redirects=False)

    if res_ .status_code != 200:
        return None

    info_ = res_.json().get("data")
    if not info_:
        return None

    children = info_.get("children", [])
    for c in children:
        hot_list.append(c["data"]["title"])

    after = info_.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
