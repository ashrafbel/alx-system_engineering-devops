#!/usr/bin/python3
"""this script to fetch TODO list progress
for a given employee ID using REST API.
"""
import csv
import sys
import requests


URL_USERS_API = "https://jsonplaceholder.typicode.com/users/"
URL_TODOS_API = "https://jsonplaceholder.typicode.com/todos?userId="

if len(sys.argv) == 2:
    try:
        id_emp = int(sys.argv[1])
        url_users = f"{URL_USERS_API}{id_emp}"
        url_todos = f"{URL_TODOS_API}{id_emp}"

        resp_user = requests.get(url_users)
        data_user = resp_user.json()
        name_of_user = data_user.get('username')
        resp_totos = requests.get(url_todos)
        data_totos = resp_totos.json()
        fl_name = f"{id_emp}.csv"
        with open(fl_name, mode='w', newline='') as fl:
            wt = csv.writer(fl, quoting=csv.QUOTE_ALL)
            for t in data_totos:
                w = [id_emp, name_of_user, t.get('completed'), t.get('title')]
                wt.writerow(w)
        print(f"Data exported to {fl_name}")
    except ValueError:
        print("EMPLOYEE_ID must be an integer")
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
