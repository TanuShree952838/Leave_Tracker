from datetime import datetime
from typing import Optional, Dict
from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import call_leave_request_service, get_leave_request_service
from app.models.emp_leaves_tracker import EMP_LEAVE_TRACKER

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Python - REST API Development"}

@app.post("/api/v1/leave-requests")
def create_leave_requests(
    employee_id: Optional[str], 
    start_date: Optional[datetime], 
    end_date: Optional[datetime],
    leave_type: Optional[str], 
    reason: Optional[str], 
    db: Session = Depends(get_db)
) -> Dict:
    """
    Create a new leave request by an employee.
    This will handle validation and save the leave request to the database.
    """
    # Call service to handle leave request creation
    leave_request = call_leave_request_service(
        db, 
        employee_id, 
        start_date, 
        end_date, 
        leave_type, 
        reason
    )
    return {"message": "Leave request created successfully", "leave_request": leave_request}


@app.get("/api/v1/leave-requests/{employee_id}")
def get_leave_requests(
    employee_id: str, 
    db: Session = Depends(get_db)
) -> Dict:
    """
    Retrieve all leave requests for an individual employee.
    """
    leave_requests = get_leave_request_service(db, employee_id)
    if not leave_requests:
        return {"message": "No leave requests found for this employee"}
    return {"employee_id": employee_id, "leave_requests": leave_requests}
