from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.trait import Trait
from app.schemas.trait import TraitCreate, TraitUpdate, TraitResponse

router = APIRouter()

@router.post("/", response_model=TraitResponse)
def create_trait(trait: TraitCreate, db: Session = Depends(get_db)):
    db_trait = Trait(**trait.dict())
    db.add(db_trait)
    db.commit()
    db.refresh(db_trait)
    return db_trait

@router.get("/{trait_id}", response_model=TraitResponse)
def read_trait(trait_id: int, db: Session = Depends(get_db)):
    db_trait = db.query(Trait).filter(Trait.id == trait_id).first()
    if db_trait is None:
        raise HTTPException(status_code=404, detail="Trait not found")
    return db_trait

@router.put("/{trait_id}", response_model=TraitResponse)
def update_trait(trait_id: int, trait: TraitUpdate, db: Session = Depends(get_db)):
    db_trait = db.query(Trait).filter(Trait.id == trait_id).first()
    if db_trait is None:
        raise HTTPException(status_code=404, detail="Trait not found")
    for key, value in trait.dict().items():
        setattr(db_trait, key, value)
    db.commit()
    db.refresh(db_trait)
    return db_trait

@router.delete("/{trait_id}", response_model=TraitResponse)
def delete_trait(trait_id: int, db: Session = Depends(get_db)):
    db_trait = db.query(Trait).filter(Trait.id == trait_id).first()
    if db_trait is None:
        raise HTTPException(status_code=404, detail="Trait not found")
    db.delete(db_trait)
    db.commit()
    return db_trait