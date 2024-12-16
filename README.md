# User Profile Management System

---

## Features

1. **User Registration**

   - Users can register by providing their username, email, password, address, phone number, and name.
   - Validation for phone number (10-digit) and email format.

2. **User Login**

   - Users can log in using their credentials.
   - Incorrect username or password results in an error message.

3. **User Dashboard**

   - A protected dashboard page accessible only to logged-in users.

4. **Profile Management**

   - Users can edit their profiles, including updating their username, email, address, phone number, and name.
   - Validations are applied to ensure correct input.

5. **Logout**

   - Users can log out, and their session will be cleared.
---

## Installation and Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- Django 4.0+

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/muhammedshabeen/User-Management
   cd User-Management
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL Database**

   - Create a PostgreSQL database.
   - Update the `DATABASES` setting in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': '<your_database_name>',
             'USER': '<your_database_user>',
             'PASSWORD': '<your_database_password>',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Run Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**

   - Open `http://127.0.0.1:8000/` in your browser.

---

## File Structure

### URLs Configuration

```python
from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('user-login', user_login, name='user_login'),
    path('dashboard', dashboard, name='dashboard'),
    path('signout', signout, name='signout'),
    path('profile', profile, name='profile'),
]
```

### Views

#### Register

Handles user registration with form validation.

#### Login

Authenticates users and redirects to the dashboard.

#### Dashboard

Displays the user's dashboard.

#### Profile

Allows users to edit their profiles.

#### Logout

Logs out the user and clears the session.

---

## Forms

### Registration Form

Handles user registration with validations for phone number, email, and passwords.

### Profile Edit Form

Handles profile editing with field validations.

---

## Database

The project uses **PostgreSQL** as the database backend.

- To set up the database, ensure you update the `DATABASES` setting in `settings.py`.
- Use `python manage.py migrate` to create the required tables.

---


