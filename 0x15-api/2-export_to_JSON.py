#!/usr/bin/python3
"""this script to fetch TODO list progress
for a given employee ID using REST API.
"""
import json
import requests
import sys


URL_USERS_API = "https://jsonplaceholder.typicode.com/users/"
URL_TODOS_API = "https://jsonplaceholder.typicode.com/todos?userId="

if len(sys.argv) == 2:
    try:
        id_emp = int(sys.argv[1])
        url_users = f"{URL_USERS_API}{id_emp}"
        url_todos = f"{URL_TODOS_API}{id_emp}"

        resp_user = requests.get(url_users)
        resp_user.raise_for_status()
        data_user = resp_user.json()
        name_of_user = data_user.get('username')
        resp_totos = requests.get(url_todos)
        resp_user.raise_for_status()
        data_totos = resp_totos.json()

        ts = []
        for task in data_totos:
            task_info = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": name_of_user
                }
            ts.append(task_info)
        d = {str(id_emp): ts}
        fln = f"{id_emp}.json"
        with open(fln, mode='w') as fl:
            json.dump(d, fl, indent=4)
        print(f"Data exported to {fln}")

    except ValueError:
        print("EMPLOYEE_ID must be an integer")
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
