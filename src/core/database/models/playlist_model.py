from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship

from src.core.database.models.base import Base

association_table = Table(
    'playlists_songs', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('playlist_id', ForeignKey('playlists.id')),
    Column('song_id', ForeignKey('songs.id')),
    Column('created_at', DateTime, default=datetime.utcnow),
    Column('updated_at', DateTime, default=datetime.utcnow)
)


class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255), nullable=False)
    songs = relationship('Song', secondary=association_table)
    created_at = Column('created_at', DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column('updated_at', DateTime, nullable=False, default=datetime.utcnow)

    def get_songs(self, engine):
        query = f'SELECT song_id FROM playlists_songs WHERE playlist_id = {self.id};'
        result = engine.execute(query)
        songs = [row[0] for row in result]
        return songs
