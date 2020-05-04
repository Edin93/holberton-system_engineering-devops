#!/usr/bin/python3
"""
Module contains a function that writes informations about a requested employee
into a CSV file, named USER_ID.csv, where USER_ID is the id of the sought user
"""


import csv
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
        file_name = '{}.csv'.format(content.get('id', 0))
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow([
                    int(user_id),
                    content.get('username', ''),
                    task.get('completed', False),
                    task.get('title', '')
                ])


if __name__ == "__main__":
    get_user_info()
