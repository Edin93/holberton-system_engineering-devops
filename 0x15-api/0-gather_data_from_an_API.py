#!/usr/bin/python3
"""
Module contains a function that returns informations about a requested employee
"""


import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    user_id = argv[1]
    response = requests.get("{}/{}".format(url, user_id), verify=False)
    if response.status_code == 200:
        tasks_done_list = []
        tasks_done = 0
        all_tasks = 0
        content = response.json()
        todos = requests.get("{}/{}/todos".format(url, user_id), verify=False)
        todos = todos.json()
        all_tasks = len(todos)
        for task in todos:
            if task.get("completed", None):
                tasks_done_list.append(task.get('title', ''))
        tasks_done = len(tasks_done_list)
        print("Employee {} is done with tasks({}/{}):".format(
            content.get('name', ""),
            tasks_done,
            all_tasks
        ))
        for task in tasks_done_list:
            print("\t {}".format(task))
