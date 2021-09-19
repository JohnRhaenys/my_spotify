from sqlalchemy import create_engine

USERNAME = 'admin'
PASSWORD = '1234'
SERVER = 'localhost'
DATABASE_NAME = 'my_spotify'


class DataManager:

    @staticmethod
    def create_tables():

        # These imports must stay here in order
        # for SQL Alchemy to create the tables
        from src.core.database.models.base import Base

        engine = create_engine(f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE_NAME}')
        Base.metadata.create_all(engine)
