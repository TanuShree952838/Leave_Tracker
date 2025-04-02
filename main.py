from datetime import datetime
from typing import Optional, Dict
from fastapi import FastAPI, Request, Depends
from requests import Session
from app.database import get_db
from app.services import call_leave_request_service, get_leave_request_service
from app.models.emp_leaves_tracker import EMP_LEAVE_TRACKER

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Python - REST API Development"}

@app.post("/api/v1/leave-requests")
def create_leave_requests(employee_id: Optional[str], start_date: Optional[datetime], end_date: Optional[datetime],leave_type: Optional[str], reason: Optional[str], db: Session = Depends(get_db))-> Dict(EMP_LEAVE_TRACKER):
    """doc here"""
    call_leave_request_service(db, employee_id, start_date, end_date, leave_type, reason)

@app.get("/api/v1/leave-requests/{employee_id}")
def create_leave_requests(employee_id: str, db: Session = Depends(get_db)):
    """doc here"""
    get_leave_request_service(db, employee_id)
