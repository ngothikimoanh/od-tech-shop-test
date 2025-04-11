from sqlalchemy import Column, String, Text, DateTime
from models import Base


class DjangoSession(Base):
    __tablename__ = "django_session"

    session_key = Column(String(40), primary_key=True)
    session_data = Column(Text, nullable=False)
    expire_date = Column(DateTime, nullable=False)
