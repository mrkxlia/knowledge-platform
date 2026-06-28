from fastapi import FastAPI

app = FastAPI(
    title="AI Knowledge Platform",
    description="Personal Knowledge Platform for Human and AI",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Knowledge Platform"
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}