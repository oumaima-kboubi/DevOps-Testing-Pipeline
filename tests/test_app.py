import os
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


# Task creation Test
def test_create_task(test_client):
   #Given
    request_payload = {
        "taskname":"test",
        "status":"bien"
    }
    expected_body={
        "taskname":"test",
        "status":"bien"
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