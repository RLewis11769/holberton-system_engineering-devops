#!/usr/bin/python3
"""
Uses REST API to return jsonplaceholder employee productivity info
Writes gathered info to .csv file
"""

import json
import requests


def export_all_to_json():
    # Returns given info about given employee ID

    allDict = {}
    userDict = {}

    users = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    userJSON = users.json()
    todoJSON = todos.json()

    for user in userJSON:
        userDict[user['id']] = user['username']
    
    for task in todoJSON:
        if allDict.get(task['userId'], False) is False:
            allDict[task['userId']] = []

        taskDict = {}
        taskDict["task"] = task['title']
        taskDict["username"] = userDict[task['userId']]
        taskDict["completed"] = task['completed']
        # When each taskDict is built properly, add to final dict
        allDict[task['userId']].append(taskDict)

    # Write to empID.json file
    with open('todo_all_employees.json', 'w') as jsonFile:
        json.dump(allDict, jsonFile)

# Only imports when called, but also passes first argument
if __name__ == "__main__":
    export_all_to_json()
