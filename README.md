# Employee Leave Tracker

A Django web application for managing employee leave requests with role-based access control.

## Features
- Custom user model with roles: Employee, Manager, Admin
- Employee registration and login
- Employees can apply for leave (Sick, Casual, Earned) and track request status
- Leave balance tracking with automatic deduction on approval
- Managers/Admins can view pending requests and approve/reject them
- Role-based dashboard redirect after login
- Form validation (end date cannot be before start date)
- Custom access-denied page for unauthorized access
- Django admin panel for full data management
- Bootstrap-styled responsive UI

## Tech Stack
- Python, Django
- SQLite (development database)
- HTML, Bootstrap 5

## Setup Instructions

1. Clone the repository

git clone https://github.com/Sudharshan34/employee-leave-tracker.git
cd employee-leave-tracker


2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate


3. Install dependencies

pip install -r requirements.txt


4. Run migrations

python manage.py migrate


5. Create a superuser

python manage.py createsuperuser


6. Run the server

python manage.py runserver


7. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

'''
employee-leave-tracker/
├── accounts/ # custom user model, registration & login
├── leaves/ # leave request model, apply/view/approve logic, leave balance tracking
├── leave_tracker/ # project settings and root URL configuration
├── templates/ # HTML templates for all pages
├── manage.py
└── requirements.txt
'''


## User Roles
- *Employee* — can register, apply for leave, and view their own leave history and balance
- *Manager / Admin* — can view all pending leave requests and approve or reject them

## Future Improvements
- Email notifications on approval/rejection
- REST API for mobile/frontend integration
- Password reset flow
- In-app user role management (currently done via Django admin)

## Author
Kuluru Sudharshan Reddy
