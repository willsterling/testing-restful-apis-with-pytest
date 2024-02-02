from uuid import uuid4

import requests

from config import BASE_URI


def get_task(task_id):
    return requests.get(BASE_URI + f'/get-task/{task_id}')


#refactor the response for create task
def create_task(payload):
    return requests.put(BASE_URI + '/create-task', json=payload)


#refactor the response for update task
def update_task(payload):
    return requests.put(BASE_URI + '/update-task', json=payload)


def list_tasks(user_id):
    return requests.get(BASE_URI + f'/list-tasks/{user_id}')


def delete_task(task_id):
    return requests.delete(BASE_URI + f'/delete-task/{task_id}')


# helper function to create payload
def new_payload():
    # create unique identifier for user id
    # convert to string hex representation of the object returned from uuid4() function
    user_id = f"test_user_{uuid4().hex}"
    task_content = f"test_task_content_{uuid4().hex}"
    return {
        "content": task_content,
        "user_id": user_id,
        "is_done": False
    }
