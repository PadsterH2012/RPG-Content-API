from pydantic import BaseModel

class CharacterBase(BaseModel):
    name: str
    backstory: str
    behaviors: str
    sample_speech: str
    traits: str

class CharacterCreate(CharacterBase):
    pass

class CharacterUpdate(CharacterBase):
    pass

class CharacterResponse(CharacterBase):
    id: int

    class Config:
        from_attributes = True