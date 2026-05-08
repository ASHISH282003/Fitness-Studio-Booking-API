from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import pytz

from app.models import FitnessClass
from app.schemas import (
    FitnessClassCreate,
    FitnessClassResponse
)
from app.dependencies import (
    get_db,
    get_current_user
)

router = APIRouter(
    prefix="/classes",
    tags=["Classes"]
)

IST = pytz.timezone("Asia/Kolkata")


@router.post("")
def create_class(
    fitness_class: FitnessClassCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    ist_time = fitness_class.dateTime.astimezone(IST)

    new_class = FitnessClass(
        name=fitness_class.name,
        date_time=ist_time,
        instructor=fitness_class.instructor,
        available_slots=fitness_class.availableSlots
    )

    db.add(new_class)
    db.commit()
    db.refresh(new_class)

    return {
        "message": "Class created successfully",
        "data": new_class
    }


@router.get("", response_model=list[FitnessClassResponse])
def get_classes(db: Session = Depends(get_db)):
    classes = db.query(FitnessClass).filter(
        FitnessClass.date_time >= datetime.now(IST)
    ).all()

    return [
    {
        "id": cls.id,
        "name": cls.name,
        "dateTime": cls.date_time,
        "instructor": cls.instructor,
        "availableSlots": cls.available_slots
    }
    for cls in classes
]