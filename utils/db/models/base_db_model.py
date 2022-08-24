from sqlalchemy.orm import Session

from utils.db.db_engine import SessionMaker


class BaseDB:
    __db_name__ = None

    def __init__(self):
        self._session: Session = None

    def _get_session(self) -> Session:
        if not self._session:
            self._session = SessionMaker().get_session(self.__db_name__)
        return self._session

    def _close(self):
        self._session.close()
        self._session = None
