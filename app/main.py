from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="RPG Content API",
    description="API for generating and managing RPG content",
    version="1.0.0",
    debug=settings.DEBUG
)

@app.get("/")
async def root():
    return {"message": "Welcome to the RPG Content API"}

@app.get("/info")
async def info():
    return {
        "ollama_model": settings.OLLAMA_MODEL,
        "debug_mode": settings.DEBUG
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)