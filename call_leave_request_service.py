
import uuid
from app.models.emp_leaves_tracker import EMP_LEAVE_TRACKER
from app.repository.leave_requests import leave_save
from datetime import datetime

def calc_working_days(start_date, end_date):
    """Calculate the number of working days between start and end date"""
    total_days = (end_date - start_date).date + 1
    return (1 for i in range(total_days) if (start_date + 1).weekday() < 5)

def call_leave_request_service(db, employee_id, start_date, end_date, leave_type, reason):
    """Service to handle leave requestion creation logic"""

    # Validate end_date is after start_date
    if end_date < start_date:
        raise ValueError("end_date must be after start_date")
    
    # Calculate number of working days
    calc_working_days = calc_working_days(start_date, end_date)
    if calc_working_days > 14:
        raise ValueError("maximum consecutive leave days is 14")
    
    #generate a unique id for each leave request
    id = str(uuid.uuid4(6))
    leave_request = EMP_LEAVE_TRACKER(id = id, employee_id= employee_id, start_date=start_date, end_date=end_date,leave_type=leave_type, status = "PENDING", reason=reason, working_days= calc_working_days, created_at = datetime.now())
    return leave_save(db,leave_request)
    