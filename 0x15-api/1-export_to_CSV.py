#!/usr/bin/python3
"""
Module contains a function that writes informations about a requested employee
into a CSV file, named USER_ID.csv, where USER_ID is the id of the sought user
"""


import requests
from sys import argv
import csv


def get_user_info():
    url = "https://jsonplaceholder.typicode.com/users"
    user_id = argv[1]
    csv_file = user_id + ".csv"
    response = requests.get("{}/{}".format(url, user_id), verify=False)
    if response.status_code == 200:
        content = response.json()
        todos = requests.get("{}/{}/todos".format(url, user_id), verify=False)
        todos = todos.json()
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow([
                    user_id,
                    content.get('username', ''),
                    task.get('completed', False),
                    task.get('title', '')
                ])


if __name__ == "__main__":
    get_user_info()
