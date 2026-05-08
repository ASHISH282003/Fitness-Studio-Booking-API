from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(
        String,
        unique=True,
        index=True
    )

    hashed_password = Column(
        String,
        nullable=False
    )

    bookings = relationship(
        "Booking",
        back_populates="user"
    )


class FitnessClass(Base):
    __tablename__ = "fitness_classes"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    date_time = Column(
        DateTime,
        nullable=False
    )

    instructor = Column(
        String,
        nullable=False
    )

    available_slots = Column(
        Integer,
        nullable=False
    )

    bookings = relationship(
        "Booking",
        back_populates="fitness_class"
    )


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    class_id = Column(
        Integer,
        ForeignKey("fitness_classes.id")
    )

    client_name = Column(
        String,
        nullable=False
    )

    client_email = Column(
        String,
        nullable=False
    )

    booked_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="bookings"
    )

    fitness_class = relationship(
        "FitnessClass",
        back_populates="bookings"
    )