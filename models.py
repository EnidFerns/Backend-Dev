from sqlalchemy import Column, Integer, String

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field


class Table(BaseModel):
    __tablename__ = "TableData"

    date  = Column(TIMESTAMP(timezone=True))
    chart_type  = Column(String)
    customer_id = Column(Integer)
    customer_name = Column(String)
    days_overdue = Column(Integer)
    amount_outstanding = Column(Integer)
    recovery = Column(Integer)


