from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from src.core.database.models.base import Base


class Song(Base):

    __tablename__ = 'songs'

    id = Column('id', Integer, primary_key=True)
    thumbnail_path = Column('thumbnail_path', String(255), nullable=True)
    name = Column('name', String(255), nullable=False)
    duration_in_seconds = Column('duration', Integer, nullable=False)
    video_id = Column('video_id', String(255), nullable=False)
    file_path = Column('file_path', String(255), nullable=False)
    created_at = Column('created_at', DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column('updated_at', DateTime, nullable=False, default=datetime.utcnow)
