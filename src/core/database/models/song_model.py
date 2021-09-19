from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from src.core.database.models.base import Base


class Song(Base):

    __tablename__ = 'songs'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255), nullable=False)
    duration_in_seconds = Column('duration', Integer, nullable=False)
    thumbnail_path = Column('thumnail_path', String(255), nullable=True)
    file_path = Column('file_path', String(255), nullable=False)
    created_at = Column('created_at', DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column('updated_at', DateTime, nullable=False, default=datetime.utcnow)
