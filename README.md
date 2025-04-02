In this assignment I have created two a RESTful APIs service for managing Employee Leave Requests. The service
handle leave request creation with validation rules and retrieval of leave requests.

This is my project dir tree:
├── app
│   ├── database.py
│   ├── models
│   │   └── emp_leaves_tracker.py
│   ├── repository
│   │   └── leave_requests.py
│   └── services
│       ├── call_leave_request_service.py
│       └── get_leave_request_service.py
└── main.py

Setup and Implementation:
I have already setuped vscode in my machine, I install required libraries- fastapi uvicorn, sqlalchemy mainly,
I have implemented two APIs (POST and GET) with FastAPI, following a structured approach,
I break down the api implementation approach and the created services seperately, 
    POST API – Allows employees to submit leave requests.
    Validates leave request data and calculates the number of working days.
    Raises errors if incorrect values are provided.
    Stores the request in the database with a unique 6-digit leave ID generated using UUID.
    
    GET API – Fetches leave request details for a specific employee.
    Accepts employee_id as a parameter.
    Retrieves all leave requests associated with the given employee using SQLAlchemy ORM queries.


Testing instructions:
So we can test it using curl:
1. curl --location 'http://127.0.0.1:8000/api/v1/leave-requests' \
--header 'Accept: application/json' \
--header 'Authorization: Basic <your_auth_token>' \
--form 'employee_id="12443"' \
--form 'start_date="2025-03-01"' \
--form 'end_date="2025-05-01"' \
--form 'leave_type="ANNUAL"' \
--form 'reason="Family vacation to visit parents"'

2. curl --location --request GET 'http://127.0.0.1:8000/api/v1/leave-requests/employee_id=12443' \
--header 'Accept: application/json' '

IDE: Visual Studio Code
Libraries: fastapi, uvicorn, sqlalchemy
Run Server: uvicorn main:app --reload
