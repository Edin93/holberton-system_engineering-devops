#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles of all hot
articles for a given subreddit. If no results are found for the given
subreddit, the function should return None.
"""


import json
import requests
import sys


headers = {
    'User-Agent': 'my custom user agent 1.0',
}


def get_url(subreddit, after):
    """
    Return URL of subreddit to request.
    """
    url = 'https://www.reddit.com/r/{}/.json?after={}'.format(subreddit, after)
    return url


def recurse(subreddit, hot_list=[], after=None):
    """
    Return a list containing the titles of all hot
    articles for a given subreddit.
    """
    data = requests.get(
        get_url(subreddit, after), headers=headers
    ).json().get('data', None)
    if (data is None):
        return None
    hot_list += data.get('children', [])
    if (data.get('after', None) is not None):
        recurse(subreddit, hot_list, data.get('after', None))
    return hot_list
