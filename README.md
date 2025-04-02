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


So, I have created mainly 2 apis(one is POST and one is GET),
I have devided it into services, repositories and define model schema that will have all the data related to employee's leave.

Setup and Implementation:
I have already setuped vscode in my machine, I install required libraries- fastapi uvicorn, sqlalchemy mainly,
I break down the api implementation approach and the created 2 services seperately, 
    Fist, I created post api, that will take data from employee related to its leave request and then calculate the number of working days, based on that we raised error to the employee so that they can pass correct value in param,
    then I have created repository to store the data into the table with unique leave id generated with uuid of 6 digit.

    Second, I have created a get api which will be taking employee_id and based on that it will fetch all the data of that individual employee, I have fetched the data using sqlalchemy orm query to filter the data based on the employee_id only.


Testing instructions:
So we can test it using curl:
1. curl --location 'http://127.0.0.1:8000/api/v1/leave-requests' \
--header 'Accept: application/json' \
--header 'Authorization: Basic ay03ZTk1NzRhZi00MDY2LTRhYTQtOTBjYi05YjQxNzYyYjJhOWE6cy1jMjM0Nzk0Mi0zMTJkLTQxNjItODZlMS1lNjc3ZGU4NDRmZGU=' \
--form 'employee_id="12443"' \
--form 'start_date="\"2025-03-01\""' \
--form 'end_date="\"2025-05-01\""' \
--form 'leave_type="\"ANNUAL\""' \
--form 'reason="\"Family vacation to visit parents\""'

2. curl --location --request POST 'http://127.0.0.1:8000/api/v1/leave-requests/employee_id=12443' \
--header 'Accept: application/json' \
--header 'Authorization: Basic ay03ZTk1NzRhZi00MDY2LTRhYTQtOTBjYi05YjQxNzYyYjJhOWE6cy1jMjM0Nzk0Mi0zMTJkLTQxNjItODZlMS1lNjc3ZGU4NDRmZGU='


Run fastapi server- uvicorn main:app --reload