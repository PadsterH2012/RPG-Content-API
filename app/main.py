from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.routes import character, quest, trait, character_behavior, pdf_upload
from app.database import create_tables

app = FastAPI(
    title="RPG Content API",
    description="API for generating and managing RPG content",
    version="1.0.0",
)

# Create tables at startup
create_tables()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

app.include_router(character.router, prefix="/characters", tags=["characters"])
app.include_router(quest.router, prefix="/quests", tags=["quests"])
app.include_router(trait.router, prefix="/traits", tags=["traits"])
app.include_router(character_behavior.router, prefix="/character_behaviors", tags=["character_behaviors"])
app.include_router(pdf_upload.router, prefix="/pdf", tags=["pdf"])

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/sample_data")
async def get_sample_data():
    # This is just an example. You should replace this with actual data from your database.
    return {
        "characters": [
            {"id": 1, "name": "Giblo Trellis", "backstory": "A mysterious figure with a dark past."},
            {"id": 2, "name": "Elara Moonwhisper", "backstory": "An elven mage seeking ancient knowledge."}
        ],
        "quests": [
            {"id": 1, "title": "The Lost Artifact", "description": "Retrieve a powerful artifact from an ancient tomb."},
            {"id": 2, "title": "Dragon's Lair", "description": "Defeat the dragon terrorizing the nearby village."}
        ]
    }