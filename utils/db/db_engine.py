from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from .db_names import db_names
from utils.db.credentials import Credentials
from ..patterns.singleton import Singleton
from sqlalchemy.orm import Session


class EngineFabricBase:
    CREDS = Credentials.DB_CREDS_BASE

    def __init__(self):
        self.engines = {}
        self._set_engines()

    def create_engine(self, db_name, echo: bool = True, pool_size: int = 5, max_overflow: int = 10):
        print(self.CREDS)
        print()
        engine = create_engine(
            self.CREDS % db_name,
            echo=echo,
            pool_size=pool_size,
            max_overflow=max_overflow
        )
        if not database_exists(engine.url):
            create_database(engine.url)

        return engine.connect(False)

    def _set_engines(self):
        for db_name in db_names:
            self.engines[db_name] = self.create_engine(db_name)


class EngineFabric(EngineFabricBase, metaclass=Singleton):
    pass


class SessionMakerBase:

    @staticmethod
    def get_session(db_name: str) -> Session:
        return Session(bind=EngineFabric().engines[db_name])


class SessionMaker(SessionMakerBase, metaclass=Singleton):
    pass
