import typing

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import insert

from src.core.database.models.playlist_model import Playlist, association_table
from src.core.database.models.song_model import Song
from src.core.exceptions import SongAlreadyInPlaylistException

USERNAME = 'admin'
PASSWORD = '1234'
SERVER = 'localhost'
DATABASE_NAME = 'my_spotify'

engine = create_engine(f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE_NAME}')


def create_tables() -> None:
    from src.core.database.models.base import Base
    Base.metadata.create_all(engine)


def get_all_songs() -> typing.List[Song]:
    session = Session(bind=engine)
    songs = session.query(Song).all()
    session.close()
    return songs


def get_song(song_id: int) -> Song:
    """
    Retrieves ONE song from the database.
    :param song_id: the ID of the song
    :return: Song object or None (if not found)
    """
    session = Session(bind=engine)
    song = session.query(Song).get(song_id)
    session.close()
    return song


def get_all_playlists() -> typing.List[Playlist]:
    session = Session(bind=engine)
    playlists = session.query(Playlist).all()
    session.close()
    return playlists


def get_playlist(playlist_id: int) -> Playlist:
    """
    Retrieves ONE playlist from the database.
    :param playlist_id: the ID of the playlist
    :return: Playlist object or None (if not found)
    """
    session = Session(bind=engine)
    playlist = session.query(Playlist).get(playlist_id)
    session.close()
    return playlist


def insert_song(song: Song) -> int:
    try:
        session = Session(bind=engine)

        # If the song already exists, return its ID
        database_song = session.query(Song).filter(Song.video_id == song.video_id).first()
        if database_song is not None:
            session.close()
            return database_song.id

        # If the song does not exists, insert it into the database and return the new ID
        session.add(song)
        session.flush()
        song_id = song.id
        session.commit()
        session.close()
        return song_id
    except Exception as e:
        print(e)
        return -1


def insert_song_into_playlist(playlist_id, song_id) -> bool:
    try:
        query = f'SELECT * FROM playlists_songs WHERE playlist_id = {playlist_id} AND song_id = {song_id};'
        result = engine.execute(query)
        result_list = [row[0] for row in result]

        song = get_song(song_id)
        playlist = get_playlist(playlist_id)

        if len(result_list) > 0:
            raise SongAlreadyInPlaylistException(
                f'The song "{song.name}" is already in the playlist "{playlist.name}"')

        statement = insert(association_table).values(playlist_id=playlist_id, song_id=song_id)
        session = Session(bind=engine)
        session.execute(statement)
        session.commit()
        session.close()
        return True
    except Exception as e:
        print(e)
        return False
