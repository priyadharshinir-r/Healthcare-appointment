from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    role: str

class UserCreate(UserBase):
    password: str  

class UserResponse(UserBase):
    user_id: int

    class Config:
        from_attributes = True  


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    date_time: datetime
    status: str

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentResponse(AppointmentBase):
    id: int

    class Config:
        from_attributes = True


class PrescriptionBase(BaseModel):
    appointment_id: int
    doctor_id: int
    patient_id: int
    medicines: str
    notes: Optional[str] = None  

class PrescriptionCreate(PrescriptionBase):
    pass

class PrescriptionResponse(PrescriptionBase):
    id: int

    class Config:
        from_attributes = True
