from fastapi import FastAPI, HTTPException, status,Query
from manager.task_manager import TaskManager
from models.task import Task
from typing import Annotated

app = FastAPI()
task_manager = TaskManager()



@app.get('/tasks')
def read_tasks(query: Annotated[str | None, Query(min_length=3 , max_length=50)]=None):
        tasks = task_manager.read_tasks(query)
        return {'success':True, 'data':tasks}

@app.get("/tasks/{task_id}")
def read_task(task_id: str):
    task = task_manager.read_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'success':False,'message':f"Task with ID {task_id} not found!"})
    return {"success": True, "data": task}
  

@app.post('/tasks', status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    new_task = task_manager.create_task(task)
    return {"success": True, "data": new_task}

@app.put('/tasks/{task_id}')
def update_task(task_id: str, task: Task):
    updated_task = task_manager.update_task(task_id,task)
    if not updated_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'success':False,'message':f"Task with ID {task_id} not found!"})
    return {"success": True, "data": updated_task}

@app.delete('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str):
    deleted_task = task_manager.delete_task(task_id)
    if not deleted_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'success':False,'message':f"Task with ID {task_id} not found!"})
    return {"succe ss": True, "data": deleted_task}

































# /tasks/{task_id}/mark-completed' 

@app.put('/tasks/mark-completed/{task_id}')
def markCompleted(task_id:str):
    mark_completed = task_manager.markCompleted(task_id)
    if  not mark_completed:
        return {'success': False, 'massage': f"task with id{task_id} not found!"}
    return {"success":True,"data":mark_completed}
    


































