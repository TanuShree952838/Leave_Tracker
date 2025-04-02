from datetime import datetime
from sqlalchemy import Column, Date, String

def EMP_LEAVE_TRACKER(Base):
    """DB table schema for emp_leave_tracker table"""
    __tablename__ = "emp_leaves_tracker"

    id = Column(String, primary_key= True)
    employee_id = Column(String, nullable= False)
    start_date = Column(Date, nullable= False)
    end_date = Column(Date, nullable= False)
    leave_type = Column(String, nullable= False)
    reason = Column(String, nullable= False)
    status = Column(String, nullable= False, default= "PENDING")
    working_days = Column(int, nullable= False)
    created_at = Column(Date, nullable= False, default = datetime.now())



    
