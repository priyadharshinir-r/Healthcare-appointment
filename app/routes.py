from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app import crud
from app.config import get_db
from app.schemas import UserCreate, UserResponse, AppointmentCreate, AppointmentResponse, PrescriptionCreate, PrescriptionResponse
from app.dependencies import get_current_user, get_current_admin_user

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin_user)
):
    return crud.create_user(db, user)



@router.post("/appointments/", response_model=AppointmentResponse)
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.create_appointment(db, appointment)


@router.get("/appointments/", response_model=List[AppointmentResponse])
def read_appointments(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.get_all_appointments(db)



@router.post("/prescriptions/", response_model=PrescriptionResponse)
def create_prescription(
    prescription: PrescriptionCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.create_prescription(db, prescription)


@router.get("/prescriptions/", response_model=List[PrescriptionResponse])
def read_prescriptions(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.get_all_prescriptions(db)
