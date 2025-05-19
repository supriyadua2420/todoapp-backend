from sqlalchemy.orm import Session
import models, schemas

def get_tasks(db: Session):
    return db.query(models.Task).all()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def mark_complete(db: Session, task_id: int):
    task = db.query(models.Task).get(task_id)
    if task:
        task.completed = True
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).get(task_id)
    if task:
        db.delete(task)
        db.commit()
    return task
