import json
import sqlite3
from flask import jsonify, render_template, request
from app import app

@app.get('/tasks/home')
def tasks_home():
    db_connection= app.config["DATABASE_CON"]
    db_connection.row_factory = sqlite3.Row 
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT * FROM tasks"
    )
    data = cursor.fetchall()
    msg = countTaskMessage(len(data))
    return  render_template("index.html", tasks=data, message=msg)

@app.get('/tasks/one')
def get_first_task(task_id):
    db_connection= app.config["DATABASE_CON"]
    db_connection.row_factory = sqlite3.Row 
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT * FROM tasks where task_id=?",(task_id,) #tuple that has only one element
    ) 
    data = cursor.fetchone()
    dict_data=(dict(data))
    return{
        'task_id': dict_data['task_id'],
        'taskname':dict_data['taskname'],
        'status': dict_data['status']
        }

@app.get('/tasks')
def get_all_tasks():
    db_connection= app.config["DATABASE_CON"]
    db_connection.row_factory = sqlite3.Row 
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT * FROM tasks"
    )
    data = cursor.fetchall()
    print([dict(element) for element in data]) # list comprehention
    return jsonify([
        {
            "task_id":element['task_id'],
            "taskname": element['taskname'],
            "status": element['status']
        }
        for element in data
    ])
   

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
   
@app.delete('/tasks/<string:task_id>')
def delete_task(task_id):
    db_connection= app.config["DATABASE_CON"]
    cursor = db_connection.cursor()
    cursor.execute(
        "DELETE FROM tasks where task_id = ?",
        (task_id,)
    )
    if cursor.rowcount == 0:
        return {
            "message": "Task not deleted successfully"
        }
    elif cursor.rowcount == 1:
        return{
            "message": "Task deleted successfully"
        }
    return app 

# @app.put("/tasks/<string:task_id>")
# def update_task(task_id):
#     db_connection= app.config["DATABASE_CON"]
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "UPDATE tasks SET where task_id = ?",
#         (task_id,)
#     )

def countTaskMessage(lenTask):
    if lenTask < 3 :
        return{"message":"Let's get more active! Keep the hight spirit"}
    elif 3<lenTask and lenTask <5:
          return{"message":"You seem to be active today! Well done"}
    elif lenTask > 5:
        return{"message":"Excellent job! You deserve a good treat"}
    elif lenTask < 0:
        return{"message":"Error"}

        
@app.route("/")
def homepage():
   return render_template("index.html")