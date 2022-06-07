import os
from urllib import response
import pytest 
from flask import Flask
from app import app
from utils.create_db import create_db


@pytest.fixture(scope="session",autouse=True)
def create_test_database(tmp_path_factory):
   tmp_dir=  tmp_path_factory.mktemp("tmp")  # will be cleaned up automatically by the os
   database_filename = tmp_dir / "test_database.db"
   create_db(database_filename)
   os.environ["DATABASE_FILENAME"] = str(database_filename)

@pytest.fixture(scope='module')#module is test_app.py / function 
def test_client():
    flask_app = app
    testing_client = flask_app.test_client(use_cookies=False)
    context=flask_app.app_context()
    context.push()
    yield testing_client # followed by clean up, for each function we have a new context
    context.pop()

# First task creation Test
def test_create_task1(test_client):
   #Given
    request_payload = {
        "taskname":"Do DevOps project",
        "status":"Todo"
    }
    expected_body={
        "taskname":"Do DevOps project",
        "status":"Todo"
    }
    expected_body_keys = ["task_id","taskname","status"]
    expected_status_code = 200

   #When
    response = test_client.post('/tasks', json=request_payload)

   #Then
    assert expected_status_code == response.status_code
    assert (response.json | expected_body ) == response.json
    assert int == type(response.json["task_id"])
    assert set (expected_body_keys) == response.json.keys()

# Second task creation Test
def test_create_task2(test_client):
   #Given
    request_payload = {
        "taskname":"Complete Software Testing project",
        "status":"In Progress"
    }
    expected_body={
        "taskname":"Complete Software Testing project",
        "status":"In Progress"
    }
    expected_body_keys = ["task_id","taskname","status"]
    expected_status_code = 200

   #When
    response = test_client.post('/tasks', json=request_payload)

   #Then
    assert expected_status_code == response.status_code
    assert (response.json | expected_body ) == response.json
    assert int == type(response.json["task_id"])
    assert set (expected_body_keys) == response.json.keys()

#Third task creation Test
def test_create_task3(test_client):
   #Given
    request_payload = {
        "taskname":"Integration Testing",
        "status":"Complete"
    }
    expected_body={
        "taskname":"Integration Testing",
        "status":"Complete"
    }
    expected_body_keys = ["task_id","taskname","status"]
    expected_status_code = 200

   #When
    response = test_client.post('/tasks', json=request_payload)

   #Then
    assert expected_status_code == response.status_code
    assert (response.json | expected_body ) == response.json
    assert int == type(response.json["task_id"])
    assert set (expected_body_keys) == response.json.keys()

# get all tasks Test
def test_get_all_tasks(test_client):
    #Given
    expected_response = [
        {
            "task_id":1,
            "taskname":"Do DevOps project",
            "status":"Todo"
        }
        ,{
           "task_id":2,
            "taskname":"Complete Software Testing project",
            "status":"In Progress"
        },
        {
            "task_id":3,
        "taskname":"Integration Testing",
        "status":"Complete"
        }
    ]
    expected_status_code = 200
    #When
    response = test_client.get('/tasks')

    #Then
    assert expected_status_code == response.status_code
    assert expected_response  == response.json

def test_delete_existing_task(test_client):
    #Given
    task_id_to_delete = 1
    exepcted_body = {
         "message": "Task deleted successfully"
    }

    #When 
    response = test_client.delete(f'/tasks/{task_id_to_delete}')

    #Then
    assert exepcted_body == response.json

def test_delete_already_deleted_task(test_client):
    #Given
    task_id_to_delete = 1
    expected_body = {
        "message": "Task not deleted successfully"
    }

    #When
    response = test_client.delete(f'/tasks/{task_id_to_delete}')

    #Then
    assert expected_body == response.json


def test_delete_non_existing_task(test_client):
    #Given
    task_id_to_delete = 1478
    expected_body = {
        "message": "Task not deleted successfully"
    }

    #When
    response = test_client.delete(f'/tasks/{task_id_to_delete}')

    #Then
    assert expected_body == response.json

def test_get_tasks_after_delete(test_client):
    #Given
    expected_response = [
       {
           "task_id":2,
            "taskname":"Complete Software Testing project",
            "status":"In Progress"
        },
        {
            "task_id":3,
        "taskname":"Integration Testing",
        "status":"Complete"
        }
    ]
    expected_status_code = 200
    #When
    response = test_client.get('/tasks')

    #Then
    assert expected_status_code == response.status_code
    assert expected_response == response.json

