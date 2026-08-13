from sqlalchemy.orm import Session

from app.models.task import Task
from app.repositories import task_repository
from app.schemas.task import TaskCreate


def get_tasks(db: Session):
    return task_repository.get_all(db)


def get_task(db: Session, task_id: int):
    return task_repository.get_by_id(db, task_id)


def create_task(db: Session, task_data: TaskCreate):

    task = Task(
        title=task_data.title
    )

    return task_repository.create(db, task)
