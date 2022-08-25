import uuid

from sqlalchemy import Column, Text, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from utils.db.db_engine import EngineFabric

Base = declarative_base()


class Device(Base):
    __tablename__ = "devices"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    phone_type = Column(Text(), nullable=False)
    device_id = Column(Text(), nullable=False)
    device_info = Column(Text(), nullable=False)
    device_os = Column(Text(), nullable=False)
    lang_id = Column(Text(), nullable=False)
    app_version = Column(Text(), nullable=False)


class User(Base):
    __tablename__ = "users"
    """
        self.card_number = card_number
        self.date_expire = date_expire

        self.photo = photo
    """

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    phone_number = Column(Text(), nullable=False)

    first_name = Column(Text())
    last_name = Column(Text())
    middle_name = Column(Text())

    refresh_token = Column(Text())

    birth_date = Column(Text())
    doc_type = Column(Text())
    doc_series = Column(Text())
    doc_number = Column(Text())
    pinfl = Column(Text())
    residence_of_uz = Column(Boolean(), nullable=False, default=True)

    cards = relationship("Card")


class Card(Base):
    __tablename__ = "cards"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    card_number = Column(Text(), nullable=False)
    date_expire = Column(Text(), nullable=False)

    card_id = Column(Text())
    card_type = Column(Text())
    processing = Column(Text())
    state = Column(Text())
    account = Column(Text())

    user = relationship("User")


if __name__ == "__main__":
    Base.metadata.create_all(EngineFabric().engines["automation_tests_data"])


# class TestDDBBase(BaseDB):
#     __db_name__ = "automation_tests_data"
#
#     def all_users(self, name: str):
#         return self._get_session().query(User).all()


