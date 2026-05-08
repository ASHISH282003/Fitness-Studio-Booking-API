from fastapi import FastAPI

from app.database import engine, Base
from app.routes import users, classes, bookings

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(
    title="Fitness Booking API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Routers
app.include_router(users.router)
app.include_router(classes.router)
app.include_router(bookings.router)

# Home route
@app.get("/")
def home():
    return {
        "message": "Fitness Booking API Running"
    }