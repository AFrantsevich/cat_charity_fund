from datetime import datetime

from sqlalchemy import BOOLEAN, Column, DateTime, Integer

from app.core.db import Base


class CharityDonationAbc(Base):
    __abstract__ = True
    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(BOOLEAN, default=0)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)
