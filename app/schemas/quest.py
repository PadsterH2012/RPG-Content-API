from pydantic import BaseModel

class QuestBase(BaseModel):
    title: str
    description: str
    difficulty: str
    reward: str

class QuestCreate(QuestBase):
    pass

class QuestUpdate(QuestBase):
    pass

class QuestResponse(QuestBase):
    id: int

    class Config:
        from_attributes = True