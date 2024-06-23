from pydantic import BaseModel

class TraitBase(BaseModel):
    name: str
    description: str

class TraitCreate(TraitBase):
    pass

class TraitUpdate(TraitBase):
    pass

class TraitResponse(TraitBase):
    id: int

    class Config:
        from_attributes = True