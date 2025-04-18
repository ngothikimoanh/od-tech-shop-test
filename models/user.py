from sqlalchemy import Column, Integer, String, DATETIME, BigInteger,Enum
from models import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String(255), nullable=False)

    phone_number = Column(String(15), nullable=False, index=True, unique=True)
    role = Column(String(32), nullable=True)
    name = Column(String(150), nullable=True)
    points = Column(BigInteger, default=0, nullable=False)
    address = Column(String(256), nullable=True)
    birthday = Column(DATETIME, nullable=True)
    email = Column(String, nullable=True)
