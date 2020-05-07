#!/usr/bin/python3
"""
Module to query the Reddit API and returs the number of subscribers of a
given subreddit.
"""


import requests
import json


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a given subreddit.

    Parameters:
    subreddit (string): subreddit to search for.
    """
    subreddit_subscribers = 0
    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    headers = {
        'User-Agent': 'my custom user agent 1.0',
    }
    res = requests.get(url, headers=headers, verify=False)
    content = res.json()
    if res.status_code == 200:
        children = content.get('data', None).get('children', None)
        if children:
            subreddit_subscribers = children[0].get('data', None).get(
                'subreddit_subscribers', None)
    return subreddit_subscribers
