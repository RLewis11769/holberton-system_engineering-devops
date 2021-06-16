#!/usr/bin/python3
""" Uses REST API to return jsonplaceholder employee productivity info """

import requests
import sys


def get_employee_tasks(empID):
    # Returns given info about given employee ID

    name = ''
    task_list = []
    completed = 0

    # Recieves API response in form of complicated dict
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(empID))
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(empID))

    # Use json method to break api response into value at key "name"
    userJSON = user.json()
    name = userJSON.get('name')

    todoJSON = todo.json()
    for task in todoJSON:
        if task.get('completed') is True:
            completed += 1
            task_list.append(task.get('title'))

    print("Employee {} is done with tasks ({}/{}):".format(
        name, completed, len(todoJSON)))
    for task in task_list:
        print("\t {}".format(task))

# Only imports when called, but also passes first argument
# Called via "python3 0-gather_data_from_an_API.py (number)"
if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
