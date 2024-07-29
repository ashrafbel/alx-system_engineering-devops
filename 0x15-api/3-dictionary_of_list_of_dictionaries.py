#!/usr/bin/python3
"""This script fetches TODO list progress for all employees using REST API
and exports the data in JSON format.
"""
import json
import requests

URL_USERS_API = "https://jsonplaceholder.typicode.com/users"
URL_TODOS_API = "https://jsonplaceholder.typicode.com/todos"

try:
    # جلب بيانات جميع المستخدمين
    resp_users = requests.get(URL_USERS_API)
    resp_users.raise_for_status()
    users_data = resp_users.json()

    # جلب بيانات جميع المهام
    resp_todos = requests.get(URL_TODOS_API)
    resp_todos.raise_for_status()
    todos_data = resp_todos.json()

    all_data = {}

    # معالجة البيانات
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

    # إنشاء ملف JSON
    file_name = 'todo_all_employees.json'
    with open(file_name, mode='w') as file:
        json.dump(all_data, file, indent=4)

    print(f"Data exported to {file_name}")

except requests.exceptions.RequestException as e:
    print(f"HTTP Request failed: {e}")
