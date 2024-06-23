from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    difficulty = Column(String)
    reward = Column(String)