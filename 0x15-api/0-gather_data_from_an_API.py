#!/usr/bin/python3
""" Uses restAPI and jsonplaceholder to return info about employee productivity """

import requests
import sys


def get_employee_tasks(empID):
    # Returns given info about given employee ID

    name = ''
    task_list = []
    completed = 0

    userResponse = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(empID))
    todoResponse = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(empID))

    userJSON = userResponse.json()
    name = userJSON.get('name')

    todoJSON = todoResponse.json()
    for task in todoJSON:
        if task.get('completed') is True:
            completed += 1
            task_list.append(task.get('title'))

    print("Employee {} is done with tasks ({}/{}):".format(name, completed, len(todoJSON)))
    for task in task_list:
        print("\t {}".format(task))


if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
