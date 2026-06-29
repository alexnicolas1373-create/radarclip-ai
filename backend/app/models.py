from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field
from app.database import Base


class User(BaseModel):
    name: str = Field(default="")
    email: str = Field(default="")


class Trend(Base):
    __tablename__ = "trends"

    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, nullable=False)
    source = Column(String, nullable=False)
