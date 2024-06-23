from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI(
    title="RPG Content API",
    description="API for generating and managing RPG content",
    version="1.0.0",
)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the RPG Content API"}