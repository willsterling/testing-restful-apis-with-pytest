import requests

from api_calls.todopixegami_request_calls import get_task, create_task, update_task, list_tasks, delete_task, \
    new_payload
from config import BASE_URI


# TESTS
def test_get_resp():
    response = requests.get(BASE_URI)
    assert response.status_code == 200


def test_can_create_task():
    payload = new_payload()
    response_for_create_task = create_task(payload)
    assert response_for_create_task.status_code == 200
    data = response_for_create_task.json()
    # print(data)

    # isolate task id from json data and utilize it to make API call to get the task
    task_id = data["task"]["task_id"]
    response_for_get_task = get_task(task_id)
    assert response_for_get_task.status_code == 200
    get_task_data = response_for_get_task.json()

    #uncomment to print task data:
    # print(get_task_data)
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


def test_can_update_task():
    # create a task
    payload = new_payload()
    response_for_create_task = create_task(payload)
    task_id = response_for_create_task.json()["task"]["task_id"]

    # update a task
    updated_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my updated content",
        "is_done": True,
    }
    response_for_updated_task = update_task(updated_payload)
    assert response_for_updated_task.status_code == 200

    # get, and validate update to selected task
    response_for_get_task = get_task(task_id)
    get_task_data = response_for_get_task.json()
    assert get_task_data["content"] == updated_payload["content"]
    assert get_task_data["is_done"] == updated_payload["is_done"]


def test_can_list_tasks():
    # create N tasks
    #   each will have unique task ID but same randomly generated task content and user ID
    n = 3
    payload = new_payload()
    for _ in range(n):
        response_for_create_task = create_task(payload)
        assert response_for_create_task.status_code == 200

    # extract user ID from payload to list tasks
    user_id = payload["user_id"]
    # List tasks using user ID, and check that there are N tasks
    response_for_list_tasks = list_tasks(user_id)
    assert response_for_list_tasks.status_code == 200
    list_data = response_for_list_tasks.json()

    tasks = list_data["tasks"]
    assert len(tasks) == n
    # uncomment to print list of tasks created:
    # print(list_data)


def test_can_delete_task():
    # create task
    payload = new_payload()
    response_for_create_task = create_task(payload)
    task_id = response_for_create_task.json()["task"]["task_id"]

    # delete task based using task ID
    response_for_delete_task = delete_task(task_id)
    assert response_for_delete_task.status_code == 200

    # verify task is deleted; should return "not found" 404 error from get task call
    response_for_get_deleted_task = get_task(task_id)
    assert response_for_get_deleted_task.status_code == 404
