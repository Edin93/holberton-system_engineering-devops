#!/usr/bin/python3
"""
Module to query the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""


import json
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {
        'User-Agent': 'my custom user agent 1.0',
    }
    params = {'limit': 10}
    res = requests.get(url, headers=headers, params=params)
    try:
        content = res.json()
        children = content.get('data').get('children')
        if len(children) == 0:
            print(None)
        else:
            for item in children:
                print('{}'.format(item.get('data').get('title')))
    except Exception as e:
        print(None)
