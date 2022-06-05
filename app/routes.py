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
    cur = db_connection.cursor()
    cur.execute(
        "SELECT * FROM tasks wherer task_id=?",(task_id,) #tuple that has only one element
    ) 
    return {"message":"Inserted successfully"}

@app.route("/")
def homepage():
   return render_template("index.html")