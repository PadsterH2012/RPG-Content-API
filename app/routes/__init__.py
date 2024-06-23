from fastapi import APIRouter
from . import character, quest, trait, character_behavior, pdf_upload

router = APIRouter()
router.include_router(character.router, prefix="/characters", tags=["characters"])
router.include_router(quest.router, prefix="/quests", tags=["quests"])
router.include_router(trait.router, prefix="/traits", tags=["traits"])
router.include_router(character_behavior.router, prefix="/character_behaviors", tags=["character_behaviors"])
router.include_router(pdf_upload.router, prefix="/pdf", tags=["pdf"])