from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Trait(Base):
    __tablename__ = "traits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)