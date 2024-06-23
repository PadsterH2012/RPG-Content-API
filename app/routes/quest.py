from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.quest import Quest
from app.schemas.quest import QuestCreate, QuestUpdate, QuestResponse

router = APIRouter()

@router.post("/", response_model=QuestResponse)
def create_quest(quest: QuestCreate, db: Session = Depends(get_db)):
    db_quest = Quest(**quest.dict())
    db.add(db_quest)
    db.commit()
    db.refresh(db_quest)
    return db_quest

@router.get("/{quest_id}", response_model=QuestResponse)
def read_quest(quest_id: int, db: Session = Depends(get_db)):
    db_quest = db.query(Quest).filter(Quest.id == quest_id).first()
    if db_quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    return db_quest

@router.put("/{quest_id}", response_model=QuestResponse)
def update_quest(quest_id: int, quest: QuestUpdate, db: Session = Depends(get_db)):
    db_quest = db.query(Quest).filter(Quest.id == quest_id).first()
    if db_quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    for key, value in quest.dict().items():
        setattr(db_quest, key, value)
    db.commit()
    db.refresh(db_quest)
    return db_quest

@router.delete("/{quest_id}", response_model=QuestResponse)
def delete_quest(quest_id: int, db: Session = Depends(get_db)):
    db_quest = db.query(Quest).filter(Quest.id == quest_id).first()
    if db_quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    db.delete(db_quest)
    db.commit()
    return db_quest