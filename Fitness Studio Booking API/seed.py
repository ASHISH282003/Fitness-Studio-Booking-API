from app.database import SessionLocal
from app.models import User, FitnessClass, Booking

from datetime import datetime

db = SessionLocal()

# Prevent duplicate seeding
existing_user = db.query(User).first()

if not existing_user:

    # Users
    users = [
        User(
            name="Ashish Patel",
            email="ashishpatel@gmail.com",
            hashed_password="$2b$12$ujwr.PO9bMctMR9DG5kb9u78tcQ5zfzvFqfYrbA0F8lLa7k5m"
        ),

        User(
            name="Rohit Singh",
            email="rohit@gmail.com",
            hashed_password="$2b$12$.lhvtglz1VsKxudCC2l7Te7HKAmHNGsa.3fRayS"
        ),

        User(
            name="Pravin",
            email="Pravin@gmail.com",
            hashed_password="$2b$12$6EszNy/ki6ZAaiiT7lggPOpVbAU8rWiNgVDX4G3"
        )
    ]

    db.add_all(users)
    db.commit()

    # Fitness Classes
    classes = [
        FitnessClass(
            name="Yoga",
            date_time=datetime(2026, 5, 9, 19, 40, 24),
            instructor="Sam",
            available_slots=8
        ),

        FitnessClass(
            name="Zumba",
            date_time=datetime(2026, 5, 10, 19, 40, 24),
            instructor="Zack",
            available_slots=13
        ),

        FitnessClass(
            name="HIIT",
            date_time=datetime(2026, 5, 11, 19, 40, 24),
            instructor="Prince",
            available_slots=18
        ),

        FitnessClass(
            name="Gym",
            date_time=datetime(2026, 5, 12, 19, 40, 24),
            instructor="Harry",
            available_slots=8
        ),

        FitnessClass(
            name="Cardio",
            date_time=datetime(2026, 5, 13, 19, 40, 24),
            instructor="Kevin",
            available_slots=13
        )
    ]

    db.add_all(classes)
    db.commit()

    # Bookings
    bookings = [
        Booking(
            user_id=1,
            class_id=1,
            client_name="Ashish",
            client_email="ashishpatel@gmail.com"
        ),

        Booking(
            user_id=1,
            class_id=2,
            client_name="Ashish",
            client_email="ashishpatel@gmail.com"
        ),

        Booking(
            user_id=1,
            class_id=3,
            client_name="Ashish",
            client_email="ashishpatel@gmail.com"
        ),

        Booking(
            user_id=1,
            class_id=4,
            client_name="Ashish",
            client_email="ashishpatel@gmail.com"
        ),

        Booking(
            user_id=1,
            class_id=5,
            client_name="Ashish",
            client_email="ashishpatel@gmail.com"
        )
    ]

    db.add_all(bookings)
    db.commit()

    print("Seed data inserted successfully")

else:
    print("Data already exists")

db.close()