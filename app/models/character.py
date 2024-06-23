from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    backstory = Column(Text)
    behaviors = Column(Text)
    sample_speech = Column(Text)
    traits = Column(Text)