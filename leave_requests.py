from app.models.emp_leaves_tracker import EMP_LEAVE_TRACKER


def leave_save(db, leave_request: EMP_LEAVE_TRACKER):
    """save leave request data to the DB table emp_leaves_tracker"""
    db.add(leave_request)
    db.commit()
    db.refresh(leave_request)
    return leave_request

def get_leave(db, employee_id: str):
    """fetch leave data from the DB table based on employee_id"""
    return db.query(EMP_LEAVE_TRACKER).filter(EMP_LEAVE_TRACKER.employee_id == EMP_LEAVE_TRACKER).all()

