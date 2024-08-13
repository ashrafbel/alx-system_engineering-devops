#!/usr/bin/python3
"""Module to query Reddit API for subscriber count"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    
    :param subreddit: str, the name of the subreddit
    :return: int, the number of subscribers (0 if subreddit is invalid)
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:my_reddit_client:v1.0 (by /u/your_username)"
    }
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
