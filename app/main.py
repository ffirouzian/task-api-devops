from fastapi import FastAPI
from app.api.tasks import router as task_router

app = FastAPI(
    title="Task API",
    version="1.0.0"
)

app.include_router(task_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "task-api"
    }