from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.character_behavior import CharacterBehavior
from app.schemas.character_behavior import CharacterBehaviorCreate, CharacterBehaviorUpdate, CharacterBehaviorResponse

router = APIRouter()

@router.post("/", response_model=CharacterBehaviorResponse)
def create_character_behavior(character_behavior: CharacterBehaviorCreate, db: Session = Depends(get_db)):
    db_character_behavior = CharacterBehavior(**character_behavior.dict())
    db.add(db_character_behavior)
    db.commit()
    db.refresh(db_character_behavior)
    return db_character_behavior

@router.get("/{character_behavior_id}", response_model=CharacterBehaviorResponse)
def read_character_behavior(character_behavior_id: int, db: Session = Depends(get_db)):
    db_character_behavior = db.query(CharacterBehavior).filter(CharacterBehavior.id == character_behavior_id).first()
    if db_character_behavior is None:
        raise HTTPException(status_code=404, detail="Character behavior not found")
    return db_character_behavior

@router.put("/{character_behavior_id}", response_model=CharacterBehaviorResponse)
def update_character_behavior(character_behavior_id: int, character_behavior: CharacterBehaviorUpdate, db: Session = Depends(get_db)):
    db_character_behavior = db.query(CharacterBehavior).filter(CharacterBehavior.id == character_behavior_id).first()
    if db_character_behavior is None:
        raise HTTPException(status_code=404, detail="Character behavior not found")
    for key, value in character_behavior.dict().items():
        setattr(db_character_behavior, key, value)
    db.commit()
    db.refresh(db_character_behavior)
    return db_character_behavior

@router.delete("/{character_behavior_id}", response_model=CharacterBehaviorResponse)
def delete_character_behavior(character_behavior_id: int, db: Session = Depends(get_db)):
    db_character_behavior = db.query(CharacterBehavior).filter(CharacterBehavior.id == character_behavior_id).first()
    if db_character_behavior is None:
        raise HTTPException(status_code=404, detail="Character behavior not found")
    db.delete(db_character_behavior)
    db.commit()
    return db_character_behavior