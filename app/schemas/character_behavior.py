from pydantic import BaseModel

class CharacterBehaviorBase(BaseModel):
    name: str
    description: str

class CharacterBehaviorCreate(CharacterBehaviorBase):
    pass

class CharacterBehaviorUpdate(CharacterBehaviorBase):
    pass

class CharacterBehaviorResponse(CharacterBehaviorBase):
    id: int

    class Config:
        from_attributes = True