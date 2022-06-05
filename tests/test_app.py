import os
import pytest 
from flask import Flask
from utils.create_db import create_db


@pytest.fixture(scope="session",autouse=True)
def create_test_database(tmp_path_factory):
   tmp_dir=  tmp_path_factory.mktemp("tmp")
   database_filename = tmp_dir / "test_database.db"
   create_db(database_filename)
   os.environ["DATABASE_FILENAME"] = str(database_filename)


@pytest.fixture(scope='module')#module is test_app.py / function 
def test_client():
    flask_app = Flask(__name__)
    testing_client = flask_app.test_client(use_cookies=False)
    context=flask_app.app_context()
    context.push()
    yield testing_client # followed by clean up
    context.pop()


def test_get_tasks(test_client):
    test_client.get('/tasks')
    print(os.environ("DATABASE_FILENAME"))
    assert False 