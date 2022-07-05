from sqlalchemy.orm import Session, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Integer, Column, Text, DateTime, Numeric, ForeignKey, Enum, Date
from sqlalchemy.ext.declarative import declarative_base
import datetime

import uuid

from utils.db.db_engine import SessionMaker
from utils.patterns.singleton import Singleton

Base = declarative_base()


class Device:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    phone_type = Column(Text(), nullable=False)
    device_id = Column(Text(), nullable=False)
    device_info = Column(Text(), nullable=False)
    device_os = Column(Text(), nullable=False)
    lang_id = Column(Text(), nullable=False)


class User:
    """
        self.card_number = card_number
        self.date_expire = date_expire

        self.photo = photo
    """

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    phone_number = Column(Text(), nullable=False)
    birth_date = Column(Text(), nullable=False)
    doc_type = Column(Text(), nullable=False)
    doc_series = Column(Text(), nullable=False)
    doc_number = Column(Text(), nullable=False)
