from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class UserCreate(BaseModel):
    name: str = Field(
        example="Ashish Patel"
    )

    email: str = Field(
        example="ashishpatel@gmail.com"
    )

    password: str = Field(
        example="Ashish@123"
    )


class UserLogin(BaseModel):
    email: str = Field(
        example="ashishpatel@gmail.com"
    )

    password: str = Field(
        example="Ashish@123"
    )


class Token(BaseModel):
    access_token: str
    token_type: str


class FitnessClassCreate(BaseModel):
    name: str
    dateTime: datetime
    instructor: str
    availableSlots: int

from pydantic import BaseModel

class BookingCreate(BaseModel):
    class_id: int
    client_name: str
    client_email: str

   

class FitnessClassResponse(BaseModel):
    id: int
    name: str
    dateTime: datetime
    instructor: str
    availableSlots: int

    model_config = {
        "from_attributes": True
    }

   


class BookingResponse(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: str

    model_config = {
    "from_attributes": True
}