import sqlite3
from flask import render_template, request
from app import app

@app.get('/tasks')
def get_all_tasks():
    return "tasks"

@app.post('/tasks')
def create_task():
    """
    POST /tasks JSON
    {
        "taskname":string
        "status": string
    }
    """
    request_body = request.get_json()
    taskname = request_body["taskname"]
    status = request_body["status"]
    #print(taskname)
    #print(status)
    db_connection= app.config["DATABASE_CON"]
    cursor = db_connection.cursor()
    cursor.execute(
        "INSERT INTO tasks (taskname, status) VALUES (?,?)",
        (taskname,status)
    )
    db_connection.commit()
    task_id = cursor.lastrowid
    db_connection.row_factory = sqlite3.Row 
    cur = db_connection.cursor()
    cur.execute(
        "SELECT * FROM tasks where task_id=?",(task_id,) #tuple that has only one element
    ) 
    data = cur.fetchone()
    dict_data=(dict(data))
    return{
        'task_id': dict_data['task_id'],
        'taskname':dict_data['taskname'],
        'status': dict_data['status']
        }
   

@app.route("/")
def homepage():
   return render_template("index.html")