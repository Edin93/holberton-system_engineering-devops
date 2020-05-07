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
    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    headers = {
        'User-Agent': 'my custom user agent 1.0',
    }
    res = requests.get(url, headers=headers, verify=False)
    content = res.json()
    #print(content)
    #print('*****************************************')
    #for i in res.__dict__:
        #print('--------->>> {}'.format(i))
        #print(json.dumps(getattr(res, i, None), indent=4, sort_keys=True))
        #print('res[{}] = {}'.format(i, getattr(res, i, None)))
        #print('-----------------------------------------------')
    #print(json.dumps(res._content, indent=4, sort_keys=True))
    if res.status_code == 200:
        #print(json.dumps(content.get('data', None), indent=4, sort_keys=True))
        #print(content)
        print(
            content.get('data', None)
            .get('children', None)[0]
            .get('data', None)
            .get('subreddit_subscribers', None)
        )
        print('--------------------------')
    return 0
