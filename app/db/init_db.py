from app.db.database import engine, Base
from app.models.task import Task


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
