<<<<<<< HEAD
# Django JWT Authentication Demo

This project demonstrates JWT (JSON Web Token) authentication in a Django application with Django REST Framework.

## Features

- User registration (signup) and login
- JWT token authentication for API endpoints
- Access and refresh token functionality
- Token expiration and renewal
- Login activity tracking
- Protected API endpoints

## Overview

This application demonstrates how JWT authentication works in a Django project:

1. Users can create accounts via the signup page
2. Upon login, users receive JWT access and refresh tokens
3. The access token can be used to authenticate API requests
4. When the access token expires, the refresh token can be used to get a new one
5. Login history is tracked and displayed on the user's profile

## Installation

1. Clone the repository
2. Create a virtual environment and activate it:

```bash
python -m venv env
env\Scripts\activate
```

3. Install dependencies:

```bash
pip install djangorestframework djangorestframework-simplejwt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

## Project Structure

- `api/` - Django app containing views, models and URLs
- `jwt_project/` - Main Django project settings
- `templates/` - HTML templates
- `static/` - Static files (CSS)

## Usage

1. **Sign up**: Create a new user account by visiting `/api/signup/`
2. **Log in**: Log in with your credentials at `/api/login/`
3. **View profile**: After login, view your JWT tokens at `/api/profile/`
4. **Protected API**: Test token authentication at `/api/protected/`

## JWT Configuration

- Access Token lifetime: 5 minutes
- Refresh Token lifetime: 1 day

## Technologies Used

- Django 5.2.1
- Django REST Framework 3.16.0
- djangorestframework-simplejwt 5.5.0
- PyJWT 2.9.0
- SQLite (database)
- Bootstrap 5 (frontend)

## Notes

This is a demonstration project intended to show how JWT authentication works. In a production environment, additional security measures would be required.
=======
# Django JWT Authentication Demo

This project demonstrates JWT (JSON Web Token) authentication in a Django application with Django REST Framework.

## Features

- User registration (signup) and login
- JWT token authentication for API endpoints
- Access and refresh token functionality
- Token expiration and renewal
- Login activity tracking
- Protected API endpoints

## Overview

This application demonstrates how JWT authentication works in a Django project:

1. Users can create accounts via the signup page
2. Upon login, users receive JWT access and refresh tokens
3. The access token can be used to authenticate API requests
4. When the access token expires, the refresh token can be used to get a new one
5. Login history is tracked and displayed on the user's profile

## Installation

1. Clone the repository
2. Create a virtual environment and activate it:

```bash
python -m venv env
env\Scripts\activate
```

3. Install dependencies:

```bash
pip install djangorestframework djangorestframework-simplejwt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

## Project Structure

- `api/` - Django app containing views, models and URLs
- `jwt_project/` - Main Django project settings
- `templates/` - HTML templates
- `static/` - Static files (CSS)

## Usage

1. **Sign up**: Create a new user account by visiting `/api/signup/`
2. **Log in**: Log in with your credentials at `/api/login/`
3. **View profile**: After login, view your JWT tokens at `/api/profile/`
4. **Protected API**: Test token authentication at `/api/protected/`

## JWT Configuration

- Access Token lifetime: 5 minutes
- Refresh Token lifetime: 1 day

## Technologies Used

- Django 5.2.1
- Django REST Framework 3.16.0
- djangorestframework-simplejwt 5.5.0
- PyJWT 2.9.0
- SQLite (database)
- Bootstrap 5 (frontend)

## Notes

This is a demonstration project intended to show how JWT authentication works. In a production environment, additional security measures would be required.
>>>>>>> 1d2a47fef390eff824b3bc7cf2ea9d7e421b8492
