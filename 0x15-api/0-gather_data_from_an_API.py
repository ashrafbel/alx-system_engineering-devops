#!/usr/bin/python3
"""this script to fetch TODO list progress
for a given employee ID using REST API.
"""

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
        data_user = resp_user.json()
        name_of_user = data_user.get('name')
        resp_todos = requests.get(url_todos)
        data_todos = resp_todos.json()
        tasks = len(data_todos)
        done = [t for t in data_todos if t.get('completed')]
        num_of_tasks_done = len(done)
        
        # تأكد من تنسيق الرسالة بشكل صحيح
        print("Employee {} is done with tasks({}/{}):".format(
            name_of_user, num_of_tasks_done, tasks))
        
        for t in done:
            print("\t{}".format(t.get('title')))
            
    except ValueError:
        print("EMPLOYEE_ID must be an integer")
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
else:
    print("Usage: python script.py EMPLOYEE_ID")
