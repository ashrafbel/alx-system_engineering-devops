#!/usr/bin/python3
"""this script to fetch TODO list progress
for a given employee ID using REST API.
"""
import json
import requests
import sys


URL_USERS_API = "https://jsonplaceholder.typicode.com/users"
URL_TODOS_API = "https://jsonplaceholder.typicode.com/todos"

try:
    resp_users = requests.get(URL_USERS_API)
    resp_users.raise_for_status()
    users_data = resp_users.json()


    resp_todos = requests.get(URL_TODOS_API)
    resp_todos.raise_for_status()
    todos_data = resp_todos.json()

    all_data = {}
    for user in users_data:
        user_id = user['id']
        username = user['username']
        user_tasks = []

        for task in todos_data:
            if task['userId'] == user_id:
                task_info = {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                user_tasks.append(task_info)

        all_data[str(user_id)] = user_tasks


    fl_name = 'todo_all_employees.json'
    with open(fl_name, mode='w') as fl:
        json.dump(all_data, fl)

    print(f"Data exported to {fl_name}")

except requests.exceptions.RequestException as e:
    print(f"HTTP Request failed: {e}")
