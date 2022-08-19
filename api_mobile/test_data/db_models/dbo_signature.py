from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Integer, Column, Text, DateTime, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import datetime

import uuid

from utils.db.models.base_db_model import BaseDB
from utils.patterns.singleton import Singleton

Base = declarative_base()


def expired_time():
    return datetime.datetime.now() + datetime.timedelta(minutes=1)


class Code(Base):
    __tablename__ = "codes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    secret = Column(Text(), nullable=False)
    phone = Column(Text(), nullable=False)
    created_at = Column(DateTime(), default=datetime.datetime.now, nullable=False)
    expires_at = Column(DateTime(), default=expired_time, nullable=False)
    used_at = Column(DateTime())
    ttl = Column(Integer(), nullable=False)
    template_id = Column(Text(), nullable=False)
    attempts = Column(Numeric(), default=3, nullable=False)
    otp_last_send_at = Column(DateTime(), default=datetime.datetime.now)


class OTP(Base):
    __tablename__ = "otps"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    sign_id = Column(UUID(as_uuid=True), ForeignKey("signatures.id"))
    code = Column(Text(), nullable=False)
    phone = Column(Text(), nullable=False)
    template_id = Column(Text(), nullable=False)
    language = Column(Text(), nullable=False)
    ttl = Column(Integer(), nullable=False)
    expires_at = Column(DateTime(), default=expired_time, nullable=False)
    created_at = Column(DateTime(), default=datetime.datetime.now, nullable=False)
    signature = relationship("Signature")


class Signature(Base):
    __tablename__ = "signatures"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    type_ = Column("type", Integer(), nullable=False)
    attempts = Column(Integer(), nullable=False)
    last_refreshed_at = Column(DateTime(), nullable=True)
    signed_at = Column(DateTime(), nullable=True)
    document_id = Column(Text(), nullable=True)
    created_at = Column(DateTime(), default=datetime.datetime.now, nullable=False)



class DBOSignatureBase(BaseDB):
    __db_name__ = "dbo_signature"

    def sms_key(self, sign_id) -> OTP.code:
        secret = self._get_session().query(OTP).filter(OTP.sign_id == sign_id).one().code
        self._close()
        return secret

    def sign(self, sign_id) -> Signature:
        return self._get_session().query(OTP).filter(OTP.sign_id == sign_id).one().signature


class DBOSignature(DBOSignatureBase, metaclass=Singleton):
    pass
