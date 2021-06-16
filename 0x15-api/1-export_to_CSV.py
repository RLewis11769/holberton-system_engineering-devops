#!/usr/bin/python3
"""
Uses REST API to return jsonplaceholder employee productivity info
Writes gathered info to .csv file
"""

import csv
import requests
import sys


def export_to_csv(empID):
    # Returns given info about given employee ID

    name = ''
    task_list = []

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(empID))
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(empID))

    userJSON = user.json()
    name = userJSON.get('username')

    todoJSON = todo.json()
    for task in todoJSON:
        if task.get('completed') is True:
            # Each line should have format:
            #   empID, name, True/False if completed, task title
            taskRow = []
            taskRow.append(empID)
            taskRow.append(name)
            taskRow.append(task.get("completed"))
            taskRow.append(task.get("title"))
            # When each task line is built properly, add to row
            task_list.append(taskRow)

    # Write to empID.csv file
    with open("{}.csv".format(empID), 'w') as csvFile:
        # Quote all fields aka "2","Shadow"
        csvwriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        # Write row from task_list to file
        csvwriter.writerows(task_list)

# Only imports when called, but also passes first argument
if __name__ == "__main__":
    export_to_csv(sys.argv[1])
