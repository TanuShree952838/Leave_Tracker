from app.repository.leave_requests import get_leave

def get_leave_request_service(db, employee_id):
    """Service to fetch leave data of individual employee based on employee_id"""
    get_leave(db,employee_id)