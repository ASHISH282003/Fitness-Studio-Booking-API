# Fitness Studio Booking API

# Project overview

A simple and practical FastAPI project for managing fitness classes and bookings.

This project allows users to:

- Register and login using JWT authentication
- Create fitness classes
- View upcoming fitness classes
- Book slots in available classes
- View personal bookings
- Prevent overbooking automatically
- Test APIs using Swagger UI

The project was built using FastAPI, SQLAlchemy, SQLite, and JWT authentication.

---

# Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Pydantic
- Passlib (bcrypt hashing)
- Pytest
- Swagger UI

---

# Project Structure

```bash
Fitness Studio Booking API/
│
├── app/
│   ├── routes/
│   │   ├── users.py
│   │   ├── classes.py
│   │   └── bookings.py
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── utils.py
│
├── tests/
│   └── test_main.py
│
├── requirements.txt
├── seed.py
├── README.md
└── fitness.db
```

---

# Features

## Authentication

- User Signup
- User Login
- JWT Token Generation
- Password Hashing using bcrypt
- Protected Routes using Bearer Token
- Token Expiration Handling

## Fitness Classes

- Create new classes
- Fetch all upcoming classes
- Timezone handling using IST
- Stores available slots

## Booking System

- Book a class
- Prevent overbooking
- Reduce slot count automatically
- View logged-in user bookings

## Testing

- Basic unit tests added using pytest
- API root endpoint tested
- Class endpoint tested

## Swagger Documentation

- Interactive API testing using Swagger UI
- Custom example request bodies added

---

# Setup instructions and How to run locally

## 1. Clone Repository

```bash
git clone <repository-url>
cd "Fitness Studio Booking API"
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Server runs at:

```bash
http://127.0.0.1:8000
```

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

ReDoc:

```bash
http://127.0.0.1:8000/redoc
```

---

# Database

The project uses SQLite.

Database file:

```bash
fitness.db
```

Tables are automatically created on startup using:

```python
Base.metadata.create_all(bind=engine)
```

---

# Authentication Flow

## Signup

Endpoint:

```http
POST /signup
```

Example Request:

```json
{
  "name": "Ashish Patel",
  "email": "ashishpatel@example.com",
  "password": "Ashish@123"
}
```

---

## Login

Endpoint:

```http
POST /login
```

Example Request:

```json
{
  "email": "ashishpatel@example.com",
  "password": "Ashish@123"
}
```

Response:

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

---

# Authorization in Swagger

1. Login using `/login`
2. Copy access token
3. Click `Authorize` button in Swagger UI
4. Enter:

```bash
Bearer your_token_here
```

Now protected endpoints can be accessed.

---

# API Endpoints and API usage

## 1. Home Route

```http
GET /
```

Response:

```json
{
  "message": "Fitness Booking API Running"
}
```

---

## 2. Signup

```http
POST /signup
```

Registers a new user.

---

## 3. Login

```http
POST /login
```

Authenticates user and returns JWT token.

---

## 4. Create Class

```http
POST /classes
```

Protected Route.

Example Request:

```json
{
  "name": "Yoga Flow",
  "dateTime": "2026-05-07T10:00:00Z",
  "instructor": "John Doe",
  "availableSlots": 20
}
```

---

## 5. Get Upcoming Classes

```http
GET /classes
```

Returns all upcoming fitness classes.

Example Response:

```json
[
  {
    "id": 1,
    "name": "Yoga Flow",
    "dateTime": "2026-05-07T15:30:00",
    "instructor": "John Doe",
    "availableSlots": 20
  }
]
```

---

## 6. Book a Class

```http
POST /book
```

Protected Route.

Example Request:

```json
{
  "class_id": 1,
  "client_name": "Ashish Patel",
  "client_email": "ashishpatel@example.com"
}
```

Features:

- Prevents overbooking
- Deducts available slot automatically
- Validates class existence

---

## 7. View My Bookings

```http
GET /bookings
```

Protected Route.

Returns all bookings of logged-in user.

---

# Token Expiration

JWT token expiration is implemented using:

```python
expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
```

The expiration value is stored in JWT payload:

```python
to_encode.update({"exp": expire})
```

---

# Timezone Handling

The project stores and compares time using IST timezone.

```python
IST = pytz.timezone("Asia/Kolkata")
```

Upcoming classes are filtered using current IST time.

---

# Unit Testing

Pytest is used for unit testing.

Run tests:

```bash
pytest
```

Example output:

```bash
4 passed
```

---

# Common Issues

## Swagger shows "No operations defined in spec"

Solution:

Make sure routers are included in `main.py`

```python
app.include_router(users.router)
app.include_router(classes.router)
app.include_router(bookings.router)
```

---

## Unauthorized Error

Make sure token is added correctly:

```bash
Bearer your_token
```

---

## Empty Class List

This happens when there are no future classes in database.

Create a class with future date/time.

---



---

# Author

Ashish Patel

---
