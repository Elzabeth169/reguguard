
from fastapi import FastAPI

app = FastAPI(
    title="ReguGuard API",
    description="AI-powered Quality Intelligence and Compliance Platform",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "ReguGuard",
         "version": "0.1.0"
    }
