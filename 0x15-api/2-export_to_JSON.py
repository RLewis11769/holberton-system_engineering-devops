#!/usr/bin/python3
"""
Uses REST API to return jsonplaceholder employee productivity info
Writes gathered info to .csv file
"""

import json
import requests
import sys


def export_to_json(empID):
    # Returns given info about given employee ID

    name = ''
    userDict = {}

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(empID))
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(empID))

    userJSON = user.json()
    name = userJSON.get('username')

    todoJSON = todo.json()

    userDict[empID] = []

    for task in todoJSON:
        taskDict = {}
        taskDict["task"] = task.get('title')
        taskDict["username"] = name
        taskDict["completed"] = task.get('completed')

        userDict[empID].append(taskDict)

    # Write to empID.json file
    with open("{}.json".format(empID), 'w') as jsonFile:
        json.dump(userDict, jsonFile)

# Only imports when called, but also passes first argument
if __name__ == "__main__":
    export_to_json(sys.argv[1])
