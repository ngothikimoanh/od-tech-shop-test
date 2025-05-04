from sqlalchemy import Column, Integer, BigInteger, String, DateTime
from datetime import datetime
from models import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)

    time_order = Column(DateTime, default=datetime.utcnow)
    time_delivered = Column(DateTime, nullable=True)
    time_shipping = Column(DateTime, nullable=True)
    time_cancel = Column(DateTime, nullable=True)

    total_amount = Column(BigInteger, nullable=False)
    total_amount_paid = Column(BigInteger, default=0, nullable=False)

    buyer_phone_number = Column(String(15), nullable=False)
    buyer_name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)

    point_used = Column(BigInteger, nullable=False)
    point = Column(BigInteger, nullable=False)
