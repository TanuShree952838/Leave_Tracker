from datetime import datetime
from sqlalchemy import Column, Date, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EmpLeaveTracker(Base):
    """DB table schema for emp_leaves_tracker table"""
    __tablename__ = "emp_leaves_tracker"

    id = Column(String, primary_key=True)
    employee_id = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    leave_type = Column(String, nullable=False)
    reason = Column(String, nullable=False)
    status = Column(String, nullable=False, default="PENDING")
    working_days = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
