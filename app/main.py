from fastapi import FastAPI

app = FastAPI(
    title="Task API",
    description="A simple Task Management API",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "task-api"
    }
