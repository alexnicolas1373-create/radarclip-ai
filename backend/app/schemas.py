from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    name: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str
    created_at: datetime

    class Config:
        from_attributes = True


class TrendBase(BaseModel):
    title: str
    platform: str
    topic: str
    score: float


class TrendCreate(TrendBase):
    pass


class TrendOut(TrendBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class VideoBase(BaseModel):
    title: str
    url: str
    platform: str


class VideoCreate(VideoBase):
    pass


class VideoOut(VideoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ClipBase(BaseModel):
    title: str
    start_time: int
    end_time: int
    video_id: int


class ClipCreate(ClipBase):
    pass


class ClipOut(ClipBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
