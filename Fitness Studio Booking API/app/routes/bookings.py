from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import Booking, FitnessClass
from app.schemas import (
    BookingCreate,
    BookingResponse
)
from app.dependencies import (
    get_db,
    get_current_user
)

router = APIRouter(
    tags=["Bookings"]
)


@router.post("/book")
def book_class(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    fitness_class = db.query(FitnessClass).filter(
        FitnessClass.id == booking.class_id
    ).first()

    if not fitness_class:
        raise HTTPException(
            status_code=404,
            detail="Class not found"
        )

    if fitness_class.available_slots <= 0:
        raise HTTPException(
            status_code=400,
            detail="No slots available"
        )

    new_booking = Booking(
        user_id=current_user.id,
        class_id=booking.class_id,
        client_name=booking.client_name,
        client_email=booking.client_email
    )

    fitness_class.available_slots -= 1

    db.add(new_booking)
    db.commit()

    return {
        "message": "Booking successful"
    }


@router.get("/bookings", response_model=list[BookingResponse])
def my_bookings(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    bookings = db.query(Booking).filter(
        Booking.user_id == current_user.id
    ).all()

    return bookings