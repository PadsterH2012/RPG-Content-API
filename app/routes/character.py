from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.character import Character
from app.schemas.character import CharacterCreate, CharacterUpdate, CharacterResponse

router = APIRouter()

@router.post("/", response_model=CharacterResponse)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    db_character = Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

@router.get("/{character_id}", response_model=CharacterResponse)
def read_character(character_id: int, db: Session = Depends(get_db)):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character

@router.put("/{character_id}", response_model=CharacterResponse)
def update_character(character_id: int, character: CharacterUpdate, db: Session = Depends(get_db)):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    for key, value in character.dict().items():
        setattr(db_character, key, value)
    db.commit()
    db.refresh(db_character)
    return db_character

@router.delete("/{character_id}", response_model=CharacterResponse)
def delete_character(character_id: int, db: Session = Depends(get_db)):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    db.delete(db_character)
    db.commit()
    return db_character