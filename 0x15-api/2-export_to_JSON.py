#!/usr/bin/python3
"""
Module contains a function that writes informations about a requested employee
into a JSON file, named USER_ID.json. USER_ID is the id of the sought user
"""


import json
import requests
import sys


def get_user_info():
    url = "https://jsonplaceholder.typicode.com/users"
    user_id = sys.argv[1]
    response = requests.get("{}/{}".format(url, user_id), verify=False)
    if response.status_code == 200:
        content = response.json()
        todos = requests.get("{}/{}/todos".format(url, user_id), verify=False)
        todos = todos.json()
        file_name = '{}.json'.format(content.get('id', 0))
        data = {}
        data[str(user_id)] = [
            {
                "task": task.get('title', ''),
                "completed": task.get('completed', False),
                "username": content.get('username', '')
            } for task in todos
        ]
        with open(file_name, 'w', newline='') as file:
            json.dump(data, file)


if __name__ == "__main__":
    get_user_info()
