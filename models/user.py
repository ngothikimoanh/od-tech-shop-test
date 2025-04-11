from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime

from models import Base


class Role:
    ADMIN = "admin"
    EMPLOYEE = "employee"
    GUEST = "guest"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(150), nullable=True)
    last_name = Column(String(150), nullable=True)
    email = Column(String, nullable=True)
    role = Column(String(10), default=Role.GUEST)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    phone_number = Column(String(15), nullable=False, index=True, unique=True)
    password = Column(String(255), nullable=False)
    is_verify_phone_number = Column(Boolean, default=False)
    is_verify_email = Column(Boolean, default=False)
    points = Column(Float, default=0.0)
    date_joined = Column(DateTime, default=datetime.utcnow)
    last_password_change = Column(DateTime, default=datetime.utcnow)
