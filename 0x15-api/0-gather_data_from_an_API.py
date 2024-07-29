import requests
import sys
"""this script to fetch TODO list progress
for a given employee ID using REST API.
"""


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
        resp_totos = requests.get(url_todos)
        data_totos = resp_totos.json()
        tasks = len(data_totos)
        done = [t for t in data_totos if t.get('completed')]
        num_of_tasks_done = len(done)
        print("Employee {} is done with tasks({}/{}):".format(
            name_of_user, num_of_tasks_done, tasks))
        for t in done:
            print(f"\t {t.get('title')}")
    except ValueError:
        print("EMPLOYEE_ID must be an integer")
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
